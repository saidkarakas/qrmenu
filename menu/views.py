from django.shortcuts import render
from django.core.cache import cache
from .models import Category, MenuItem
from django.db.models import Prefetch

def menu_view(request):
    # Try to get categories from cache
    categories = cache.get('menu_categories')
    
    if categories is None:
        # Fetch categories and prefetch only active items
        active_items_prefetch = Prefetch(
            'items',
            queryset=MenuItem.objects.filter(is_active=True)
        )
        
        categories = list(Category.objects.prefetch_related(active_items_prefetch).all())
        
        # Save to cache for 1 day, it will be invalidated by signals on changes
        cache.set('menu_categories', categories, timeout=60*60*24)

    return render(request, 'menu/index.html', {'categories': categories})

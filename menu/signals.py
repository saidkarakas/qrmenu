from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Category, MenuItem

@receiver(post_save, sender=Category)
@receiver(post_delete, sender=Category)
@receiver(post_save, sender=MenuItem)
@receiver(post_delete, sender=MenuItem)
def clear_menu_cache(sender, **kwargs):
    """
    Kategori veya ürün eklendiğinde, silindiğinde veya güncellendiğinde (fiyat değişimi vb.)
    müşteri menü önbelleğini (cache) temizler.
    """
    cache.delete('menu_categories')

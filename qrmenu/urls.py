from django.contrib import admin
from django.urls import path
from menu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu_view, name='menu'),
]

# Admin Panel Customization
admin.site.site_header = "Pideci Admin Paneli"
admin.site.site_title = "Pideci Admin"
admin.site.index_title = "Yönetim Paneline Hoşgeldiniz"

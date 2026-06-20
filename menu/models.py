from django.db import models

class Category(models.Model):
    name = models.CharField("Kategori Adı", max_length=100)
    order_index = models.IntegerField("Sıralama", default=0, help_text="Küçük sayı önce gösterilir.")

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"
        ordering = ['order_index', 'name']

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items', verbose_name="Kategori")
    name = models.CharField("Ürün Adı", max_length=200)
    description = models.TextField("Açıklama/İçindekiler", blank=True, help_text="Müşteriye gösterilecek ürün detayı.")
    price = models.DecimalField("Fiyat (₺)", max_digits=10, decimal_places=2)
    image_url = models.URLField("Görsel Linki", blank=True, help_text="Örn: https://example.com/pide.jpg")
    is_active = models.BooleanField("Aktif (Menüde Göster)", default=True)

    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"
        ordering = ['category__order_index', 'name']

    def __str__(self):
        return self.name

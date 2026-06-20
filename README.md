# 🍕 Pideci Said — Dinamik QR Menü

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?logo=django&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

Bir pide fırını (veya restoran/kafe) için özel olarak geliştirilmiş **Dinamik ve Mobile-First** bir QR Menü uygulamasıdır. Sipariş/sepet içermez (Read-Only). Sadece müşterilere güncel menüyü, fotoğrafları ve fiyatları en hızlı ve modern şekilde sunmayı amaçlar.

İşletme sahibi, yönetim paneline (Django Admin) girerek menüdeki tüm ürünleri ve fiyatları **koda hiç dokunmadan** anında güncelleyebilir.

---

## 🚀 Özellikler

- **Modern ve Premium Tasarım:** Glassmorphism detayları, modern tipografi (Inter & Outfit) ve yüksek kaliteli gölge/blur efektleriyle göz alıcı bir arayüz.
- **Mobile-First & Çok Hızlı:** Yatay kaydırılabilir, yapışkan (sticky) kategori menüsüyle üstün kullanıcı deneyimi (UX).
- **Yönetim Paneli (Admin):** Django'nun yerleşik paneli ile ürün ekleme, silme, fiyat güncelleme ve ürünü pasife alma işlemleri tek tıkla.
- **Önbellekleme (Caching):** Her menü isteğinde veritabanını yormamak için sayfa önbelleğe alınır. Admin panelinden bir değişiklik yapıldığında önbellek otomatik olarak temizlenir.
- **Sıfır Bağımlılık Frontend:** Harici JS/CSS kütüphanesi kullanılmadan ultra hızlı sayfa yüklemesi.

---

## 🛠️ Kullanılan Teknolojiler

| Katman | Teknoloji |
|---|---|
| **Backend** | Python 3, Django 6.0 |
| **Veritabanı** | SQLite |
| **Frontend** | HTML5, Vanilla CSS3, Vanilla JavaScript |
| **Tipografi** | Google Fonts (Inter, Outfit) |
| **Deploy** | PythonAnywhere |

---

## ⚙️ Teknik Detaylar

- **Django ORM** ile `Category → MenuItem` ilişkisel veri modeli
- **Prefetch Related** ile N+1 sorgu optimizasyonu
- **Django Signals** (`post_save`, `post_delete`) ile event-driven cache invalidation
- **LocMemCache** backend ile performanslı önbellekleme
- **Intersection Observer API** ile scroll-based aktif kategori navigasyonu
- **Glassmorphism** + sticky navigation ile framework'süz premium UI

---

## 💻 Kurulum ve Çalıştırma (Lokal Ortam)

```bash
# 1. Repoyu klonlayın
git clone https://github.com/saidkarakas/qrmenu.git
cd qrmenu

# 2. Sanal ortam oluşturun
python -m venv venv

# Windows
.\venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# 3. Bağımlılıkları yükleyin
pip install -r requirements.txt

# 4. Veritabanını oluşturun
python manage.py makemigrations menu
python manage.py migrate
python manage.py createsuperuser

# 5. Sunucuyu başlatın
python manage.py runserver
```

Menü: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
Admin Paneli: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🌍 Deploy (PythonAnywhere)

1. [PythonAnywhere.com](https://www.pythonanywhere.com) üzerinden ücretsiz hesap açın.
2. **Web** sekmesinden "Add a new web app" → **Manual Configuration** → Python 3 seçin.
3. **Bash** konsolunda:

```bash
git clone https://github.com/saidkarakas/qrmenu.git
cd qrmenu
mkvirtualenv --python=/usr/bin/python3.10 qrmenu-venv
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

4. **Web** sekmesinde:
   - **Source code:** `/home/KULLANICI/qrmenu`
   - **Virtualenv:** `/home/KULLANICI/.virtualenvs/qrmenu-venv`
   
5. **WSGI dosyasını** düzenleyin:

```python
import os
import sys

path = '/home/KULLANICI/qrmenu'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'qrmenu.settings'
os.environ['DJANGO_SECRET_KEY'] = 'buraya-guclu-bir-secret-key-koyun'
os.environ['DJANGO_DEBUG'] = 'False'
os.environ['DJANGO_ALLOWED_HOSTS'] = 'KULLANICI.pythonanywhere.com'
os.environ['DJANGO_CSRF_TRUSTED_ORIGINS'] = 'https://KULLANICI.pythonanywhere.com'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

6. **Static files** ayarı (Web sekmesi):
   - URL: `/static/`
   - Directory: `/home/KULLANICI/qrmenu/staticfiles`

7. Yeşil **Reload** butonuna basın. 🎉

> ⚠️ `KULLANICI` ve `saidkarakas` yazan yerleri kendi kullanıcı adlarınızla değiştirmeyi unutmayın.

---

## 📁 Proje Yapısı

```
qrmenu/
├── manage.py
├── requirements.txt
├── qrmenu/              # Proje konfigürasyonu
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── menu/                # Ana uygulama
│   ├── models.py        # Category & MenuItem modelleri
│   ├── views.py         # Cache + Prefetch ile menü view
│   ├── admin.py         # Admin panel yapılandırması
│   └── signals.py       # Otomatik cache temizleme
├── templates/menu/
│   └── index.html
└── static/
    ├── css/styles.css
    ├── js/main.js
    └── images/
```

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.

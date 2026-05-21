from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# BURAYI GÜNCELLEDİK: redirect_to_index fonksiyonunu da import ettik
from core.views import index, redirect_to_index

urlpatterns = [
    path('admin/', admin.site.urls),
    # 2. Ana sayfayı ('') senin yazdığın index fonksiyonuna bağla
    path('', index, name='index'),

    # 3. Contact ile ilgili sayfaları (örneğin iletişim formu) '/contact/' altına al
    path('contact/', include('contact.urls')),

    # Artık sistem redirect_to_index'in nereden geldiğini biliyor
    path('<slug>/', redirect_to_index, name='redirect_urls'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
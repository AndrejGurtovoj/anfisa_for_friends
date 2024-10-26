from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('homepage.urls')),
    path('about/', include('about.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('contest/', include('contest.urls')),
    path('ice_cream/', include('ice_cream.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

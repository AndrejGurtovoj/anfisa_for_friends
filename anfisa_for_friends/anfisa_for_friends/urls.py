from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


urlpatterns = [
    path('', include('homepage.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('homepage:index'),
        ),
        name='registration',
    ),
    path('about/', include('about.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('contest/', include('contest.urls')),
    path('ice_cream/', include('ice_cream.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

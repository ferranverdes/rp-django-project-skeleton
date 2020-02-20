from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

API_PATH = 'api/v1/'

urlpatterns = [
	path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
	path('token-auth/', obtain_auth_token, name='token_auth'),
	path(API_PATH, include('apps.location.urls')),
	path(API_PATH, include('apps.studies.urls')),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path, include
from rest_framework import routers
from apps.location import views

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
router.register('countries', views.CountryView)

translations_router = routers.DefaultRouter()
translations_router.register('languages', views.LanguageTranslationView)
translations_router.register('countries', views.CountryTranslationView)

urlpatterns = [
	path('', include(router.urls)),
	path('translations/', include(translations_router.urls)),
]

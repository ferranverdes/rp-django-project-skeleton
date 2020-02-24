from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('categories', views.CategoryView)
router.register('courses', views.CourseView)

urlpatterns = [
	path('', include(router.urls)),
]

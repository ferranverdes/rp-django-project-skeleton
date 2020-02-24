from django.shortcuts import render
from rest_framework import viewsets
from skeleton import permissions
from . import models, serializers

class CategoryView(viewsets.ModelViewSet):
	queryset = models.Category.objects.all()
	serializer_class = serializers.CategorySerializer
	permission_classes = [permissions.ReadOnly]

class CourseView(viewsets.ModelViewSet):
	queryset = models.Course.objects.all()
	serializer_class = serializers.CourseSerializer
	permission_classes = [permissions.ReadOnly]

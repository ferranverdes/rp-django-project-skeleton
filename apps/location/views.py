from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from skeleton import permissions
from apps.location import models, serializers

class LanguageView(viewsets.ModelViewSet):
	queryset = models.Language.objects.all()
	serializer_class = serializers.LanguageSerializer
	permission_classes = [permissions.IsAccountAdminOrReadOnly]

class LanguageTranslationView(viewsets.ModelViewSet):
	queryset = models.LanguageTranslation.objects.all()
	serializer_class = serializers.LanguageTranslationSerializer
	permission_classes = [permissions.IsAccountAdminOrReadOnly]
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ('translated_to__alpha2',) # GET /api/v1/translations/languages/?translated_to__alpha2=ES

class CountryView(viewsets.ModelViewSet):
	queryset = models.Country.objects.all()
	serializer_class = serializers.CountrySerializer
	permission_classes = [permissions.IsAccountAdminOrReadOnly]

class CountryTranslationView(viewsets.ModelViewSet):
	queryset = models.CountryTranslation.objects.all()
	serializer_class = serializers.CountryTranslationSerializer
	permission_classes = [permissions.IsAccountAdminOrReadOnly]

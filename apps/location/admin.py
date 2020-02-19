from django.contrib import admin
from apps.location import models

@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
	pass

@admin.register(models.LanguageTranslation)
class LanguageTranslationAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
	pass

@admin.register(models.CountryTranslation)
class CountryTranslationAdmin(admin.ModelAdmin):
	pass

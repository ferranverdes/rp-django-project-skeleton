from django.contrib import admin
from . import models

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
	pass

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	pass

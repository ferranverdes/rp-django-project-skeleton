from django.db import models

class Category(models.Model):
	""" It refers to a political nation from the world. """
	name = models.CharField(max_length=70)

	def __str__(self):
		return f'{self.name}'

	class Meta:
		verbose_name_plural = "Categories"

class Course(models.Model):
	""" It refers to a political nation from the world. """
	title = models.CharField(max_length=50)
	subtitle = models.CharField(max_length=100, blank=True)
	description = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified_on = models.DateTimeField(auto_now=True)
	preview_image = models.ImageField(upload_to="previews/%Y/%m/%d")
	categories = models.ManyToManyField(Category, related_name='courses', blank=True)

	def __str__(self):
		return f'{self.title}'

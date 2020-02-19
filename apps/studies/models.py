from django.db import models

class Course(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified_on = models.DateTimeField(auto_now=True)
	preview_image = models.ImageField(upload_to="previews/%Y/%m/%d")

	def __str__(self):
		return f'{self.title}'

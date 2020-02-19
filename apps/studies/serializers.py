from rest_framework import serializers
from . import models

class CourseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Course
		fields = '__all__'

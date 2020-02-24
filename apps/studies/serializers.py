from rest_framework import serializers
from . import models

class CourseSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = models.Course
		fields = '__all__'
		depth = 1

class CategorySerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)
	# courses = CourseSerializer(read_only=True, many=True)

	class Meta:
		model = models.Category
		fields = '__all__'

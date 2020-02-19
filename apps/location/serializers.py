from rest_framework import serializers
from apps.location import models

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = models.Language
		fields = '__all__'

class LanguageTranslationSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = models.LanguageTranslation
		fields = '__all__'
		depth = 1

class CountrySerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = models.Country
		fields = '__all__'

class CountryTranslationSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.IntegerField(read_only=True)

	class Meta:
		model = models.CountryTranslation
		fields = '__all__'
		depth = 1

class AddressSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Address
		fields = '__all__'

from django.db import models
from django.core import validators as core_validators
from skeleton import validators

class Language(models.Model):
	"""	It refers to the languages spoken by humans. """
	name = models.CharField(max_length=30, unique=True)
	alpha2 = models.CharField(
		max_length=2,
		validators=[
			core_validators.MinLengthValidator(2),
			validators.IsAlphaValidator
		]
	)

	def save(self,  *args, **kwargs):
		self.name = self.name.lower().capitalize()
		self.alpha2 = self.alpha2.upper()
		super(Language, self).save(*args, **kwargs)

	def __str__(self):
		return f'{self.name} ({self.alpha2})'

class LanguageTranslation(models.Model):
	""" It refers to the Language model but translated into another language. """
	translated_to = models.ForeignKey(Language, on_delete=models.CASCADE)
	base_language = models.ForeignKey(
		Language,
		on_delete=models.CASCADE,
		related_name="translations"
	)
	name = models.CharField(max_length=30, blank=False)

	class Meta:
		unique_together = ('translated_to', 'base_language', )

	def save(self,  *args, **kwargs):
		self.name = self.name.lower().capitalize()
		super(LanguageTranslation, self).save(*args, **kwargs)

	def __str__(self):
		return f'{self.name} | {self.translated_to.alpha2}'

class Country(models.Model):
	""" It refers to a political nation from the world. """
	name = models.CharField(max_length=30, unique=True)
	alpha2 = models.CharField(
		unique=True,
		max_length=2,
		validators=[
			core_validators.MinLengthValidator(2),
			validators.IsAlphaValidator
		]
	)
	alpha3 = models.CharField(
		unique=True,
		max_length=3,
		validators=[
			core_validators.MinLengthValidator(3),
			validators.IsAlphaValidator
		]
	)
	numeric_code = models.IntegerField(
		validators=[
			core_validators.MinValueValidator(1),
			core_validators.MaxValueValidator(999)
		]
	)
	telephone_prefix =  models.IntegerField(
		validators=[
			core_validators.MinValueValidator(1),
			core_validators.MaxValueValidator(1999)
		]
	)

	class Meta:
		verbose_name_plural = "Countries"

	def save(self,  *args, **kwargs):
		self.name = self.name.lower().capitalize()
		self.alpha2 = self.alpha2.upper()
		self.alpha3 = self.alpha3.upper()
		super(Country, self).save(*args, **kwargs)

	def __str__(self):
		return f'{self.name} ({self.alpha3})'

class CountryTranslation(models.Model):
	""" It refers to the Country model but translated into another language. """
	translated_to = models.ForeignKey(Language, on_delete=models.CASCADE)
	base_country = models.ForeignKey(
		Country,
		on_delete=models.CASCADE,
		related_name="translations"
	)
	name = models.CharField(max_length=30, blank=False)

	class Meta:
		unique_together = ('translated_to', 'base_country', )

	def save(self,  *args, **kwargs):
		self.name = self.name.lower().capitalize()
		super(CountryTranslation, self).save(*args, **kwargs)

	def __str__(self):
		return f'{self.name} | {self.translated_to.alpha2}'

class StreetType(models.Model):
	""" It refers to types of streets used to define an address. """
	name = models.CharField(max_length=30, unique=True)
	abbreviation = models.CharField(
		max_length=5,
		validators=[
			core_validators.MinLengthValidator(2),
			validators.IsAlphaValidator
		]
	)

	def save(self,  *args, **kwargs):
		self.name = self.name.lower().capitalize()
		super(StreetType, self).save(*args, **kwargs)

	def __str__(self):
		return f'{self.name} ({self.abbreviation})'

class StreetTypeTranslation(models.Model):
	"""
	It refers to types of streets used to define an address but translated into
	another language.
	"""
	translated_to = models.ForeignKey(Language, on_delete=models.CASCADE)
	base_street_type = models.ForeignKey(
		StreetType,
		on_delete=models.CASCADE,
		related_name="translations"
	)
	name = models.CharField(max_length=30, blank=False)
	abbreviation = models.CharField(
		max_length=5,
		validators=[
			core_validators.MinLengthValidator(2),
			validators.IsAlphaValidator
		]
	)

	class Meta:
		unique_together = ('translated_to', 'base_street_type', )

	def save(self,  *args, **kwargs):
		self.name = self.name.lower().capitalize()
		super(StreetTypeTranslation, self).save(*args, **kwargs)

	def __str__(self):
		return f'{self.name} ({self.abbreviation}) | {self.translated_to.alpha2}'

class Address(models.Model):
	""" It refers to a specific address. """
	address = models.CharField(max_length=70)
	address_num = models.CharField(max_length=20)
	address_info = models.CharField(max_length=100, blank=True, null=True)
	# street_type = models.ForeignKey(StreetType, on_delete=models.CASCADE)
	city = models.CharField(max_length=70)
	postal_code = models.IntegerField(
		validators=[
			core_validators.MinValueValidator(1),
			core_validators.MaxValueValidator(99999)
		]
	)
	state = models.CharField(max_length=50)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
	long = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

class AliasedAddress(Address):
	""" It refers to a specific address identified by an alias. """
	alias = models.CharField(max_length=30)

class Place(Address):
	""" It refers to a place with a specific address. """
	name = models.CharField(max_length=70)

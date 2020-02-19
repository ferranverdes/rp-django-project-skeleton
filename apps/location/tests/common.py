import copy
from apps.location import models

def get_country_data(name):
	swticher= {
		'UNITED STATES': {
			'name': 'UNITED STATES',
			'alpha2': 'US',
			'alpha3': 'USA',
			'numeric_code': 840,
			'telephone_prefix': 1
		},
		'FRANCE': {
			'name': 'FRANCE',
			'alpha2': 'FR',
			'alpha3': 'FRA',
			'numeric_code': 250,
			'telephone_prefix': 33
		},
		'AUSTRALIA': {
			'name': 'AUSTRALIA',
			'alpha2': 'AU',
			'alpha3': 'AUS',
			'numeric_code': 360,
			'telephone_prefix': 61
		},
		'SPAIN': {
			'name': 'SPAIN',
			'alpha2': 'ES',
			'alpha3': 'ESP',
			'numeric_code': 724,
			'telephone_prefix': 34
		}
	}

	return copy.deepcopy(swticher[name])

def get_street_type_data(name):
	swticher= {
		'STREET': {
			'name': 'STREET',
			'alphabetic_code': 'ST'
		},
	}

	return copy.deepcopy(swticher[name])

def create_country(name, alpha2, alpha3, numeric_code, telephone_prefix):
	return models.Country.objects.create(
		name=name,
		alpha2=alpha2,
		alpha3=alpha3,
		numeric_code=numeric_code,
		telephone_prefix=telephone_prefix
	)

def create_steet_type(name, alphabetic_code):
	return models.StreetType.objects.create(
		name=name,
		alphabetic_code=alphabetic_code
	)

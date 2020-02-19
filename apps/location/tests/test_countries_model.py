from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from skeleton.tests import auth, errors
from apps.location import views, models, serializers
from apps.location.tests.common import get_country_data

class CountryViewTest(APITestCase):
	client = APIClient()

	def setUp(self):
		# Create an admin user to use in auth requests
		self.admin, self.admin_token, self.admin_auth_header = auth.create_superuser()

		# Define a valid country for post requests
		self.valid_post_data = get_country_data('SPAIN')

	def test_alpha2_shorter_length_than_required(self):
		"""
		This test ensures that it is NOT possible to create a new country by
		defining the 'alpha2' field with a length shorter than 2.
		"""
		min_length=2
		country_with_alpha2_shorter_length = self.valid_post_data
		country_with_alpha2_shorter_length['alpha2'] = 'E'

		response = self.client.post(
			reverse('country-list'),
			data=country_with_alpha2_shorter_length,
			**self.admin_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(response.data, {
			"alpha2": [ errors.get_shorter_length_error_message(min_length) ]
		})

	def test_alpha2_longer_length_than_required(self):
		"""
		This test ensures that it is NOT possible to create a new country by
		defining the 'alpha2' field with a length longer than 2.
		"""
		max_length=2
		country_with_alpha2_longer_length = self.valid_post_data
		country_with_alpha2_longer_length['alpha2'] = 'ESP'

		response = self.client.post(
			reverse('country-list'),
			data=country_with_alpha2_longer_length,
			**self.admin_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(response.data, {
			"alpha2": [ errors.get_longer_length_error_message(max_length) ]
		})

	def test_alpha2_is_saved_in_uppercase(self):
		"""
		This test ensures that when a new country is created the field of 'alpha2'
		is saved in uppercase.
		"""
		country_with_alpha2_in_lowercase = self.valid_post_data
		country_with_alpha2_in_lowercase['alpha2'] = 'es'

		response = self.client.post(
			reverse('country-list'),
			data=country_with_alpha2_in_lowercase,
			**self.admin_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		country = models.Country.objects.get(name=self.valid_post_data['name'])
		serializer = serializers.CountrySerializer(country)

		self.assertEqual(serializer.data['alpha2'], 'ES')

	def test_alpha2_only_allows_alpha_characters(self):
		"""
		This test ensures that when a new country is created the field of 'alpha2'
		only allows alpha characters.
		"""
		country_with_alpha2_using_numbers = self.valid_post_data
		country_with_alpha2_using_numbers['alpha2'] = '12'

		response = self.client.post(
			reverse('country-list'),
			data=country_with_alpha2_using_numbers,
			**self.admin_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(response.data, {
			"alpha2": [ errors.get_only_allowed_alpha_characters_error_message() ]
		})

	def test_alpha3_shorter_length_than_required(self):
		"""
		This test ensures that it is NOT possible to create a new country by
		defining the 'alpha3' field with a length shorter than 3.
		"""
		min_length=3
		country_with_alpha3_shorter_length = self.valid_post_data
		country_with_alpha3_shorter_length['alpha3'] = 'ES'

		response = self.client.post(
			reverse('country-list'),
			data=country_with_alpha3_shorter_length,
			**self.admin_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(response.data, {
			"alpha3": [ errors.get_shorter_length_error_message(min_length) ]
		})

	def test_alpha3_longer_length_than_required(self):
		"""
		This test ensures that it is NOT possible to create a new country by
		defining the 'alpha3' field with a length longer than 3.
		"""
		max_length=3
		country_with_alpha3_longer_length = self.valid_post_data
		country_with_alpha3_longer_length['alpha3'] = 'ESPA'

		response = self.client.post(
			reverse('country-list'),
			data=country_with_alpha3_longer_length,
			**self.admin_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(response.data, {
			"alpha3": [ errors.get_longer_length_error_message(max_length) ]
		})

	def test_alpha3_is_saved_in_uppercase(self):
		"""
		This test ensures that when a new country is created the field of 'alpha3'
		is saved in uppercase.
		"""
		country_with_alpha3_in_lowercase = self.valid_post_data
		country_with_alpha3_in_lowercase['alpha3'] = 'esp'

		response = self.client.post(
			reverse('country-list'),
			data=country_with_alpha3_in_lowercase,
			**self.admin_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		country = models.Country.objects.get(name=self.valid_post_data['name'])
		serializer = serializers.CountrySerializer(country)

		self.assertEqual(serializer.data['alpha3'], 'ESP')

	def test_alpha3_only_allows_alpha_characters(self):
		"""
		This test ensures that when a new country is created the field of 'alpha3'
		only allows alpha characters.
		"""
		country_with_alpha3_using_numbers = self.valid_post_data
		country_with_alpha3_using_numbers['alpha3'] = '123'

		response = self.client.post(
			reverse('country-list'),
			data=country_with_alpha3_using_numbers,
			**self.admin_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(response.data, {
			"alpha3": [ errors.get_only_allowed_alpha_characters_error_message() ]
		})

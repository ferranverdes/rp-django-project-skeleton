from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from skeleton.tests import auth
from apps.location import views, models, serializers
from apps.location.tests.common import get_country_data, create_country

class CountryViewTest(APITestCase):
	client = APIClient()

	def setUp(self):
		# Create a regular user to use in auth requests
		self.user, self.user_token, self.user_auth_header = auth.create_user()

		# Create an admin user to use in auth requests
		self.admin, self.admin_token, self.admin_auth_header = auth.create_superuser()

		# Define countries to create in the db
		self.first_country = get_country_data('UNITED STATES')
		self.second_country = get_country_data('FRANCE')
		self.third_country = get_country_data('AUSTRALIA')

		# Create countries
		create_country(**self.first_country)
		create_country(**self.second_country)
		create_country(**self.third_country)

		# Define a valid country for post requests
		self.valid_post_data = get_country_data('SPAIN')

	def test_get_all_countries_without_authentication(self):
		"""
		This test ensures that all countries that have been added in the setUp
		method can be retrieved when making a GET request to '/countries' endpoint
		without any authentication provided.
		"""
		expected = models.Country.objects.all()
		serializer = serializers.CountrySerializer(expected, many=True)

		response = self.client.get(
			reverse('country-list')
		)

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_all_countries_with_user_authentication(self):
		"""
		This test ensures that all countries that have been added in the setUp
		method can be retrieved when making a GET request to '/countries' endpoint
		with a regular user authentication provided.
		"""
		expected = models.Country.objects.all()
		serializer = serializers.CountrySerializer(expected, many=True)

		response = self.client.get(
			reverse('country-list'),
			**self.user_auth_header
		)

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_all_countries_with_admin_authentication(self):
		"""
		This test ensures that all countries that have been added in the setUp
		method can be retrieved when making a GET request to '/countries' endpoint
		with an admin user authentication provided.
		"""
		expected = models.Country.objects.all()
		serializer = serializers.CountrySerializer(expected, many=True)

		response = self.client.get(
			reverse('country-list'),
			**self.admin_auth_header
		)

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_post_new_country_without_authentication(self):
		"""
		This test ensures that it is NOT possible to create a new country making a
		POST request to '/countries' endpoint without any authentication provided.
		"""
		response = self.client.post(
			reverse('country-list'),
			data=self.valid_post_data
		)

		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

		country = models.Country.objects.filter(name=self.valid_post_data['name'])
		self.assertFalse(country.exists())

	def test_post_new_country_with_user_authentication(self):
		"""
		This test ensures that it is NOT possible to create a new country making a
		POST request to '/countries' endpoint with a regular user authentication
		provided.
		"""
		response = self.client.post(
			reverse('country-list'),
			data=self.valid_post_data,
			**self.user_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

		country = models.Country.objects.filter(name=self.valid_post_data['name'])
		self.assertFalse(country.exists())

	def test_post_new_country_with_admin_authentication(self):
		"""
		This test ensures that it is possible to create a new country making a
		POST request to '/countries' endpoint with an admin user authentication
		provided.
		"""
		response = self.client.post(
			reverse('country-list'),
			data=self.valid_post_data,
			**self.admin_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		country = models.Country.objects.get(name=self.valid_post_data['name'])
		serializer = serializers.CountrySerializer(country)

		self.assertTrue(self.valid_post_data.items() <= serializer.data.items())

	def test_post_an_existing_country_as_a_new_country_with_admin_authentication(self):
		"""
		This test ensures that it is NOT possible to create a new country using
		data from an existing country and making a POST request to '/countries'
		endpoint with an admin user authentication provided and it throws a BAD
		REQUEST error.
		"""
		countries_num = models.Country.objects.count()

		country_id=1
		existing_country = models.Country.objects.get(pk=country_id)
		serializer = serializers.CountrySerializer(existing_country)

		post_data = serializer.data
		post_data.pop('id', None)

		response = self.client.post(
			reverse('country-list'),
			data=post_data,
			**self.admin_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(countries_num, models.Country.objects.count())

	def test_get_single_country_without_authentication(self):
		"""
		This test ensures that countries are accessible through their id making a GET
		request to '/countries/<int:pk>' endpoint without any authentication provided.
		"""
		country_id=1
		expected = models.Country.objects.get(pk=country_id)
		serializer = serializers.CountrySerializer(expected)

		response = self.client.get(
			reverse('country-detail', args={country_id})
		)

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_single_country_with_user_authentication(self):
		"""
		This test ensures that countries are accessible through their id making a GET
		request to '/countries/<int:pk>' endpoint with a regular user authentication
		provided.
		"""
		country_id=1
		expected = models.Country.objects.get(pk=country_id)
		serializer = serializers.CountrySerializer(expected)

		response = self.client.get(
			reverse('country-detail',
			args={country_id}),
			**self.user_auth_header
		)

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_single_country_with_admin_authentication(self):
		"""
		This test ensures that countries are accessible through their id making a GET
		request to '/countries/<int:pk>' endpoint with an admin user authentication
		provided.
		"""
		country_id=1
		expected = models.Country.objects.get(pk=country_id)
		serializer = serializers.CountrySerializer(expected)

		response = self.client.get(
			reverse('country-detail',
			args={country_id}),
			**self.admin_auth_header
		)

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_update_existing_country_without_authentication(self):
		"""
		This test ensures that countries can NOT be updated through their id making a
		PUT request to '/countries/<int:pk>' endpoint without any authentication
		provided.
		"""
		country_id=2
		response = self.client.put(
			reverse('country-detail',
			args={country_id}),
			data=self.valid_post_data,
		)

		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

		country = models.Country.objects.filter(name=self.valid_post_data['name'])
		self.assertFalse(country.exists())

	def test_update_existing_country_with_user_authentication(self):
		"""
		This test ensures that countries can NOT be updated through their id making a
		PUT request to '/countries/<int:pk>' endpoint with a regular user authentication
		provided.
		"""
		country_id=2
		response = self.client.put(
			reverse('country-detail',
			args={country_id}),
			data=self.valid_post_data,
			**self.user_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

		country = models.Country.objects.filter(name=self.valid_post_data['name'])
		self.assertFalse(country.exists())

	def test_update_existing_country_with_admin_authentication(self):
		"""
		This test ensures that countries can be updated through their id making a
		PUT request to '/countries/<int:pk>' endpoint with an admin user authentication
		provided.
		"""
		country_id=2
		original = models.Country.objects.get(pk=country_id)
		original_serializer = serializers.CountrySerializer(original)

		self.assertEqual(original_serializer.data['name'], 'FRANCE')

		response = self.client.put(
			reverse('country-detail',
			args={country_id}),
			data=self.valid_post_data,
			**self.admin_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

		updated = models.Country.objects.get(pk=country_id)
		updated_serializer = serializers.CountrySerializer(updated)
		self.assertTrue(self.valid_post_data.items() <= updated_serializer.data.items())

	def test_update_non_existing_country_with_admin_authentication(self):
		"""
		This test ensures that non existing countries can NOT be updated through
		their id making a PUT request to '/countries/<int:pk>' endpoint with an
		admin user authentication provided and it throws a NOT FOUND error.
		"""
		country_id=100
		get_response = self.client.get(
			reverse('country-detail',
			args={country_id}),
			**self.admin_auth_header
		)

		self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)

		put_response = self.client.put(
			reverse('country-detail',
			args={country_id}),
			data=self.valid_post_data,
			**self.admin_auth_header
		)

		self.assertEqual(put_response.status_code, status.HTTP_404_NOT_FOUND)

	def test_delete_existing_country_without_authentication(self):
		"""
		This test ensures that countries can NOT be deleted through their id making a
		DELETE request to '/countries/<int:pk>' endpoint without any authentication
		provided.
		"""
		country_id=3
		expected = models.Country.objects.get(pk=country_id)
		expected_serializer = serializers.CountrySerializer(expected)

		response = self.client.delete(
			reverse('country-detail',
			args={country_id})
		)

		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

		country = models.Country.objects.get(pk=country_id)
		country_serializer = serializers.CountrySerializer(country)
		self.assertEqual(expected_serializer.data, country_serializer.data)

	def test_delete_existing_country_with_user_authentication(self):
		"""
		This test ensures that countries can NOT be deleted through their id making a
		DELETE request to '/countries/<int:pk>' endpoint with a regular user
		authentication provided.
		"""
		country_id=3
		expected = models.Country.objects.get(pk=country_id)
		expected_serializer = serializers.CountrySerializer(expected)

		response = self.client.delete(
			reverse('country-detail',
			args={country_id}),
			**self.user_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

		country = models.Country.objects.get(pk=country_id)
		country_serializer = serializers.CountrySerializer(country)
		self.assertEqual(expected_serializer.data, country_serializer.data)

	def test_delete_existing_country_with_admin_authentication(self):
		"""
		This test ensures that countries can be deleted through their id making a
		DELETE request to '/countries/<int:pk>' endpoint with an admin user
		authentication provided.
		"""
		country_id=3
		expected = models.Country.objects.get(pk=country_id)
		expected_serializer = serializers.CountrySerializer(expected)

		response = self.client.delete(
			reverse('country-detail',
			args={country_id}),
			**self.admin_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

		country = models.Country.objects.filter(name='FRANCE')
		self.assertTrue(country.exists())

	def test_delete_non_existing_country_with_admin_authentication(self):
		"""
		This test ensures that deleting non existing countries through their id
		making a DELETE request to '/countries/<int:pk>' endpoint with an admin user
		authentication provided throw a NOT FOUND error.
		"""
		country_id=100
		get_response = self.client.get(
			reverse('country-detail',
			args={country_id}),
			**self.admin_auth_header
		)

		self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)

		delete_response = self.client.delete(
			reverse('country-detail',
			args={country_id}),
			**self.admin_auth_header
		)

		self.assertEqual(delete_response.status_code, status.HTTP_404_NOT_FOUND)

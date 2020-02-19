from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from skeleton.tests import auth, errors
from apps.location import views, models, serializers
from apps.location.tests.common import get_street_type_data

class StreetTypeViewTest(APITestCase):
	client = APIClient()

	def setUp(self):
		# Create an admin user to use in auth requests
		self.admin, self.admin_token, self.admin_auth_header = auth.create_superuser()

		# Define a valid street type for post requests
		self.valid_post_data = get_street_type_data('STREET')

	def test_alphabetic_code_shorter_length_than_required(self):
		"""
		This test ensures that it is NOT possible to create a new street type by
		defining the 'alphabetic_code' field with a length shorter than 2.
		"""
		min_length=2
		street_type_with_alphabetic_code_shorter_length = self.valid_post_data
		street_type_with_alphabetic_code_shorter_length['alphabetic_code'] = 'S'

		response = self.client.post(
			reverse('streettype-list'),
			data=street_type_with_alphabetic_code_shorter_length,
			**self.admin_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(response.data, {
			"alphabetic_code": [ errors.get_shorter_length_error_message(min_length) ]
		})

	def test_alphabetic_code_longer_length_than_required(self):
		"""
		This test ensures that it is NOT possible to create a new street type by
		defining the 'alphabetic_code' field with a length longer than 2.
		"""
		max_length=2
		street_type_with_alphabetic_code_longer_length = self.valid_post_data
		street_type_with_alphabetic_code_longer_length['alphabetic_code'] = 'STR'

		response = self.client.post(
			reverse('streettype-list'),
			data=street_type_with_alphabetic_code_longer_length,
			**self.admin_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(response.data, {
			"alphabetic_code": [ errors.get_longer_length_error_message(max_length) ]
		})

	def test_alphabetic_code_is_saved_in_uppercase(self):
		"""
		This test ensures that when a new street type is created the field of
		'alphabetic_code' is saved in uppercase.
		"""
		street_type_with_alphabetic_code_in_lowercase = self.valid_post_data
		street_type_with_alphabetic_code_in_lowercase['alphabetic_code'] = 'ST'

		response = self.client.post(
			reverse('streettype-list'),
			data=street_type_with_alphabetic_code_in_lowercase,
			**self.admin_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		street_type = models.StreetType.objects.get(name=self.valid_post_data['name'])
		serializer = serializers.StreetTypeSerializer(street_type)

		self.assertEqual(serializer.data['alphabetic_code'], 'ST')

	def test_alphabetic_code_only_allows_alpha_characters(self):
		"""
		This test ensures that when a new street type is created the field of
		'alphabetic_code' only allows alpha characters.
		"""
		street_type_with_alphabetic_code_using_numbers = self.valid_post_data
		street_type_with_alphabetic_code_using_numbers['alphabetic_code'] = '12'

		response = self.client.post(
			reverse('streettype-list'),
			data=street_type_with_alphabetic_code_using_numbers,
			**self.admin_auth_header
		)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(response.data, {
			"alphabetic_code": [
				errors.get_only_allowed_alpha_characters_error_message()
			]
		})

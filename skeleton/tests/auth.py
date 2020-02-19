from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

def create_user(username='testuser', email='test@testemail.com', password='testpassword'):
	"""
	Creates a built-in user useful for authenticated API endpoints using Token
	Authentication.

	Returns:
		user: user created using Django auth User model.
		user_token: Authentication Token created.
		user_auth_header: HTTP_AUTHORIZATION header containing the valid
			Authentication Token generated for HTTP requests.
	"""
	user = User.objects.create_user(
		username=username,
		email=email,
		password=password
	)

	user_token = Token.objects.create(user=user)
	user_auth_header = { 'HTTP_AUTHORIZATION': f'Token {user_token}' }

	return user, user_token, user_auth_header

def create_superuser(username='testadmin', email='admin@testemail.com', password='adminpassword'):
	"""
	Creates a built-in user admin useful for authenticated API endpoints using Token
	Authentication.

	Returns:
		admin: user created using Django auth User model.
		admin_token: Authentication Token created.
		admin_auth_header: HTTP_AUTHORIZATION header containing the valid
			Authentication Token generated for HTTP requests.
	"""
	admin = User.objects.create_superuser(
		username=username,
		email=email,
		password=password
	)

	admin_token = Token.objects.create(user=admin)
	admin_auth_header = { 'HTTP_AUTHORIZATION': f'Token {admin_token}' }

	return admin, admin_token, admin_auth_header

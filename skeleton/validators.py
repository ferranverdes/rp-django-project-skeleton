from django.core.validators import RegexValidator

"""
Validator that uses regex to make sure that a string is composed only by alpha
characters.
"""
IsAlphaValidator = RegexValidator(
	r'^[a-zA-Z]*$',
	message='Ensure this field only uses alpha characters.',
	code='Invalid characters'
)

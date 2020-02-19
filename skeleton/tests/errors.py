
def get_shorter_length_error_message(min_length):
	return f'Ensure this field has at least {min_length} characters.'

def get_longer_length_error_message(max_length):
	return f'Ensure this field has no more than {max_length} characters.'

def get_only_allowed_alpha_characters_error_message():
	return 'Ensure this field only uses alpha characters.'

from django.db import models

class Contact(Address):
	pass
	# email
	# start_date
	# prefered_language = models.ForeignKey(Language, on_delete=models.CASCADE)
	# telephone

class Person(Contact):
	pass

class Company(Contact):
	pass

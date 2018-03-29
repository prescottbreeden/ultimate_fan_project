from django.db import models
from django.conf import settings
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User_Manager(models.Manager):

	##### REGISTRATION VALIDATION #####
	def validate_registration(self, postData):
		print('validation started')
		result = {
			'status' : False,
			'errors' : {}
		}

		# name field validation
		if postData['first_name'] == '':
			result['errors']['first_name'] = 'First name cannot be blank'
		if postData['last_name'] == '':
			result['errors']['last_name'] = 'Last name cannot be blank'
		if postData['alias'] == '':
			result['errors']['alias'] = 'Alias cannot be blank'

		# email field validation
		if postData['email'] == '':
			result['errors']['email'] = 'Email cannot be blank'
		if not EMAIL_REGEX.match(postData['email']):
			result['errors']['email'] = 'Invalid Email Address'
		existing = User.objects.filter(email = postData['email'])
		if existing:
			result['errors']['email'] = 'Email already registered, please log in instead.'

		# password field validation
		if postData['password'] != postData['cpassword']:
			result['errors']['password'] = 'Passwords do not match'
		if len(postData['password']) <8:
			result['errors']['password'] = 'Passwords must be at least 8 characters long.' 

		if len(result['errors']):
			return result
		else:
		# create new user
			user_password = postData['password'] 
			hashed = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt())
			new_user = User.objects.create(
				first_name = postData['first_name'],
				last_name = postData['last_name'],
				alias = postData['alias'],
				email = postData['email'],
				password = hashed,
				)
			result['status'] = True
			result['user_id'] = new_user.id
			return result

	##### LOGIN VALIDATION #####
	def validate_login(self, postData):
		result = {
			'status' : False,
			'errors' : {}
		}

		# email validation
		existing = User.objects.filter(email = postData['email'])
		if existing:
			user_password = postData['password'].encode()
			# this is magic....
			existing_password = existing[0].password[2: len(existing[0].password) - 1]
			existing_password = existing_password.encode()
			if not bcrypt.checkpw(user_password, existing_password):
				result['errors']['password'] = 'Password doesn\'t match'
		else:
			result['errors']['password'] = 'Email not found'

		if len(result['errors']):
			return result
		else:
			result['status'] = True
			result['user_id'] = existing[0].id
			return result

# define super_user
class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = User_Manager()





#

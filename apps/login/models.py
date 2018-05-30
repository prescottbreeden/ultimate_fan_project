from django.db import models
from django.conf import settings
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User_Manager(models.Manager):

	# REGISTRATION VALIDATION
	def validate_registration(self, postData):
		print('validation started')
		result = {
			'status' : False,
			'errors' : {}
		}

		# name field validation
		if postData['alias'] == '':
			result['errors']['alias'] = 'Alias cannot be blank'
		existing = User.objects.filter(alias = postData['alias'])
		if existing:
			result['errors']['alias'] = 'Alias already registered'

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
		if len(postData['password']) < 6 or len(postData['password']) > 12:
			result['errors']['password'] = 'Passwords must be between 6 and 12 characters.' 

		if len(result['errors']):
			return result
		else:

		# create new user
			user_password = postData['password'] 
			hashed = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt())
			new_user = User.objects.create(
				first_name = '',
				last_name = '',
				alias = postData['alias'],
				email = postData['email'],
				password = hashed,
				)
			result['status'] = True
			result['user_id'] = new_user.id
			return result

	# LOGIN VALIDATION
	def validate_login(self, postData):
		result = {
			'status' : False,
			'errors' : {}
		}

		# email validation
		existing = User.objects.filter(email = postData['email'])
		if not existing:
			existing = User.objects.filter(alias = postData['email'])
		if existing:
			user_password = postData['password'].encode()
			# as of 2018 bcrypt with python 3 in django causes hashes to be saved in DB as: b'hash'
			# below code is to slice off the b and the quotes before encoding it for verification
			existing_password = existing[0].password[2: len(existing[0].password) - 1]
			existing_password = existing_password.encode()
			if not bcrypt.checkpw(user_password, existing_password):
				result['errors']['password'] = 'Incorrect Password'
		else:
			result['errors']['password'] = 'Alias or Email Not Found'

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

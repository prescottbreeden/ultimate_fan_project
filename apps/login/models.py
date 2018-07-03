from django.db import models
from django.conf import settings
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User_Manager(models.Manager):

    # REGISTRATION VALIDATION
    def validate_registration(self, postData):
        print('validation started')
        result = {
            'status': False,
            'errors': {}
        }

        # name field validation
        if postData['alias'] == '':
            result['errors']['alias'] = 'Alias cannot be blank'
        exists = User.objects.filter(alias=postData['alias'])
        if exists:
            result['errors']['alias'] = 'Alias already registered'

        # email field validation
        if postData['email'] == '':
            msg = 'Email cannot be blank'
            result['errors']['email'] = msg
        if not EMAIL_REGEX.match(postData['email']):
            msg = 'Invalid Email Address'
            result['errors']['email'] = msg
            exists = User.objects.filter(email=postData['email'])
        if exists:
            msg = 'Email already registered, please log in instead.'
            result['errors']['email'] = msg

        # password field validation
        if postData['password'] != postData['cpassword']:
            msg = 'Passwords do not match'
            result['errors']['password'] = msg
        if len(postData['password']) < 6 or len(postData['password']) > 12:
            msg = 'Passwords must be between 6 and 12 characters.'
            result['errors']['password'] = msg

        if len(result['errors']):
            return result

        else:

            # create new user
            user_password = postData['password']
            hashed = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt())
            new_user = User.objects.create(
                first_name='',
                last_name='',
                alias=postData['alias'],
                email=postData['email'],
                password=hashed,
            )
            result['status'] = True
            result['user_id'] = new_user.id

        return result

    # LOGIN VALIDATION
    def validate_login(self, postData):
        result = {
            'status': False,
            'errors': {}
        }

        # email validation
        exists = User.objects.filter(email=postData['email'])
        if not exists:
            exists = User.objects.filter(alias=postData['email'])
        if exists:
            user_password = postData['password'].encode()
            '''
            Bcrypt with python3 in django causes hashes to be saved in DB as:
                b'hash' which does not register as a binary marker but rather
                the letter 'b' with quotes around the following word,
                preventing authentication.

            below code is to slice off the b and the quotes before encoding
            it for verification
            '''
            curr_pwd = exists[0].password[2: len(exists[0].password)-1]
            curr_pwd = curr_pwd.encode()
            if not bcrypt.checkpw(user_password, curr_pwd):
                result['errors']['password'] = 'Incorrect Password'
        else:
            result['errors']['password'] = 'Alias or Email Not Found'

        if len(result['errors']):
            return result
        else:
            result['status'] = True
            result['user_id'] = exists[0].id

        return result

# USER SCHEMA
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = User_Manager()

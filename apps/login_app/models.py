from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
  # whatever


# Create your models here.
class UserManager(models.Manager):
    def validateRegistration(self,postData):
        result = {}
        errors = []
        if len(postData['first_name']) < 1:
            errors.append('please enter a first name')
        if len(postData['last_name']) < 1:
            errors.append('please enter a last name')
        if len(postData['email']) < 1:
            errors.append('please enter an email')
        if len(postData['password']) < 1:
            errors.append('please enter a password')
        if not EMAIL_REGEX.match(postData['email']):
            errors.append('please enter a valid email address')
        if postData['password'] != postData['confirm']:
            errors.append('password don"t match')
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors.append('email already exists')

        if len(errors) > 0:
            result['errors'] = errors
        else:
            result['user_id'] = User.objects.create(
                first_name=postData['first_name'],
                last_name=postData['last_name'],
                email=postData['email'],
                password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            ).id
            
        return result


class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

    def __repr__(self):
        return f"[User Object for {self.first_name}]"
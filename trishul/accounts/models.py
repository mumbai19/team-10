# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.template.loader import get_template
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    email =models.EmailField()
    mobile_number  = PhoneNumberField(default='9999999999')
    first_name     = models.CharField(max_length=255, default='John')
    last_name      = models.CharField(max_length=255, default='Miller')
    

    def __str__(self):
    	return self.email

class User(AbstractBaseUser):
	email          = models.EmailField(max_length=255, unique=True, default='abc123@gmail.com')

	USERNAME_FIELD = 'email'

	REQUIRED_FIELD = ['email']

	

	def __str__(self):
		return self.email
	
	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True








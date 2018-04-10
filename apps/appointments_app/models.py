from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime
from django.utils import timezone
import re
import bcrypt

Name_Regex = re.compile(r'^[A-Za-z ]+$')
NumR = 100
pr = 0

# Create your models here.
class userManager(models.Manager):
    def validate (self, postData):
        errors = []
        global NumR
        NumR = NumR - int(str(postData['nr']))
        if len(postData['name']) < 2:
            errors.append("Name needs to be more than 1 letter")
        if not Name_Regex.match(postData['name']):
            errors.append("name can only be letters")
        if len(User.objects.filter(email = postData['email'])) > 0:
            errors.append("email already exists")
        if len(postData["email"])==0:
            errors.append("Please insert an email address in the bracket")
        elif not re.search(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$', postData["email"]):
            errors.append("Please insert a valid email address")
        if str(postData['dd']) == str(postData['ad']):
            errors.append("Please input a different date")
        if (NumR - int(postData['nr'])) < 0 :
            errors.append("There are not enough rooms to book")
            errors.append(NumR)
        if str(postData['dd']) < str(postData['ad']):
            errors.append("Please input a different departure date")
        if len(errors) == 0:
            newuser = User.objects.create(name= postData['name'], email= postData['email'], ad= postData['ad'],dd= postData['dd'])
            print (NumR,pr)
            return (True, newuser)
        else:
            return (False, errors)
class User(models.Model):
    name = models.CharField(max_length=45)
    email= models.CharField(max_length=45, blank=True, null=True)
    ad= models.DateField(blank=True, null=True)
    dd= models.DateField(blank=True, null=True)
    nr= models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()

class appointManager(models.Manager):
    def finish(self, postData):
        global NumR
        NumR = int(postData['nrr'])
        makeappoint= Appointment.objects.create(pr= str(postData['pr']),nrr= str(postData['nrr']))
        NumR = NumR * int(str(postData['pr'])) /100 + NumR
        NumR = int(NumR)
        print (NumR)
        #print (pr)
        #print (res)
        #print (str(postData['nrr']))
        #print (str(postData['pr']))
        return (True)

class Appointment(models.Model):

    pr = models.CharField(max_length=100,null=True)
    nrr = models.CharField(max_length = 100,null=True)
    objects= appointManager()

from django.db import models




class Users(models.Model):
     GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
     PROFILE_CHOICES = (
       ('M', 'myself'),
       ('b', 'brother'),
       ('S','Son'),
       ('SS','Sister'),
       ('F','Friend'),
       ('R','Relative')
   )
     firstName   = models.CharField(max_length= 250)
     lastName    = models.CharField(max_length=250)
     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
     email       = models.EmailField(unique=True)
     password    = models.CharField(max_length=250)
     phone       = models.CharField(max_length=250)
     created_at  = models.DateField(auto_now_add=True)
     updated_at  = models.DateField(null=True)
     status =  models.BooleanField(default=False)
     profile_for = models.CharField(max_length=12, choices=PROFILE_CHOICES)


class Contact(models.Model):
    contact_name =  models.CharField(max_length= 250)
    contact_number = models.CharField(max_length=250)
    created_at  = models.DateField(auto_now_add=True)
    updated_at  = models.DateField(null=True)

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

labourtype = (('FL', 'Farm Labour'), ('TL', 'Transportation Labour'), ('SF', 'Scientific Farming'))

class RegisterLabour(models.Model):
    name = models.CharField(max_length=100)
    labourType = models.CharField(max_length=100, choices=labourtype)
    dateOfBirth= models.CharField(max_length=100)
    address = models.TextField()
    adharCard = models.FileField(upload_to='AdharCard')
    bankName = models.CharField(max_length=100)
    AccountNo = models.IntegerField()
    IFSC = models.IntegerField()
    def __str__(self):
        return self.name

class RequestLabour(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    quantity = models.IntegerField( default='')
    work_type = models.CharField(max_length=100)
    date = models.DateField()
    confirm_Request = models.BooleanField(null=True, blank=True, default=False)
    called_farmers = models.BooleanField(null=True, blank=True, default=False)
    def __str__(self):
        return self.name

class RegisterComplaint(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, blank=True, default='')
    description = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    query  = models.TextField()

    def __str__(self):
        return self.name
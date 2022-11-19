from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

labourtype = (('FL', 'Farm Labour'), ('TL', 'Transportation Labour'), ('SF', 'Scientific Farming'))

class RegisterLabour(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, blank=True, default='')
    labourType = models.CharField(max_length=50, choices=labourtype)
    ok = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name

class RequestLabour(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, blank=True, default='')
    quantity = models.IntegerField( default='')
    work_type = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name

class RegisterComplaint(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, blank=True, default='')
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email  = models.TextField()

    def __str__(self):
        return self.name
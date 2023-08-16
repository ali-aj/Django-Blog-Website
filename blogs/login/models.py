from django.db import models

# Create your models here.
class otpClass(models.Model):
    otp = models.CharField(max_length=6)
    email = models.EmailField()
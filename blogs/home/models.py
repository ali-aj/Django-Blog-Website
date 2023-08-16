from django.db import models

# Create your models here.
class blogData(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=10000, default='')
    image1 = models.ImageField(upload_to='images/', default='')
    image2 = models.ImageField(upload_to='images/', blank=True)
    image3 = models.ImageField(upload_to='images/', blank=True)
    owner_username = models.CharField(max_length=100, default='')
    time_created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class contactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name
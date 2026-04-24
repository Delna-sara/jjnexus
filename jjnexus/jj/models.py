from django.db import models

class Contact(models.Model):
    # objects = None
    # objects = None
    objects = None
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.

from django.db import models

class College(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='Colleges/')
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

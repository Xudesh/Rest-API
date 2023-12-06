from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    name = models.CharField(max_length=150, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=500, null=True)
    slug = models.CharField(max_length=150)
    image = models.ImageField(upload_to='pet-img/', null=True)
    phone_number = models.IntegerField(max_length=9, null=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    video = models.FileField(max_length=350, upload_to='pet-videos/', null=True, blank=True)
    public_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return  self.name
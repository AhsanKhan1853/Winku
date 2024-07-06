from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)  # Foreign key to user model
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=600)
    image = models.ImageField(default='default.jpg',upload_to='posts_pics')
    date_posted = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return self.title
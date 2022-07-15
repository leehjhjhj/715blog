from django.db import models
from django.forms import CharField
from account.models import CustomUser
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Blog(models.Model):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=10)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)

    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    writer = models.CharField(max_length=20, null=True)
    date = models.DateTimeField(default=timezone.now)

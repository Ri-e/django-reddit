from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    topic = models.CharField(max_length=200)
    def __str__(self):
        return self.topic

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    heading = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    class Meta:
        ordering = ['-updated', '-created']
    def __str__(self):
        return self.heading[0:25] + "..."

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message[0:25] + "..."
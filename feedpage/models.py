from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tag.models import Tag

# Create your models here.
class Feed(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, null=True, on_delete= models.CASCADE) 
    like_users = models.ManyToManyField(User, blank=True, related_name='like_feeds', through='Like')
    tags = models.ManyToManyField(Tag, blank=True, related_name='feeds')
    
    def update_date(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    content = models.TextField()
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, on_delete= models.CASCADE) 

    def __str__(self):
        return str(self.id)
    
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
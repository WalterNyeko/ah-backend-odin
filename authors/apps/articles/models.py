from django.db import models
from ..authentication.models import User
from datetime import datetime, timedelta

from taggit.managers import TaggableManager


# Create your models here.

class Article(models.Model):


    title = models.CharField(db_index= True, max_length = 255)
    description = models.CharField(db_index=True, max_length = 255)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    published = models.BooleanField()
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tagList = TaggableManager(blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.TextField(null=True, blank=True)
    read_time = models.TextField(max_length = 200, default="Unknown")

    @property
    def likescount(self):
        return ArticleLikes.objects.filter(article_like=True).count()

    @property
    def dislikescount(self):
        return ArticleLikes.objects.filter(article_like=False).count()

    objects = models.Manager()

class BookmarkingArticles(models.Model):
 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    bookmarked_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class ArticleLikes(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name='article_likes')
    article_like = models.BooleanField(db_index=True, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article_liked_at = models.DateTimeField(auto_now_add=True)
    article_disliked_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
class Rating(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    article_rate = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)



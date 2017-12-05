from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from lock_tokens.models import LockableModel
# Create your models here.


class Category(LockableModel):
    name = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

    def __str__(self):
        return self.name


class Article(LockableModel):

    title = models.CharField(max_length=100)
    body = HTMLField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    featured_img = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)


    def __str__(self):
        return self.title
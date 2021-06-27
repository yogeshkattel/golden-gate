from django.db import models
from django.db.models.base import Model
from django.utils.text import slugify
from django.db.models.signals import pre_save
import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    Title = models.CharField(max_length=200)
    SubTitle = models.CharField(max_length=100)
    Description = RichTextField()
    DateTime = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)

class Comments(models.Model):
    Author = models.CharField(max_length=50, default="Anonimous")
    Content = models.TextField()
    DateTime = models.DateTimeField(auto_now_add=True)
    Blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    Parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,blank=True)

    @property
    def child(self):
        return Comments.objects.filter(Parent=self).order_by('DateTime').all()
    @property
    def is_parent(self):
        if self.Parent is None:
            return True
        return False
    


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug =  instance.Title + str(datetime.datetime.now())
        instance.slug = slugify(slug)

pre_save.connect(slug_generator, sender = Blog)


class FeedBack(models.Model):
    Email = models.EmailField()
    Subject = models.CharField(max_length=200)
    Message = models.TextField()

class ViewersProblem(models.Model):
    FullName = models.CharField(max_length=100, default="Anonymous")
    Email = models.EmailField()
    Phone = models.IntegerField(null=True, blank=True)
    Problem = models.CharField(max_length=200)
    Description = models.TextField()

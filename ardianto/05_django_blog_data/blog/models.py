from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

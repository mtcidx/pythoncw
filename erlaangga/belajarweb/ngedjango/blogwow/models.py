from django.db import models

# Create your models here.
class BlogCategory(models.Model):

	title = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def __repr__(self):
		return self.title

class BlogPost(models.Model):

	category_id = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def __repr__(self):
		return self.title

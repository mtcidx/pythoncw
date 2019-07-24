from rest_framework import serializers
from .models import BlogCategory

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = BlogCategory
		fields = '__all__'
		

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer
from .models import BlogCategory

# Create your views here.
@api_view(['GET'])
def hello_wong(request):
	return Response('Hello Wong!')

@api_view(['GET'])
def get_category(request):
	categQuerset = BlogCategory.objects.all()
	serializedCateg = CategorySerializer(categQuerset, many=True)
	return Response(serializedCateg.data)


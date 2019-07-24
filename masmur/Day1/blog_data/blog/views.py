# from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer
from rest_framework.schemas.openapi import AutoSchema


@api_view(['GET'])
def hello_world(request):
    return Response('Hello World!')


@api_view(['GET'])
def get_categories(request):
    queryset = Category.objects.all()
    serialized = CategorySerializer(queryset, many=True)
    return Response(serialized.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


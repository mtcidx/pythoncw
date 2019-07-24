# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer

@api_view(['GET'])
def hello_world(request):
    # import ipdb;ipdb.set_trace()
    return Response('Hello World')


@api_view(['GET'])
def get_categories(request):
    # http://127.0.0.1:8000/api/v1/get_categories/
    queryset = Category.objects.all()
    serialized = CategorySerializer(queryset, many=True)
    return Response(serialized.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
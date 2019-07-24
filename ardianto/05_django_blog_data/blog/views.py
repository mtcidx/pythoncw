# Create your views here.
from blog.models import Category, Post
from blog.serializers import CategorySerializer, PostSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def hellow_world(request):
    return Response('Hellow World!')


# GET

@api_view(['GET'])
def get_categories(request):
    queryset = Category.objects.all()
    serialiazed = CategorySerializer(queryset, many=True)
    return Response(serialiazed.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@api_view(['GET'])
def get_post(request):
    queryset = Category.objects.all()
    serialiazed = CategorySerializer(queryset, many=True)
    return Response(serialiazed.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

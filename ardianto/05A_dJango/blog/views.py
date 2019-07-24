from blog.serializers import CategorySerializer, PostSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, Post


# Create your views here.

@api_view(['GET'])
def hello_world(request):
    return Response('Hellooooo World')


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

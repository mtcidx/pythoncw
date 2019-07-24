from rest_framework import routers
from .views import CategoryViewSet, PostViewSet
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url, include
schema_view = get_swagger_view(title='Blog API Views')

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('posts', PostViewSet)

urlpatterns = [
    url('docs/', schema_view)
]
urlpatterns += router.urls
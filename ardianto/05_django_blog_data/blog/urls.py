from blog.views import CategoryViewSet, PostViewSet
from django.conf.urls import url
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Blog API View')
router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('post', PostViewSet)

# urlpatterns = router.urls

urlpatterns = [
    url('docs/', schema_view)
]

urlpatterns += router.urls

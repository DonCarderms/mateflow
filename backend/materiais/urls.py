from rest_framework import routers
from django.urls import include, path

from .views import UserV1, MateriaisV1, CommentsV1


router = routers.SimpleRouter()
router.register(r'user', UserV1, basename='user')
router.register(r'material', MateriaisV1, basename='material')
router.register(r'comment', CommentsV1, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]

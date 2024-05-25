from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

API_VER: str = 'v1'

router = routers.DefaultRouter()
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet)
router.register('posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)


urlpatterns = [
    path(f'{API_VER}/', include(router.urls)),
    path(f'{API_VER}/auth/', include('djoser.urls')),
    path(f'{API_VER}/auth/', include('djoser.urls.jwt')),
]

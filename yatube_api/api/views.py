from django.shortcuts import get_object_or_404

from rest_framework import filters, mixins, pagination, permissions, viewsets

from .permissions import AuthorPermission
from posts.models import Comment, Follow, Group, Post
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for post's comments."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AuthorPermission, )

    def __get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        post=CommentViewSet.__get_post(self))

    def get_queryset(self):
        return CommentViewSet.__get_post(self).comments.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for displaying groups."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """ViewSet for displaying followings."""
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet for posts."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorPermission, )
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

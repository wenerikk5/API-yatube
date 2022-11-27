from django.shortcuts import get_object_or_404

from posts.models import Post, Group, Comment
from api.serializers import PostSerializer, GroupSerializer, CommentSerializer

from rest_framework import status, viewsets, mixins
from rest_framework.permissions import BasePermission, IsAuthenticated

from django.contrib.auth import get_user_model

User = get_user_model()


class IsAuthorOrReadOnly(BasePermission):
    message = 'You have no rights to modify this!'

    def has_object_permission(self, request, view, obj):
        if request.method in ('PUT', 'PATCH', 'DELETE'):
            return request.user == obj.author
        return True


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticated,
        IsAuthorOrReadOnly
    ]

    def perform_create(self, serializer):
        # post_id = self.kwargs.get('id')
        # get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user)


class ListRetrieveViewSet(
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                viewsets.GenericViewSet
            ):
    pass


class ApiGroupList(ListRetrieveViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticated,
        IsAuthorOrReadOnly
    ]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)
        return post.comments.all()

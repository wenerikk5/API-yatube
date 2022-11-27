from django.urls import path, include

from api.views import ApiGroupList, PostViewSet, CommentViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('posts', PostViewSet, basename='post')
router.register('groups', ApiGroupList, basename='group')
router.register(
    r'posts/(?P<post_id>[\d]+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    # path('posts/<int:post_id>/comments/', comment_list),
    # path('posts/<int:post_id>/comments/<int:comment_id>/', comment_detail),
    path('', include(router.urls)),
]

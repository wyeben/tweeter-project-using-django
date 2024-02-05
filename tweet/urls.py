from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('tweets', views.TweetViewSet, basename='tweets')
comment_router = routers.NestedDefaultRouter(router, 'tweets', lookup='tweet')
comment_router.register('comments', views.CommentViewSet, basename='tweet-comments')

urlpatterns = router.urls + comment_router.urls
#     [
#     path('', include(router.urls)),
#     path('', include(comment_router.urls))
# ]

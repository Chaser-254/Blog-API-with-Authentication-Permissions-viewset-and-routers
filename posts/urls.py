from django.urls import path
from .views import PostList, PostDetail,UserDetail,UserList,UserViewSet,PostViewSet
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('<int:pk>/',PostDetail.as_view()),
    path('',PostList.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('',PostViewSet,basename='posts')

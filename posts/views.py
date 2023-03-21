from django.shortcuts import render
from .models import Post
from .serializers import PostSerializers, UserSerializer
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework import generics
from .permissions import IsAuthororReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDetail(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthororReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    
class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthororReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
from django.shortcuts import render
from api.serializers import PostSerializer
from posts.models import Post
from rest_framework.views import APIView, Response
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    permission_classes =[IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class =PostSerializer


# class PostListAPIView(generics.ListCreateAPIView):
#     permission_classes [IsAuthenticatedOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer



# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthorOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer



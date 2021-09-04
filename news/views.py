from django.contrib.auth.models import AnonymousUser, User
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Article, Author
from .serializers import (ArticleSerializer,
                          ArticleLoggedSerializer,
                          ArticleAnonSerializer,
                          AuthorSerializer,
                          UserSerializer,)


class ArticleAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser):
            return ArticleAnonSerializer
        return ArticleLoggedSerializer


class ArticleListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Article.objects.all()
    serializer_class = ArticleLoggedSerializer


class ArticleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Article.objects.all()
    serializer_class = ArticleLoggedSerializer


class AuthorListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)

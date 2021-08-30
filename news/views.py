from django.contrib.auth.models import AnonymousUser
from rest_framework import generics, permissions

from .models import Article, Author
from .serializers import ArticleSerializer, ArticleLoggedSerializer, ArticleAnonSerializer, AuthorSerializer


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

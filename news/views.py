from django.contrib.auth.models import AnonymousUser
from rest_framework import generics

from .models import Article
from .serializers import ArticleSerializer, ArticleLoggedSerializer, ArticleAnonSerializer


class ArticleAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class AticleDetailAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser):
            return ArticleAnonSerializer
        return ArticleLoggedSerializer

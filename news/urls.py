from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import AuthorViewSet, ArticleViewSet

router = SimpleRouter()
router.register('articles', ArticleViewSet)
router.register('authors', AuthorViewSet)

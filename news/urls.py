from django.urls import path
from .views import ArticleAPIView, AticleDetailAPIView

urlpatterns = [
    path('articles/', ArticleAPIView.as_view(), name='articles'),
    path('articles/<int:pk>/', AticleDetailAPIView.as_view(), name='article_detail')
]

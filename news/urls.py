from django.urls import path
from rest_framework.authtoken import views
from .views import (ArticleAPIView,
                    ArticleDetailAPIView,
                    ArticleListCreateAPIView,
                    ArticleRetrieveUpdateDestroyAPIView,
                    AuthorListCreateAPIView,
                    AuthorRetrieveUpdateDestroyAPIView,
                    UserRegisterAPIView,)

urlpatterns = [
    path('articles/', ArticleAPIView.as_view(), name='articles'),
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='article_detail'),
    path('admin/articles/', ArticleListCreateAPIView.as_view(), name='articles_admin'),
    path('admin/articles/<int:pk>/', ArticleRetrieveUpdateDestroyAPIView.as_view(), name='article_admin'),
    path('admin/authors/', AuthorListCreateAPIView.as_view(), name='authors_admin'),
    path('admin/authors/<int:pk>', AuthorRetrieveUpdateDestroyAPIView.as_view(), name='author_admin'),
    path('sign-up/', UserRegisterAPIView.as_view(), name='sign-up'),
    path('login/', views.obtain_auth_token, name='login')
]

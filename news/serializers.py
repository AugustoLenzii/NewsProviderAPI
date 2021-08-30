from rest_framework import serializers
from .models import Author, Article


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = (
            'id',
            'name',
            'picture',
        )


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'author',
            'category',
            'title',
            'summary',
        )


class ArticleLoggedSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'author',
            'category',
            'title',
            'summary',
            'firstparagraph',
            'body',
        )


class ArticleAnonSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'author',
            'category',
            'title',
            'summary',
            'firstparagraph',
        )

from rest_framework import serializers
from django.contrib.auth.models import User

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
    author = AuthorSerializer()

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
    author = AuthorSerializer()

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
    author = AuthorSerializer()

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


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "password")

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

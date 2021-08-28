from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(height_field=None, width_field=None)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    summary = models.TextField(default='')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title



from django.db import models


class Author(models.Model):
    pass


class AuthorBook(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    book = models.ForeignKey('core.Book', on_delete=models.DO_NOTHING)
    is_primary = models.BooleanField(default=False)


class Book(models.Model):
    authors = models.ManyToManyField(Author, through=AuthorBook)

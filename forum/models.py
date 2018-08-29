from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    # Use ForeignKey to create relationship between models. related_name refers to the term that the foreign key will use to access the list of objects that it is a foreign key of.

    # See Board will use 'board.topics' to access list of topics that are in in the board
    board = models.ForeignKey(
        Board, related_name='topics', on_delete=models.CASCADE)
    creater = models.ForeignKey(
        User, related_name='topics', on_delete=models.CASCADE)


class Post(models.Model):
    message = models.CharField(max_length=4000)
    topic = models.ForeignKey(
        Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)
    # related_name = '+' instructs Django we don't need this reverse relationship, so it will ignore it
    updated_by = models.ForeignKey(
        User, null=True, related_name='+', on_delete=models.DO_NOTHING)

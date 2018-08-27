import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    """docstring for Questions"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


"""
Each model is represented by a class that subclasses django.db.model.Models. Each model has a number of class variables, each of which represents a database field in the model.

Each field is represented by an instance of the Field class. (take note of required arguements for certain Field classes)
eg CharField, DateTimeField

Relationship can be defined using ForeignKey. Django suppors all common db relationships ie 1-1, many-1, 1-many, many-many


The small bit of code gives Django information to:
- create db schema (CREATE TABLE .....) for this app.
- Create a PYthon db-access API for accessing Question and Choice objects.

To create models in db, run

    - python manage.py makemigrations <APP_NAME>
        --> this tells Django some changes to the models have been made and that these changes should be stored as a migration.
        TAKE NOTE. The Models HAVE NOT BEEN created yet!
    - python manage.py migrate
        --> This creates the models in the dg!
        --> migrate command takes all the migrations that haven't been applied, and runs them against the db. (syncs changes made to the models with the schema in the db.)

eg if sqlite db is used, to see sql commands, run:
    - python manage.py sqlmigrate polls 0001
    - sqlmigrate command doesn't actually run migration on the db, it just prints to screen the sql commands that Django thinks is required. Useful for checking what Django wants to do.
To check for any problems in project without making migrations or touching db, run:
    - python manage.py check

To handle changes in the models, 3 steps to take:
1) change models in models.py,
2) Run python manage.py makemigrations to create migrations for those changes
3) Run python manage.py migrate to apply those changes to the db
"""

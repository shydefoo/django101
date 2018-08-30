from django.urls import path
from . import views
app_name = 'polls'
# This is to name space the url names. There might be many apps, so the url names need to be differentiated. Eg, polls app has a detail view, Forum app miight have one as well. The app_name here will set the application namespace. Point to the correct name space using eg 'polls:detail'.
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
"""

   To abastract html code from views, use templates.
   The project's TEMPLATES setting describes how Django will load and render templates. The default settings file configures a DjangoTemplates backend whos APP_DIRS option is set to True. By convention, DjangoTemplates looks for a "templates" subdir in each of the INSTALLED_APPS --> Thats why, you create a dir called 'templates'

   Within the templates directory, create another directory called polls, and inside that dir create the index.html. so...template should be at polls/templates/polls/index.html.

   Because of how the app_directories template loader works, this template can be referred within Django simply as polls/index.html.

"""

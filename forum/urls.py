from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'forum'
urlpatterns = [
    # path('', views.home, name='home')
    url(r'^$', views.home, name='home'),

    # (?P<pk>) tells Django to capture the value into a keyword argument named pk --> which means we gotta use the keyword argument pk in our view board_topics
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
]



from django.test import TestCase
from django.urls import reverse, resolve
from .views import home, board_topics
from .models import Board
# Create your tests here.

# This is how you write testcases!!


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('forum:home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    # def test_home_url_resolves_home_view(self):
    #     view = resolve('/')
    #     self.assertEquals(view.func, home)

class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description = 'Django Board')

    def test_board_topics_view_success_status_code(self):
        url = reverse('forum:board_topics', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('forum:board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/forum/boards/1/') # need to give the FULL path after the url!
        self.assertEquals(view.func, board_topics)

from django.test import TestCase
from django.urls import reverse, resolve
from . import views
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

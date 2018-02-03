from django.urls import resolve, reverse
from django.test import TestCase
from django.core.files import File

from ..views import home, info
from ..models import Document

import os

class HomeTests(TestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)


class InfoTests(TestCase):
    def setUp(self):
        django_file = File(open('myai/tests/dataset.xlsx', 'rb'))
        self.doc = Document.objects.create(name='DjangoData')
        self.doc.user_file.save("test.csv", django_file, save=True)

    def test_info_view_success_status_code(self):
        url = reverse('info')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    def test_info_view_contains_navigation_links(self):
        info_url = reverse('info')
        homepage_url = reverse('home')
        response = self.client.get(info_url)
        self.assertContains(response, f'href="{homepage_url}"')

    def tearDown(self):
        os.remove(self.doc.user_file.path)

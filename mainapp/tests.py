from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Casting


class MainappTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.casting = Casting.objects.create(
            title='A good title',
            description='Nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        casting = Casting(title='A sample title')
        self.assertEqual(str(casting), casting.title)

    def test_casting_content(self):
        self.assertEqual(f'{self.casting.title}', 'A good title')
        self.assertEqual(f'{self.casting.author}', 'testuser')
        self.assertEqual(f'{self.casting.body}', 'Nice body content')

    def test_casting_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_casting_detail_view(self):
        response = self.client.get('/casting/1/')
        no_response = self.client.get('/casting/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'casting_detail.html')
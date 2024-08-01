from django.test import TestCase
from django.db import connection, reset_queries
from django.shortcuts import reverse

from adverts.models import Advert, City, Category


class AdvertViewTest(TestCase):
    def setUp(self):
        city = City.objects.create(name='test-city')
        category = Category.objects.create(name='test-cat')
        self.advert = Advert.objects.create(title='test', description='test', city=city, category=category)

    def test_advert_list(self):
        response = self.client.get(reverse('advert-list'))
        self.assertEqual(response.status_code, 200)

    def test_advert_queries(self):
        old_views = self.advert.views
        reset_queries()
        response = self.client.get(reverse('advert-detail', kwargs={'pk': self.advert.pk}))

        # Check the number of queries executed
        num_queries = len(connection.queries)

        self.assertEqual(response.status_code, 200)
        self.assertLessEqual(num_queries, 2)

        new_views = Advert.objects.get(id=self.advert.id).views
        self.assertEqual(new_views, old_views + 1)

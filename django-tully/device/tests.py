from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status

from device.models import Data
from collections import OrderedDict


class CheckDataTest(APITestCase):

    def test_get_data(self):
        data = Data.objects.create(speed=100, acceleration=5)
        request = self.client.get('/data/%d/' % (data.id,))
        self.assertEqual(dict(OrderedDict(request.data)), {'id': data.pk, 'speed': 100, 'acceleration': 5})

    # def test_post_data_without_authentication(self):
    #    response = self.client.post('/data/', data = {'speed':100, 'acceleration':5}, format='json')
    #    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_data(self):
        #get_user_model().objects.create_user(username='trip', password='trip')
        #self.client.login(username='trip', password='trip')
        response = self.client.post('/data/', data={'speed': 100, 'acceleration': 5}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Data.objects.count(), 1)
        self.assertEqual(Data.objects.first().speed, 100)
        self.assertEqual(Data.objects.first().acceleration, 5)


class TestViews(TestCase):

    def test_data_view(self):
        response = self.client.get(reverse('datas_list'))
        self.assertEqual(response.status_code, 200)

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
import json

# initialize the APIClient app
client = Client()

class AccountsTest(TestCase):
    """ Test module for GET all bugs API """
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="user01", email="user01@user01.com", password="user01")
        self.user = User.objects.create_user(username="user02", email="user02@user02.com", password="user02")
        self.valid_payload_login = {
            'username': 'user01',
            'password': 'user01'
        }
        self.invalid_payload_login = {
            'username': 'user01',
            'password': 'user02'
        }
        self.valid_payload_update_profile = {
            'new_username': 'user09'
        }
        self.invalid_payload_update_profile = {
            'new_username': 'user02'
        }

    def test_valid_login(self):
        response = client.post(
            reverse('accounts:login'),
            data=json.dumps(self.valid_payload_login),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_login(self):
        response = client.post(
            reverse('accounts:login'),
            data=json.dumps(self.invalid_payload_login),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_update_profile(self):
        client.login(username='user01', password='user01')
        response = client.put(
            reverse('accounts:update'),
            data=json.dumps(self.valid_payload_update_profile),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_profile(self):
        client.login(username='user01', password='user01')
        response = client.put(
            reverse('accounts:update'),
            data=json.dumps(self.invalid_payload_update_profile),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
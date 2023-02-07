import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Bug
from ..serializers import BugSerializer, ReadBugSerializer
from django.contrib.auth import get_user_model
from datetime import datetime

# initialize the APIClient app
client = Client()

class GetAllBugsTest(TestCase):
    """ Test module for GET all bugs API """
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="user01", email="user01@user01.com", password="user01")
        Bug.objects.create(
            title='Bug01', desc='Bug01 Desc', is_open=True, handle_by=self.user, 
            created_datetime=datetime.now(), updated_datetime=datetime.now(), created_by=self.user, updated_by=self.user)
        Bug.objects.create(
            title='Bug02', desc='Bug02 Desc', is_open=True, handle_by=self.user, 
            created_datetime=datetime.now(), updated_datetime=datetime.now(), created_by=self.user, updated_by=self.user)

    def test_get_all_bugs(self):
        client.login(username='user01', password='user01')
        # get API response
        response = client.get(reverse('bugs:get_post_bugs'))
        # get data from db
        bugs = Bug.objects.only('title')
        serializer = ReadBugSerializer(bugs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleBugTest(TestCase):
    """ Test module for GET single bug API """

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="user01", email="user01@user01.com", password="user01")
        self.bug01 = Bug.objects.create(
            title='Bug01', desc='Bug01 Desc', is_open=True, handle_by=self.user, 
            created_datetime=datetime.now(), updated_datetime=datetime.now(), created_by=self.user, updated_by=self.user)
        self.bug02 = Bug.objects.create(
            title='Bug02', desc='Bug02 Desc', is_open=True, handle_by=self.user, 
            created_datetime=datetime.now(), updated_datetime=datetime.now(), created_by=self.user, updated_by=self.user)
        self.bug03 = Bug.objects.create(
            title='Bug03', desc='Bug03 Desc', is_open=True, handle_by=self.user, 
            created_datetime=datetime.now(), updated_datetime=datetime.now(), created_by=self.user, updated_by=self.user)

    def test_get_valid_single_bug(self):
        client.login(username='user01', password='user01')
        response = client.get(
            reverse('bugs:get_update_bug', kwargs={'pk': self.bug02.pk}))
        bug = Bug.objects.get(pk=self.bug02.pk)
        serializer = BugSerializer(bug)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_bug(self):
        client.login(username='user01', password='user01')
        response = client.get(
            reverse('bugs:get_update_bug', kwargs={'pk': 1000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewBugTest(TestCase):
    """ Test module for inserting a new bug """

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="user01", email="user01@user01.com", password="user01")
        
        self.valid_payload = {
            'title': 'New:Bug01',
            'desc': 'New:Bug01 Desc',
            'is_open': 'True',
            'handle_by': self.user.id,
        }
        self.invalid_payload = {
            'title': '',
            'desc': 'New:Bug02 Desc',
            'is_open': 'True',
            'handle_by': self.user.id,
        }

    def test_create_valid_bug(self):
        client.login(username='user01', password='user01')
        response = client.post(
            reverse('bugs:get_post_bugs'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_bug(self):
        client.login(username='user01', password='user01')
        response = client.post(
            reverse('bugs:get_post_bugs'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleBugTest(TestCase):
    """ Test module for updating an existing bug record """

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="user01", email="user01@user01.com", password="user01")
        self.new_user = User.objects.create_user(username="newuser01", email="newuser01@newuser01.com", password="newuser01")
        self.bug01 = Bug.objects.create(
            title='Bug01', desc='Bug01 Desc', is_open=True, handle_by=self.user, 
            created_datetime=datetime.now(), updated_datetime=datetime.now(), created_by=self.user, updated_by=self.user)
        self.bug02 = Bug.objects.create(
            title='Bug02', desc='Bug02 Desc', is_open=True, handle_by=self.user, 
            created_datetime=datetime.now(), updated_datetime=datetime.now(), created_by=self.user, updated_by=self.user)
        self.bug03 = Bug.objects.create(
            title='Bug03', desc='Bug03 Desc', is_open=True, handle_by=self.user, 
            created_datetime=datetime.now(), updated_datetime=datetime.now(), created_by=self.user, updated_by=self.user)

        self.valid_payload_assign = {
            'title': 'New:Bug01',
            'desc': 'New:Bug01 Desc',
            'is_open': 'True',
            'handle_by': self.new_user.id,
        }
        self.valid_payload_close = {
            'title': 'New:Bug03',
            'desc': 'New:Bug03 Desc',
            'is_open': 'False',
            'handle_by': self.new_user.id,
        }

        self.invalid_payload = {
            'title': '',
            'desc': 'New:Bug03 Desc',
            'is_open': 'True',
            'handle_by': self.user.id,
        }

    def test_valid_update_bug_assign(self):
        client.login(username='user01', password='user01')
        self.assertEqual(self.bug03.handle_by.id, self.user.id)

        response = client.put(
            reverse('bugs:get_update_bug', kwargs={'pk': self.bug03.pk}),
            data=json.dumps(self.valid_payload_assign),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        #Retrieve the bug object again after update
        self.bug03 = Bug.objects.get(pk=self.bug03.pk)
        
        #Check if the bug was assigned to new user
        self.assertEqual(self.bug03.handle_by.pk, self.new_user.id)


    def test_valid_update_bug_close(self):
        client.login(username='user01', password='user01')
        response = client.put(
            reverse('bugs:get_update_bug', kwargs={'pk': self.bug03.pk}),
            data=json.dumps(self.valid_payload_close),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        #Retrieve the bug object again after update
        self.bug03 = Bug.all_objects.get(pk=self.bug03.pk)
        self.assertFalse(self.bug03.is_open)

    def test_invalid_update_bug(self):
        client.login(username='user01', password='user01')
        response = client.put(
            reverse('bugs:get_update_bug', kwargs={'pk': self.bug03.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

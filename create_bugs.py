### content of "create_bugs.py" file
from bugs.models import Bug
from django.contrib.auth import get_user_model
from datetime import datetime

# Get user model
UserModel = get_user_model()
user = UserModel.objects.get(username="user01")

# Create testing bug data
Bug.objects.create(
    title='Bug01', desc='Bug01 Description', is_open=True, handle_by=user, 
    created_datetime=datetime.now(), updated_datetime=datetime.now(), created_by=user, updated_by=user)

Bug.objects.create(
    title='Bug02', desc='Bug02 Description', is_open=True, handle_by=user, 
    created_datetime=datetime.now(), updated_datetime=datetime.now(), created_by=user, updated_by=user)

Bug.objects.create(
    title='Bug03', desc='Bug04 Description', is_open=True, handle_by=user, 
    created_datetime=datetime.now(), updated_datetime=datetime.now(), created_by=user, updated_by=user)

Bug.objects.create(
    title='Bug04', desc='Bug04 Description', is_open=True, handle_by=user, 
    created_datetime=datetime.now(), updated_datetime=datetime.now(), created_by=user, updated_by=user)
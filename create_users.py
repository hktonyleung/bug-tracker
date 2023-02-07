### content of "create_users.py" file
from django.contrib.auth import get_user_model

# Get user model
UserModel = get_user_model()

# Create testing user data
if not UserModel.objects.filter(username='user01').exists():
    user=UserModel.objects.create_user('user01', password='user01')
    user.is_superuser=False
    user.is_staff=True
    user.save()

if not UserModel.objects.filter(username='user02').exists():
    user=UserModel.objects.create_user('user02', password='user02')
    user.is_superuser=False
    user.is_staff=True
    user.save()

if not UserModel.objects.filter(username='user03').exists():
    user=UserModel.objects.create_user('user03', password='user03')
    user.is_superuser=False
    user.is_staff=True
    user.save()

if not UserModel.objects.filter(username='user04').exists():
    user=UserModel.objects.create_user('user04', password='user04')
    user.is_superuser=False
    user.is_staff=True
    user.save()

if not UserModel.objects.filter(username='user05').exists():
    user=UserModel.objects.create_user('user05', password='user05')
    user.is_superuser=False
    user.is_staff=True
    user.save()
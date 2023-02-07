from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('api/v1/login', views.login,name='login'),
    path('api/v1/update', views.update,name='update'),
]
from django.urls import path
from . import views

app_name = 'bugs'

urlpatterns = [
    path('api/v1/<pk>', views.get_update_bug,name='get_update_bug'),
    path('api/v1', views.get_post_bugs, name='get_post_bugs')
]
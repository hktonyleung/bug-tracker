from rest_framework import serializers
from .models import Bug

class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = ('id', 'title', 'desc', 'is_open', 'handle_by', 'created_datetime', 'updated_datetime', 'created_by', 'updated_by')

class ReadBugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = ('id','title', )
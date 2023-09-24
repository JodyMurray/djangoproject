from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from .models import Task


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'complete')

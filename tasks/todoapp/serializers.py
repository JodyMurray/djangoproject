from rest_framework import serializers
from todoapp import models


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'description',
            'complete',
        )
        model = models.Task

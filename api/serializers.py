from rest_framework import serializers

from .models import Task


class TaskSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Task
        fields = ('title', 'desc', 'completed','owner')

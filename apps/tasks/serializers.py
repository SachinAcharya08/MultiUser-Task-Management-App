from rest_framework import serializers
from .models import Tasks

class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model=Tasks
        fields="__all__"
        read_only_fields=["id","created_at","updated_at"]
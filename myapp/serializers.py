from rest_framework import serializers
from .models import Reminder


class Reminderserializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['date', 'message']
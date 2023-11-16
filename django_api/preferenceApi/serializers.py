from rest_framework import serializers
from .models import InternPreference

class InternPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternPreference
        fields = ['id', 'work_status', 'skills']

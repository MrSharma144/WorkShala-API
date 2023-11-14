
from rest_framework import serializers
from .models import Internship,ApplyIntern

class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = '__all__'

class InternshipApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyIntern
        fields = '__all__'

# class uploadSerializer(serializers.ModelSerializer):
#     # resume = serializers.FileField(read_only=False)
#     class Meta:
#         model = ApplyIntern
#         fields = ('resume')
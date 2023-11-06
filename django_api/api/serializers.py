from rest_framework import serializers
from .models import User


class RegisterSerlizer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 60,write_only=True)

    class Meta:
        model = User
        fields = ['email','username','password']

    def validate(self,attrs):
        email=attrs.get('email','')
        username=attrs.get('username','')


        if not username.isalnum():
            raise serializers.ValidationError('username should only contain alpha numeric')
        return attrs
    

    def crete(self,validated_data):
        return User.objects.create_user(**validated_data)
        
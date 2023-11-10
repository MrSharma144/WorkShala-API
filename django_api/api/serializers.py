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
    

    def create(self,validated_data):
        print(User)
        return User.objects.create_user(**validated_data)
    
class EmailVerificationSerializer(serializers.ModelSerializer):
    token=serializers.CharField(max_length=555)

    class Meta:
        model=User
        fields = ['token']
        
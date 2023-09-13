from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from account.models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        refresh = RefreshToken.for_user(instance)
        access = refresh.access_token

        user_data = {
            "username": instance.email,
            "is_staff": instance.is_staff,
            "is_superuser": instance.is_superuser,
        }
        access["user"] = user_data
        data.update({
            "refresh": str(refresh),
            "access": str(access),
        })
        return data
    
class CustomerSerializer(UserSerializer):
    def create(self, validated_data):
        user  = User.objects.create_customer(**validated_data)
        return user
    
class StaffSerializer(UserSerializer):
    def create(self, validated_data):
        user  = User.objects.create_staff(**validated_data)
        return user
    
class SuperAdminSerializer(UserSerializer):
    def create(self, validated_data):
        user  = User.objects.create_superuser(**validated_data)
        return user

    


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Profile
        fields = ['first_name','last_name','mobile', 'address', 'profile_image']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        first_name = user_data.get('first_name')
        last_name = user_data.get('last_name')
        if first_name:
            instance.user.first_name = first_name
        if last_name:
            instance.user.last_name = last_name
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.user.save()
        instance.save()
        return instance
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({
            'email': instance.user.email
        })
        return data





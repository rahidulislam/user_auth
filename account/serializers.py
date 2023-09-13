from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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
class CustomerSerializer(UserSerializer):
    def create(self, validated_data):
        # user = super(UserSerializer, self).create_customer(**validated_data)
        # user.set_password(validated_data['password'])
        user  = User.objects.create_customer(**validated_data)
        # user.save()
        return user

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


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['mobile', 'address', 'profile_image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({
            'full_name': instance.user.get_full_name(),
            'email': instance.user.email
        })
        return data





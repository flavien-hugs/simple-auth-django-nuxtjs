# user.serializers.py

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import(
    validate_password
)

from rest_framework import serializers
from rest_framework.validators import UniqueValidator


unique_validator = UniqueValidator(
    queryset=get_user_model().objects.all()
)


class UserRegisterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(
        required=True,
        validators=[unique_validator]
    )
    email = serializers.EmailField(
        required=True,
        validators=[unique_validator]
    )
    password = serializers.CharField(
        write_only=True, required=True,
        validators=[validate_password]
    )

    class Meta:
        model = get_user_model()
        fields = [
            'phone', 'email',
            'first_name',
            'last_name',
            'password'
        ]
        extra_kwargs = {
           'password': {'write_only': True, 'min_lenght': 8},
           'last_name': {'required': True},
           'first_name': {'required': True}
        }

        def create(self, validated_data):
            user = self.Meta.model.objects.create(
                phone=validated_data['phone'],
                email=validated_data['email'],
                last_name=validated_data['last_name'],
                first_name=validated_data['first_name'],
            )
            user.set_password(validated_data['password'])
            user.save()

            return user


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    class Meta:
        model = get_user_model()
        fields = [
            'phone', 'email',
            'first_name',
            'last_name',
            'password'
        ]
        extra_kwargs = {
            'password': {'write_only': True, 'min_lenght': 8},
            'last_name': {'required': True},
            'first_name': {'required': True}
        }

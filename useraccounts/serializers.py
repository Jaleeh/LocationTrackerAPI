from rest_framework import fields, serializers
from .models import User

class CustomRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','email', 'password',)
        extra_kwargs = {
            'password': {'write_only':  True    }
            }

    def validate(self, attrs):
        email = attrs.get('email','')
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email', ('Email is already being used by a different user')}
            )
        return super().validate(attrs)

    def create_user(self, validated_data):
        return User.objects.create(**validated_data)


    



class CustomLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    

    class Meta:
        model = User
        fields = ('email', 'password',) 



class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email',)



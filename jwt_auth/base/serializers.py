from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = "__all__"
        

    def validate(self, data):
        password = data['password']
        print(data)
        if  data['password'] != data['password2']:
            raise serializers.ValidationError({'password':'Passwords doesnot match.'})
        if len(password) < 8 :
            raise serializers.ValidationError({'password': 'Password must have more then 8 charecters.'})
        print(data)
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2', None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('password2', None)
        return super().update(instance, validated_data)
    



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        # password = make_password(password)
        # password = make_password(password)
        if not CustomUser.objects.filter(email = email).exists():
            raise serializers.ValidationError({'email':'Email doesnot exists.'})
        user = CustomUser.objects.get(email = email)
        if user.password != password:
            raise serializers.ValidationError({'password':'Password not matched.'})
        if email and password:
            user = authenticate(email=email, password=password)
        data['email'] = email.lower()
        data['user'] = user
        return data

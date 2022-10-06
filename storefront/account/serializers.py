from dataclasses import fields
from statistics import mode
from xml.dom import ValidationErr
from rest_framework import serializers
from account.models import User
from crud.models import Student
from . import utils
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
""" all the serializer classes turns the queryset or database models into python data models, It's the serialization process """


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
     

"""Here normal serializer is implemented as the model serializer implemented above"""
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length = 255)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length = 255)
#     """ field level validation"""


#     def validate_roll(self, value):
#         if value >= 200:
#             raise serializers.ValidationError('Seat Full')
#         return value


#     def validate(self, data):
#         nm = data.get('name')
#         ct = data.get('city')
#         if nm.lower() != 'sakib':
#             raise serializers.ValidationError('error on name sakib')
#         return data


#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.roll = validated_data.get('roll',instance.roll)
#         instance.city = validated_data.get('city',instance.city)
#         instance.save()

#         return instance

class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style = {
        'input_type':'password'
    }, write_only = True)
    class Meta:
        model = User
        fields = ['email','name','password','password2','tc']
        extra_kwargs = {
            'password':{'write_only': True}
        }
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255)
    class Meta:
        model = User
        fields = ['email','password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','name']

class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length = 255,style = {
        'input_type':'password'
    }, write_only = True)
    password2 = serializers.CharField(max_length = 255,style = {
        'input_type':'password'
    }, write_only = True)

    class Meta:
        fields = ['password','password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        user.set_password(password)
        user.save()
        return attrs


class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length = 255)
    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
    
        if User.objects.filter(email = email).exists():
            user = User.objects.get(email = email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded UID',uid)
            token = PasswordResetTokenGenerator().make_token(user=user)
            print('Password Reset Token', token)
            link = 'http://127.0.0.1:3000/api/user/reset/'+uid+'/'+token
            print('Password Reset link', link)
            body = 'Click Following Link to Reset Your password'+link
            """send email"""
            data = {
                'subject':'Reset Your Password',
                'body': body,
                'to_email': user.email
            }

            utils.Util.send_email(data)
            
            return attrs


        else:
            raise serializers.ValidationError("You are not a registered User")

class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length = 255,style = {
        'input_type':'password'
    }, write_only = True)
    password2 = serializers.CharField(max_length = 255,style = {
        'input_type':'password'
    }, write_only = True)

    class Meta:
        fields = ['password','password2']


    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')

            if password != password2:
                raise serializers.ValidationError("Password and Confirm Password doesn't match")
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id = id)
            if not PasswordResetTokenGenerator().check_token(user,token=token):
                raise ValidationErr('Token is not valid or Expired')
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user=user, token=token)
            raise ValidationErr('Token is not valid or Expired')



    

from rest_framework import serializers
from User.models import UserProfile
from django.contrib.auth.models import User





class UserSerializer(serializers.HyperlinkedModelSerializer):
	username = serializers.CharField()
	password = serializers.CharField(
		style={'input_type': 'password'},
		write_only=True)
	class Meta:
		model = User
		fields = (
			'id',
			'username',
			'password',
			'email',
			'first_name',
			'last_name',
			)
		
class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
	user = UserSerializer()
	mobileNumber = serializers.IntegerField(default = 0)
	isFaculty = serializers.BooleanField(default = False)
	avatar = serializers.ImageField(default = '/static/User/defaultProfileImage.png')
	class Meta:
		model = UserProfile
		fields = (
			'user',
			'mobileNumber',
			'isFaculty',
			'avatar')

	def create(self , validated_data):
		user_data = validated_data.pop('user')
		user = User(
			username = user_data['username'],
			email = user_data['email'],
			first_name = user_data['first_name'],
			last_name = user_data['last_name'])
		user.set_password(user_data['password'])
		user.save()
		profile = UserProfile(
			user = user,
			mobileNumber = validated_data['mobileNumber'],
			isFaculty = validated_data['isFaculty'],
			avatar = validated_data['avatar'] 
			)
		profile.save()
		return profile
		

	
	
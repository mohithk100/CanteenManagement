from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile



class  UserRegisterationForm(UserCreationForm):
	username = forms.CharField(
						max_length = 15, 
						required = True, 
						widget = forms.TextInput(attrs={'class':'form-control' , 'id':'username' , 'placeholder':'Username'}),
						)
	email = forms.EmailField(
						required = True,
						widget = forms.EmailInput(attrs = {'class':'form-control' , 'id':'email' ,'placeholder':'Email'}),
						)
	first_name = forms.CharField(
						required = True,
						widget = forms.TextInput(attrs = {'class':'form-control' , 'id':'first_name' ,'placeholder':'First Name'}),
						) 
	last_name = forms.CharField(
						required = True,
						widget = forms.TextInput(attrs = {'class':'form-control' , 'id':'last_name' ,'placeholder':'Last Name'}),
						)
	password1 = forms.CharField(
						required = True,
						widget = forms.PasswordInput(attrs = {'class':'form-control' , 'id':'password' ,'placeholder':'Password'}),
						)
	password2 = forms.CharField(
						required = True,
						widget = forms.PasswordInput(attrs = {'class':'form-control' , 'id':'confirm_password' ,'placeholder':'Confirm Password'}),
						)

	class Meta:
		model = User
		fields = (
			'username',
			'password1',
			'password2',
			'email',
			'first_name',
			'last_name',
			)




	def save(self, commit = True):
		user = super(UserRegisterationForm , self).save(commit = False)
		user.username = self.cleaned_data['username']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		user.set_password('password1')
		if commit:
			user.save()
		return user

class UserProfileRegisterationForm(forms.ModelForm):
	mobileNumber = forms.IntegerField(
							required = True,
							widget = forms.TextInput(attrs = {'class':'form-control' , 'id':'mobileNumber' ,'placeholder':'Mobile Number'}),
							)
	isFaculty = forms.ChoiceField(
							required = True,
							choices = ((True , 'Faculty'),( False , 'Non-Faculty')) , 
							initial = False, 
							widget = forms.Select(attrs = {'class':'custom-select mb-2 mr-sm-2 mb-sm-0' , 'id':'isFaculty' }),
							)
	class Meta:
		model = UserProfile
		fields = (
			'mobileNumber',
			'isFaculty',
			)

	def save(self , commit  = True):
		user_profile = super(UserProfileRegisterationForm , self).save(commit = False)
		user_profile.mobileNumber = self.cleaned_data['mobileNumber']
		user_profile.isFaculty =self.cleaned_data['isFaculty']
		if commit:
			user_profile.save()
		return user_profile
		
			
	
		
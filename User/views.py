from django.shortcuts import render
from django.http import HttpResponse , Http404
from .forms import (
	UserProfileRegisterationForm,
	UserRegisterationForm,
	)

def UserProfileRegisteration(request):
	
	if request.method == 'GET':
		user_form = UserRegisterationForm()
		user_profile_form = UserProfileRegisterationForm()
		context = { 'user_profile_form': user_profile_form, 'user_form': user_form }
		return render(request, 'User/RegisterationPage.html' , context)
	
	elif request.method == 'POST':
		user_form= UserRegisterationForm(request.POST)
		user_profile_form = UserProfileRegisterationForm(request.POST)
		if user_form.is_valid() and user_profile_form.is_valid():
			print 'validated'
			user = user_form.save()
			print user
			profile = user_profile_form.save(commit = False)
			print profile
			profile.user = user
			profile.save()
		
			
			
			
		

		
							
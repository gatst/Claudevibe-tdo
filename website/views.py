from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def home(request):
	return render(request, 'home.html', {})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, f'Welcome {username}!')
				return redirect('home')
			else:
				messages.error(request, 'Invalid username or password.')
	else:
		form = AuthenticationForm()
	return render(request, 'login.html', {'form': form})

def register_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			login(request, user)
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'register.html', {'form': form})

def logout_view(request):
	logout(request)
	messages.success(request, 'You have been logged out.')
	return redirect('home')
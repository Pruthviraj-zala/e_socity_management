from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignupForm

# Create your views here.
def userSignupView(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if already logged in
    
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please login to continue.')
            return redirect('login')  # Redirect to login page after successful signup
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = UserSignupForm()
    
    return render(request, 'core/signup.html', {'form': form})

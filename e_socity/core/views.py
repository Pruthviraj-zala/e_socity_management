from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import UserSignupForm, UserLoginForm

# Create your views here.
def userSignupView(request):
    if request.user.is_authenticated:
        return redirect('login')  # Redirect to login if already logged in
    
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

def userLoginView(request):
  if request.method == "POST":
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      user = authenticate(request, email=email, password=password)  # Check in database
      if user:
        print(f"DEBUG: User authenticated - Email: {user.email}, Role: {user.role}")  # Debug line
        login(request, user)
        print(f"DEBUG: User logged in - Is authenticated: {request.user.is_authenticated}")  # Debug line
        if user.role == "ADMIN":
          print("DEBUG: Redirecting to admin_dashboard")  # Debug line
          return redirect("admin_dashboard")
        elif user.role == "RESIDENT":
          print("DEBUG: Redirecting to resident_dashboard")  # Debug line
          return redirect("resident_dashboard")
        elif user.role == "GUARD":
          print("DEBUG: Redirecting to guard_dashboard")  # Debug line
          return redirect("guard_dashboard")
        else:
          print(f"DEBUG: Role not recognized - {user.role}")  # Debug line
          # Default redirect if role is not recognized
          return redirect("home")
      else:
        messages.error(request, 'Invalid email or password. Please try again.')
        return render(request, 'core/login.html', {'form': form})
    else:
      # Form validation errors
      for field, errors in form.errors.items():
        for error in errors:
          messages.error(request, f'{field}: {error}')
  else:
    form = UserLoginForm()
  
  return render(request, 'core/login.html', {'form': form})
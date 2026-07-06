from django.shortcuts import render, redirect

# Create your views here.
from .utils import create_default_admin
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    create_default_admin()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # 🔥 Role-based redirection
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'controller':
                return redirect('controller_dashboard')
            elif user.role == 'viewer':
                return redirect('viewer_dashboard')
            else:
                return redirect('login')

        return redirect('login')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
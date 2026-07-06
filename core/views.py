from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.contrib.auth.decorators import login_required
from accounts.models import User
from customer.models import Customer
from .models import Rooms

@login_required
def dashboard(request):
    return render(request, 'admin/dashboard.html')

@login_required
def user_management(request):
    users = User.objects.all()

    total_admin = User.objects.filter(role='admin').count()
    total_staff = User.objects.filter(role='staff').count()

    context = {
        'users': users,
        'total_admin': total_admin,
        'total_staff': total_staff,
    }

    return render(request, 'admin/user_management.html', context)

@login_required
def user_create(request):
    if request.method == 'POST':
        # Handle form submission and user creation logic here
        username = request.POST.get('username')
        role = request.POST.get('role')
        password = request.POST.get('password')

        if username and role and password:
            user = User.objects.create_user(username=username, password=password)
            user.role = role
            user.is_active = True  # Set the user as active by default
            user.save()
            return redirect('user_management')  # Redirect to user management page after successful creation
        
    return render(request, 'admin/user_create.html')

@login_required
def user_update(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == "POST":
        user.full_name = request.POST.get("full_name")
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.role = request.POST.get("role")
        user.status = request.POST.get("status")

        password = request.POST.get("force_password")
        if password:
            user.set_password(password)

        user.save()

        return redirect("user_management")

    return render(request, "admin/user_update.html", {
        "user": user,
    })

@login_required
def user_suspend(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == "POST":
        user.is_active = False      # Suspend account
        user.save()

    return redirect("user_management")


#Customer
@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'admin/customer_list.html', {'customers': customers})

@login_required
def customer_suspend(request, id):
    customer = get_object_or_404(Customer, id=id)

    if request.method == "POST":
        customer.is_active = False  # Suspend account
        customer.save()

    return redirect("customer_list")

@login_required
def room_list(request):
    rooms = Rooms.objects.all()
    return render(request, 'admin/room_list.html', {'rooms': rooms})

@login_required
def add_room(request):
    if request.method == 'POST':
        # Handle form submission and room creation logic here
        room_number = request.POST.get('room_number')
        room_type = request.POST.get('room_type')
        price = request.POST.get('price')
        room_description = request.POST.get('room_description')
        image = request.FILES.get('image')  # Get the uploaded image file
        is_available = request.POST.get('is_available') == 'on'  # Convert checkbox value to boolean


        if room_number and room_type and price:
            # Create a new Room object and save it to the database
            # Assuming you have a Room model defined in your models.py
            Rooms.objects.create(room_number=room_number, room_type=room_type, price=price, room_description=room_description, image=image, is_available=is_available)
            return redirect('room_list')  # Redirect to room list page after successful creation
        
    return render(request, 'admin/add_room.html')

@login_required
def booking_list(request):
    return render(request, 'admin/booking_list.html')
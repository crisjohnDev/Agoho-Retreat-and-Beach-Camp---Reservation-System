from django.urls import path
from . import views

urlpatterns = [
    path('account/dashboard/', views.dashboard, name='admin_dashboard'),
    path('account/user-management/', views.user_management, name='user_management'),
    path('account/user-management/create/', views.user_create, name='user_create'),
    path('account/user-management/update/<int:id>', views.user_update, name='user_update'),
    path("account/user-management/suspend/<int:id>/", views.user_suspend, name="user_suspend",),
    path('account/customer-management/', views.customer_list, name='customer_list'),
    path('account/customer-management/suspend/<int:id>/', views.customer_suspend, name='customer_suspend'),
    path('account/room-management/', views.room_list, name='room_list'),
    path('account/room-management/add/', views.add_room, name='room_create'),
]
from django.urls import path
from . import views
app_name='apartName'

urlpatterns = [
    path('',views.home_view,name='home'),
    path('home/',views.home_view,name='home'),
    path('home1/',views.staff_home,name='staff_home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/',views.profile_view,name='profile'),
    path('profile/add/', views.add_profile, name='add_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('adminUser/add_property/', views.add_property, name='property'),
    path('adminUser/add_room/', views.add_room, name='add_room'),
    path('apartment/<int:apartment_id>/', views.apartment_detail, name='apartment_detail'),
    path('room/<int:room_id>/', views.room_detail, name='room_detail'),
    path('room/<int:room_id>/book/', views.book_room, name='book_room'),
    path('adminUser/booking/error/', views.booking_error, name='booking_error'),
    path('adminUser/booking/success/', views.booking_success, name='booking_success'),
    path('adminUser/bookings/list', views.booking_list, name='booking_list'),
    path('adminUser/payment/', views.manage_payment, name='pay_all_user'),
    path('adminUser/payment-records/', views.payment_record_list, name='payment_record_list'),
    path('adminUser/users/', views.staff_user_Data, name='users_list'),
    path('adminUser/payment/success/',views.success,name='success_page')


]

from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404,redirect
from .models import Property,Room,Profile,Booking,PaymentRecord,Account
from .forms import RegistrationForm,LoginForm,ProfileForm,PropertyForm,RoomForm,BookingForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home_view(request):
    apartments = Property.objects.all()
    rooms = Room.objects.all()
    return render(request, 'apartmentApp/home.html', {'apartments': apartments, 'rooms': rooms})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apartName:login')  # Redirect to login page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'apartmentApp/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('apartName:staff_home')  # Redirect to staff home page
                else:
                    return redirect('apartName:home')  # Redirect to regular home page
    else:
        form = LoginForm()
    return render(request, 'apartmentApp/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('apartName:home')  # Redirect to home page after logout

@login_required
def profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
        booked_room = Booking.objects.filter(user=request.user).first()  # Get the first booked room if any
        
        return render(request, 'apartmentApp/profile.html', {'profile': profile, 'booked_room': booked_room})
    except Profile.DoesNotExist:
        return redirect('apartName:add_profile')



def add_profile(request):
    try:
        # Check if the user already has a profile
        profile = Profile.objects.get(user=request.user)
        return redirect('apartName:profile')  # Redirect to edit profile view if profile already exists
    except Profile.DoesNotExist:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                # Create a new profile for the user
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                return redirect('apartName:profile')
        else:
            form = ProfileForm()
        return render(request, 'apartmentApp/add_profile.html', {'form': form})


def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('apartName:staff_home')  # Redirect to home page after successful property creation
    else:
        form = PropertyForm()
    return render(request, 'staff/add_property.html', {'form': form})
def add_room(request):
    if request.method == 'POST':
        room_form = RoomForm(request.POST, request.FILES)
        if room_form.is_valid():
            room_instance = room_form.save()
            return redirect('apartName:staff_home')  # Redirect to home page after successful room creation
        else:
             print(room_form.errors)
    else:
        room_form = RoomForm()
    return render(request, 'staff/add_room.html', {'room_form': room_form})

def apartment_detail(request, apartment_id):
    apartment = get_object_or_404(Property, pk=apartment_id)
    rooms = Room.objects.filter(property=apartment)
    return render(request, 'apartmentApp/apartment_detail.html', {'apartment': apartment, 'rooms': rooms})

def room_detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'apartmentApp/roomData.html', {'room': room})

@login_required
def book_room(request, room_id):
    room = Room.objects.get(id=room_id)
    user_bookings = Booking.objects.filter(user=request.user)
    
    # Check if the user already has a booked room
    if user_bookings.exists():
        # You can customize the redirect behavior or display a message here
        return redirect('apartName:booking_error')  # Redirect to an error page or display a message

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            user = request.user
            room_number = room.room_number
            room_fee = room.rent_fee
            # You can set the payment_status as False by default
            booking = Booking(user=user, room=room, room_number=room_number, room_fee=room_fee)
            booking.save()
            # You may also handle payment processing here if needed
            return redirect('apartName:booking_success')  # Redirect to a success page after booking
    else:
        form = BookingForm()
    return render(request, 'apartmentApp/book_room.html', {'form': form, 'room': room})

def booking_error(request):
    return render(request, 'apartmentApp/booking_error.html')

def booking_success(request):
    return render(request, 'apartmentApp/booking_success.html')

def edit_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('apartName:add_profile')  # Redirect to add profile if profile doesn't exist

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('apartName:profile')  # Redirect to profile view after successful update
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'apartmentApp/edit_profile.html', {'form': form})


def manage_payment(request):
    # Get all rooms
    rooms = Room.objects.all()
    
    for room in rooms:
        # Get all bookings for the room with payment_status=False
        bookings = Booking.objects.filter(room=room)
        
        for booking in bookings:
            # Get the user's account
            user_account = Account.objects.get(user=booking.user)
            
            # Check if the user has sufficient balance
            if user_account.balance < room.rent_fee:
                messages.warning(request, f"Insufficient balance for {booking.user.username} for room {room.room_number}. Payment not processed.")
                # Update payment_status to False
                booking.payment_status = False
                booking.save()
            else:
                # Subtract the room fee from the user's balance
                user_account.balance -=room.rent_fee
                user_account.save()
                
                try:
                    payment_record = PaymentRecord.objects.create(account=user_account, amount=room.rent_fee)
                    
                    # Update payment_status for the booking
                    booking.payment_status = True
                    booking.save()
                    
                    messages.success(request, f"Payment successful for room {room.room_number} for {booking.user.username}.")
                except IntegrityError:
                    messages.error(request, "Failed to create payment record. Please try again.")
    

    return redirect('apartName:success_page') 

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'staff/booking_list.html', {'bookings': bookings})

def payment_record_list(request):
    payment_records = PaymentRecord.objects.all()
    return render(request, 'staff/payment_record_list.html', {'payment_records': payment_records})

def staff_user_Data(request):
    profiles = Profile.objects.all()
    return render(request, 'staff/user_data.html', {'profiles': profiles})


def staff_home(request):
    apartments = Property.objects.all()
    rooms = Room.objects.all()
    return render(request, 'staff/staff_home.html', {'apartments': apartments, 'rooms': rooms})

def success(request):
    return render(request, 'staff/success_page.html')
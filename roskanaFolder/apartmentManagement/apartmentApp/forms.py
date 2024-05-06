from django import forms
from .models import Property,Room,Profile,Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))



class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'  # Use all fields from the Property model
        
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'  # Use all fields from the Room model

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'phone', 'city', 'state', 'zipcode', 'country']
        labels = {
            'avatar': 'Avatar (Optional)',
            'bio': 'Bio',
            'phone': 'Phone Number',
            'city': 'City',
            'state': 'State',
            'zipcode': 'ZIP Code',
            'country': 'Country',
        }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = []

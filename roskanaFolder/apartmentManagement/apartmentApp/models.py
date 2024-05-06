from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    property_name = models.CharField(max_length=200)
    property_type = models.CharField(max_length=200)
    property_numRooms = models.PositiveIntegerField()
    property_numPeopleCurrent = models.PositiveIntegerField()
    property_image = models.ImageField(upload_to='property/')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField()
    facilities = models.ManyToManyField('Facility')
    owner_name = models.CharField(max_length=100)
    owner_email = models.EmailField()
    owner_phone = models.CharField(max_length=20)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    number_of_reviews = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.property_name
    

class Facility(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Room(models.Model):
    property = models.ForeignKey(Property, related_name='rooms', on_delete=models.CASCADE)
    room_number = models.CharField(max_length=50)
    room_type = models.CharField(max_length=100)
    occupancy = models.PositiveIntegerField(default=0)
    bed_type = models.CharField(max_length=100)
    rent_fee = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    room_image = models.ImageField(upload_to='rooms/')
    number_of_bathrooms = models.PositiveIntegerField(default=1)
    number_of_kitchens = models.PositiveIntegerField(default=1)
    property_num_bed_Rooms = models.PositiveIntegerField(default=1)
    property_numPeopleCurrent = models.PositiveIntegerField(default=0)
    amenities = models.ManyToManyField(Amenity)
    features = models.ManyToManyField(Feature)

    class Meta:
        # Enforce uniqueness of room numbers within each property
        unique_together = ('property', 'room_number')
    
    def __str__(self):
        return f"Room {self.room_number} - {self.property.property_name}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/')
    bio = models.TextField(max_length=500, blank=True)
    date_account_created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
    

class Booking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=50)
    room_fee = models.DecimalField(max_digits=10, decimal_places=2)
    date_booked = models.DateField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.room.room_number} ({self.date_booked})"



class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Account for {self.user.username}"

class PaymentRecord(models.Model):
    account = models.ForeignKey(Account, related_name='records', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} for {self.account.user.username} at {self.timestamp}"
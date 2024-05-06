from django.contrib import admin
from .models import Property, Room, Facility, Amenity, Feature,Profile, Booking ,Account, PaymentRecord

# Register your models here.

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_name', 'property_type', 'owner_name', 'owner_email')
    search_fields = ('property_name', 'property_type', 'owner_name')
    list_filter = ('property_type',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'property', 'room_type', 'occupancy', 'bed_type', 'rent_fee', 'is_available')
    search_fields = ('room_number', 'room_type', 'bed_type')
    list_filter = ('property', 'room_type', 'is_available')

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'bio', 'phone', 'city', 'state', 'zipcode', 'country')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'room_number', 'room_fee', 'date_booked', 'payment_status')
    search_fields = ('user__username', 'room__room_number')
    list_filter = ('date_booked', 'payment_status')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')

@admin.register(PaymentRecord)
class PaymentRecordAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'timestamp')
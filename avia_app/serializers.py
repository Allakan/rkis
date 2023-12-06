from rest_framework import serializers
from .models import Airport, Flight, Passenger, Reservation


# Сериализатор для модели Airport
class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'


# Сериализатор для модели Flight
class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


# Сериализатор для модели Passenger
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


# Сериализатор для модели Reservation
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

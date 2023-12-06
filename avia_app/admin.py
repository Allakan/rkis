from django.contrib import admin
from .models import Airport, Flight, Passenger, Reservation

# Зарегистрируйте модели для административного интерфейса
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Reservation)

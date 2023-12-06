"""
URL configuration for avia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from avia_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('airports/', views.AirportList.as_view(), name='airport-list'),
    path('airports/<int:pk>/', views.AirportDetail.as_view(), name='airport-detail'),

    # Маршруты для рейсов
    path('flights/', views.FlightList.as_view(), name='flight-list'),
    path('flights/<int:pk>/', views.FlightDetail.as_view(), name='flight-detail'),

    # Маршруты для пассажиров
    path('passengers/', views.PassengerList.as_view(), name='passenger-list'),
    path('passengers/<int:pk>/', views.PassengerDetail.as_view(), name='passenger-detail'),

    # Маршруты для бронирований
    path('reservations/', views.ReservationList.as_view(), name='reservation-list'),
    path('reservations/<int:pk>/', views.ReservationDetail.as_view(), name='reservation-detail'),
]

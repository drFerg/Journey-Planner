from django.shortcuts import render
from models import Flight, Hotel
from itertools import chain

# Create your views here.

def index(request):
    flights = Flight.objects.order_by('departDate')
    return render(request, 'card-flight.html', {'flights': flights})

def paper(request):
    flights = Flight.objects.order_by('departDate')
    hotels = Hotel.objects.order_by('checkIn')
    cards = list(chain(flights, hotels))
    return render(request, 'flight-card-template.html', {'cards': cards})

def flightCard(request):
    return render(request, 'flight-card.html')

def hotelCard(request):
    return render(request, 'hotel-card.html')

def post_list(request):
    return render(request, 'post-list.html')
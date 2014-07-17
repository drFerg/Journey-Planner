from django.shortcuts import render
from models import Flight

# Create your views here.

def index(request):
    flights = Flight.objects.order_by('departDate')
    return render(request, 'card-flight.html', {'flights': flights})

def paper(request):
    return render(request, 'paper.html')

def card(request):
    return render(request, 'post-card.html')

def post_list(request):
    return render(request, 'post-list.html')
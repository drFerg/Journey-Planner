from django.db import models

# Create your models here.
class Flight(models.Model):
    airline = models.CharField(max_length=30)
    flightNum = models.CharField(max_length=20)
    departPort = models.CharField(max_length=100)
    departCity = models.CharField(max_length=100)
    arrivePort = models.CharField(max_length=100)
    arriveCity = models.CharField(max_length=100)
    departDate = models.DateTimeField('Departure time')
    arriveDate = models.DateTimeField('Arrive time')
    flightTime = models.IntegerField()
    connectingFlight = models.ForeignKey('self', null=True, blank=True)
    def cardType(self):
        return "flight"
    def __unicode__(self):
        return self.airline + " " + self.flightNum + ", From: " + self.departPort + ", To: " + self.arrivePort

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(max_length=200)
    checkIn = models.DateTimeField('Check-in')
    checkOut = models.DateTimeField('Check-out')
    nights = models.IntegerField()
    stars = models.IntegerField()
    price = models.FloatField()

    def cardType(self):
        return "hotel"
    def __unicode__(self):
        return self.name + " " + self.checkIn.strftime("%d/%m") + "-" + self.checkOut.strftime("%d/%m")

class Visit(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(max_length=200)
    address = models.TextField(max_length=200);
    visitDate = models.DateTimeField('Visit date')
    length = models.IntegerField()
    def cardType():
        return "hotel"

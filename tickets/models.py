from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=25, unique=True)


class City(models.Model):
    name = models.CharField(max_length=10, unique=True)
    language = models.ForeignKey(to=Language, on_delete=models.CASCADE)
    seats = models.PositiveIntegerField()


class Movie(models.Model):
    name = models.CharField(max_length=100)
    duration = models.FloatField()


class MoviesCityThrough(models.Model):
    city = models.ForeignKey(to=City, on_delete=models.CASCADE)
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE)
    m1 = models.BooleanField(null=True)
    m2 = models.BooleanField(null=True)
    a1 = models.BooleanField(null=True)
    a2 = models.BooleanField(null=True)
    e1 = models.BooleanField(null=True)
    e2 = models.BooleanField(null=True)
    e3 = models.BooleanField(null=True)
    amount = models.PositiveIntegerField()


class MovieLanguageThrough(models.Model):
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE)
    language = models.ForeignKey(to=Language, on_delete=models.CASCADE)


class Ticket(models.Model):
    city = models.ForeignKey(to=City, on_delete=models.CASCADE)
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE)
    show = models.DateTimeField()
    no_of_seats = models.PositiveIntegerField()
    username = models.CharField(max_length=20)
    status = models.BooleanField(null=True)
    total_amount = models.PositiveIntegerField()


class TicketSeats(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    seat_no = models.PositiveIntegerField()


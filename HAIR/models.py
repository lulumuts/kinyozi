from django.db import models


class Frequency(model.Models):
    NONE = 'NONE'
    ONCE = 'ONCE'
    TWICE = 'TWICE'
    THREE = 'THREE'
    CHOICES = (
        (ONCE, 'once'),
        (TWICE, 'twice'),
        (THREE, 'three'),
        (FOUR, 'four'),

    )

    times = models.CharField(max_length=5, choices=CHOICES, default=NONE)

    def __str__(self):
        return self.times


class Location(models.Models):

    place = models.Charfield()

    def __str__(self):
        return self.place


class Style(model.Models):

    image = models.ImageField(upload_to='products/', blank=True)
    name = models.Charfield()

    def __str__(self):
        return self.name


class Stylist(model.Models):

    photo = models.ImageField(upload_to='posts/', blank=True)
    name = models.Charfield()
    style = models.ManyToManyField(Style)
    location = models.ForeignKey(Location)
    cost = models.IntegerField()
    booked = models.BoolField(default=False)

    def __str__(self):
        return self.name


class Preference(model.Models):

    hair_style = models.Charfield()
    hair_products = ManyToManyField(Products)
    budget = models.IntegerField()
    per = models.ForeignKey(Frequency)

    def __str__(self):
        return self.hair_style


class Products(model.Models):

    image = models.ImageField(upload_to='products/', blank=True)
    brand = models.Charfield()

    def __str__(self):
        return self.brand

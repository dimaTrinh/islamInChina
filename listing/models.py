from django.db import models
from django.urls import reverse

# Create your models here.


class Person(models.Model):
    last_name = models.CharField("Last Name", max_length=100, blank=True)
    first_name = models.CharField("First Name", max_length=100, blank=True)
    middle_name = models.CharField("Middle Name", max_length=100, blank=True)

    gender = models.CharField("Gender", blank=True, max_length=20)

    birth_date = models.DateField("Birth Date", blank=True)
    death_date = models.DateField("Death Date", blank=True)
    birth_place = models.ForeignKey(
        "Place", blank=True, null=True, related_name="birth_place", on_delete=models.CASCADE)
    death_place = models.ForeignKey(
        "Place", blank=True, null=True, related_name="death_place", on_delete=models.CASCADE)

    ROLES = (('au', 'Author'),
             ('as', 'Assembler'),
             ('ed', 'Editor'),
             ('sc', 'Scrivener'),
             ('tr', 'Translator'),
             ('ot', 'Others'))

    type_of = models.CharField("Roles of the person",
                               max_length=2, choices=ROLES, blank=True, null=True,
                               default='au')

    # Works that the person has been involved with, either as author or translators
    #related_works = models.ManyToManyField("Manuscript")

    def __str__(self):
        return " ".join([self.first_name, self.middle_name, self.last_name])


class Place(models.Model):
    name = models.CharField("Name of Place", max_length=200, blank=True)
    county = models.CharField("County", max_length=100, blank=True)
    state = models.CharField("State", max_length=100, blank=True)
    latitude = models.CharField(
        "Latitude", max_length=100, blank=True, null=True)
    longitude = models.CharField(
        "Longitude", max_length=100, blank=True, null=True)
    notes = models.TextField("Description Field", max_length=500, blank=True)

    def __str__(self):
        return self.name

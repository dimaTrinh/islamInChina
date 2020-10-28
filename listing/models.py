from django.db import models
from django.urls import reverse

# Create your models here.


class Person(models.Model):
    last_name = models.CharField("Last Name", max_length=100, blank=True)
    first_name = models.CharField("First Name", max_length=100, blank=True)
    middle_name = models.CharField(
        "Middle Name", max_length=100, blank=True, null=True)

    gender = models.CharField("Gender", blank=True, max_length=20)

    birth_date = models.DateField("Birth Date", blank=True, null=True)
    death_date = models.DateField("Death Date", blank=True, null=True)
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
    related_works = models.ManyToManyField("Work")

    notes = models.TextField("Note Field", blank=True,
                             null=True, max_length=100)
    bio_notes = models.TextField(
        "Biography Note Field", blank=True, null=True, max_length=100)

    def __str__(self):
        return self.first_name + " " + self.middle_name + " " + self.last_name + " " + self.type_of


class Place(models.Model):
    name = models.CharField(
        "Name of Place", max_length=200, blank=True, null=True)
    county = models.CharField("County", max_length=100, blank=True, null=True)
    state = models.CharField("State", max_length=100, blank=True, null=True)

    latitude = models.CharField(
        "Latitude", max_length=100, blank=True, null=True)
    longitude = models.CharField(
        "Longitude", max_length=100, blank=True, null=True)
    notes = models.TextField(
        "Description Field", max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Work(models.Model):
    arabic_title = models.CharField("Title", max_length=300, blank=True)
    chinese_title = models.CharField("Title", max_length=300, blank=True)

    author_id = models.ForeignKey(
        "Person", blank=True, null=True, related_name="author_id", on_delete=models.CASCADE)

    translator_id = models.ForeignKey(
        "Person", blank=True, null=True, related_name="translator_id", on_delete=models.CASCADE)

    author_name = models.CharField("Author", max_length=100, blank=True)
    translator_name = models.CharField(
        "Translator", max_length=100, blank=True)

    pub_date = models.CharField("Date", max_length=50, blank=True)

    TYPES = (('b', 'Book'),
             ('m', 'Manuscript'))

    type_of = models.CharField("Type of the work", max_length=1, choices=TYPES, blank=True, null=True,
                               default='m')

    summary = models.CharField("Summary", max_length=1000, blank=True)
    num_pages = models.IntegerField("Number of Pages", blank=True, null=True)
    transcribed = models.BooleanField("Transcribed", default=True)

    def __str__(self):
        return self.arabictitle + " " + self.chinese_title + " " + self.author_name + " " + self.translator_name


class Page(models.Model):
    work_id = models.ForeignKey(
        "Work", blank=True, null=True, related_name="work_id", on_delete=models.CASCADE)
    img_url = models.CharField("Image URL", max_length=200, blank=True)
    transcribed = models.BooleanField("Transcribed", default=True)

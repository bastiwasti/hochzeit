from django.db import models

Anmeldung = (
    ('1', 'Ja'),
    ('2', 'Nein'),
    ('3', 'Noch nicht entschieden'),
)

Essen = (
    ('1', 'Fleisch'),
    ('2', 'Fisch'),
    ('3', 'Vegetarisch'),
)

class Eintrag(models.Model):
    Name = models.CharField(max_length=200)
    Anmeldung = models.CharField(
        max_length=2,
        choices=Anmeldung)
    Essen = models.CharField(
        max_length=2,
        choices=Essen)
    Email = models.EmailField()
    pub_date = models.DateTimeField('date published')
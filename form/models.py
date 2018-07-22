from django.db import models

Anmeldung = (
    ('1', 'Ja'),
    ('2', 'Nein'),
    ('3', 'Noch nicht entschieden'),
)

class Eintrag(models.Model):
    User = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    Anmeldung = models.CharField(
        max_length=2,
        choices=Anmeldung)
    Email = models.EmailField()
    pub_date = models.DateTimeField('date published')
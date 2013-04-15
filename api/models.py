from django.db import models
from django import forms

POSITION_FOOTBAL = (
    ('GK', 'Arquero'),
    ('DF', 'Defensa'),
    ('MF', 'Volante'),
    ('FW', 'Delantero'),
)

PROFILE_LEG = (
	('AD','Ambidiestro'),
	('DR','Derecho'),
    ('IZ','Izquierdo'),
)

# Create your models User.
class User(models.Model):

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    position = models.CharField(max_length=2, choices=POSITION_FOOTBAL)
    ranking = models.FloatField()
    old = models.DateField()
    profile = models.CharField(max_length=2, choices=PROFILE_LEG)
    level = models.DecimalField(max_digits=2,decimal_places=1)


    def __unicode__(self):
        return unicode(self.name)

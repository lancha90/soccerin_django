#encoding:utf-8
from django.db import models
from django import forms
import datetime

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

FIVE = 5
SEVEN = 7
ELEVEN = 11

FIELD_CAPACITY = (
    (FIVE, 'Cinco - 5'),
    (SEVEN, 'Siete - 7'),
    (ELEVEN, 'Once - 11'),
)

class Administrator(models.Model):

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):
        return unicode(self.name)

# Usuarios registrados en la aplicacion.
class User(models.Model):

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    position = models.CharField(max_length=2, choices=POSITION_FOOTBAL)
    ranking = models.DecimalField(max_digits=2,decimal_places=1)
    old = models.DateField()
    profile = models.CharField(max_length=2, choices=PROFILE_LEG)
    level = models.DecimalField(max_digits=2,decimal_places=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s  - %s' % (self.name,self.username)

    def natural_key(self):
        return '%s  - %s' % (self.name,self.username)

#Canchas de futbol registradas en la aplicacion
class Field(models.Model):

    administrator = models.ForeignKey(Administrator)
    name = models.CharField(max_length=50)
    cost = models.FloatField()
    latitud = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    image = models.CharField(max_length=250)
    capacity = models.IntegerField(choices=FIELD_CAPACITY)

    def __unicode__(self):
        return unicode(self.name)

    def natural_key(self):
        return '%s  - %s' % (self.name,self.cost)

#Partidos programados por los usuarios en la plataforma
class Event(models.Model):

    user = models.ForeignKey(User)
    field = models.ForeignKey(Field)
    date = models.DateTimeField()
    duration = models.DecimalField(max_digits=3,decimal_places=2)

    def __unicode__(self):
        return 'Usuario: %s  Fecha: %s' % (self.user.username, self.date)

#Equipos registrados en la plataforma
class Team(models.Model):
    
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=250)
    description = models.TextField()
    manage = models.ForeignKey(User)

    def __unicode__(self):
        return '%s' % (self.name)
    def natural_key(self):
        return '%s' % (self.name)
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
    email = models.EmailField()
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    timestamp = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.name)

# Usuarios registrados en la aplicacion.
class User(models.Model):
    email = models.EmailField()
    level = models.DecimalField(max_digits=2,decimal_places=1)
    name = models.CharField(max_length=50)
    old = models.DateField()
    password = models.CharField(max_length=128)
    position = models.CharField(max_length=2, choices=POSITION_FOOTBAL)
    profile = models.CharField(max_length=2, choices=PROFILE_LEG)
    ranking = models.DecimalField(max_digits=2,decimal_places=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s  - %s' % (self.name,self.username)

    def natural_key(self):
        return '%s  - %s' % (self.name,self.username)

#Canchas de futbol registradas en la aplicacion
class Field(models.Model):
    address = models.CharField(max_length=50)
    administrator = models.ForeignKey(Administrator)
    capacity = models.IntegerField(choices=FIELD_CAPACITY)
    cost = models.FloatField()
    image = models.CharField(max_length=250)
    latitud = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.name)

    def natural_key(self):
        return '%s  - %s' % (self.name,self.cost)

#Partidos programados por los usuarios en la plataforma
class Event(models.Model):
    date = models.DateTimeField()
    duration = models.DecimalField(max_digits=3,decimal_places=2)
    field = models.ForeignKey(Field)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return 'Usuario: %s  Fecha: %s' % (self.user.username, self.date)

#Equipos registrados en la plataforma
class Team(models.Model): 
    description = models.TextField()
    image = models.CharField(max_length=250)
    manage = models.ForeignKey(User)
    members = models.ManyToManyField(User, related_name='u+')
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' % (self.name)
    def natural_key(self):
        return '%s' % (self.name)

#Mensajes
class Message(models.Model):
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    userfrom = models.ForeignKey(User,related_name='receptor')
    userto = models.ForeignKey(User,related_name='emisor')

    def __unicode__(self):
        return 'TO: %s FROM: %s' % (self.userto,self.userfrom)
    def natural_key(self):
        return 'TO: %s FROM: %s' % (self.userto,self.userfrom)

#Mensajes
class Friend(models.Model):
    friends = models.ManyToManyField(User, related_name='userfriends')
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,related_name='person')

    def __unicode__(self):
        return '%s' % (self.user)
    def natural_key(self):
        return '%s' % (self.user)

#Clasificados
class Advertising(models.Model):
    description = models.TextField()
    image = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return '%s' % (self.user)
    def natural_key(self):
        return '%s' % (self.user)
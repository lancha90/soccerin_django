from api.models import *
import hashlib
from django.http import HttpResponse
from django.core import serializers
from django.utils import simplejson as json
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

def get_all_user(request):
    print request.method
    users = User.objects.filter(username='lancha90').values('name','email')
    data = json.dumps(list(users))
    return HttpResponse(data, mimetype='application/json')

# funcion encargada de realizar el login de usuario
@csrf_exempt
def get_info_user(request):
    if request.method == 'POST':
    	print request.POST
        users = User.objects.filter(username=request.POST['username'],password=request.POST['passwd']).values('name','email','position','level','ranking','profile')
        if users.count() == 1:
            data = json.dumps(list(users))
            return HttpResponse(data, mimetype='application/json')
        else:
            raise Http404
    else:
        raise Http404

#funcion encargada de adicionar un usuario
@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        
        user = User()
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.position = request.POST['position']
        user.ranking = request.POST['ranking']
        user.old = request.POST['old']
        user.profile = request.POST['profile']
        user.level = request.POST['level']
        user.save()

        data = json.dumps({'username':user.username,'email':user.email})
        return HttpResponse(data, mimetype='application/json')
    else:
        return Http404


#funcion encargada adicionar un evento
@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        event = Event()
        event.user = User.objects.get(email=request.POST['user'])
        event.field = Field.objects.get(name=request.POST['field'])
        event.date = request.POST['date']
        event.duration = request.POST['duration']
        event.save()

        data = json.dumps({'user':event.user.email,'field':event.field.name})
        return HttpResponse(data, mimetype='application/json')

    else:
        raise Http404

#funcion encargada de listar los ultimos 20 eventos propios
@csrf_exempt
def get_my_event(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email'])
        events = Event.objects.filter(user=user).order_by('date')[:10]
        data = serializers.serialize('json', events,use_natural_keys=True)
        return HttpResponse(data, mimetype='application/json')
    else:
        raise Http404

#funcion encargada de listar los ultimos 20 eventos
@csrf_exempt
def get_all_event(request):
    if request.method == 'GET':
        data = serializers.serialize('json', Event.objects.all().order_by('date')[:20],use_natural_keys=True)
        return HttpResponse(data, mimetype='application/json')
    else:
        raise Http404

#Funcion encargada de listar todos los campos que existen en la plataforma
@csrf_exempt
def get_all_field(request):
    if request.method == 'GET':
        fields = Field.objects.all().order_by('id')[:20]
        data = serializers.serialize('json', fields,use_natural_keys=True)
        return HttpResponse(data, mimetype='application/json')
    else:
        raise Http404


#funcion encargada adicionar un evento
@csrf_exempt
def add_team(request):
    if request.method == 'POST':
        team = Team()
        team.manage = User.objects.get(email=request.POST['user'])
        team.name = request.POST['name']
        team.description = request.POST['description']
        team.save()

        data = json.dumps({'user':team.user.email,'name':team.field.name})
        return HttpResponse(data, mimetype='application/json')

    else:
        raise Http404

#Funcion encargada de listar todos los equipos que existen en la plataforma
@csrf_exempt
def get_all_team(request):
    if request.method == 'GET':
        fields = Team.objects.all().order_by('name')[:20]
        data = serializers.serialize('json', fields,use_natural_keys=True)
        return HttpResponse(data, mimetype='application/json')
    else:
        raise Http404

#funcion encargada de listar los ultimos 20 eventos propios
@csrf_exempt
def get_my_team(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email'])
        events = Team.objects.filter(manage=user).order_by('name')[:10]
        data = serializers.serialize('json', events,use_natural_keys=True)
        return HttpResponse(data, mimetype='application/json')
    else:
        raise Http404
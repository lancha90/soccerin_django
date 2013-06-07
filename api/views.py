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
        #users = User.objects.filter(username=request.POST['username'],password=request.POST['passwd']).values('name','email','ranking','level','position','profile')
        users = User.objects.filter(username=request.POST['username'],password=request.POST['passwd']).values('name','email','position','profile')
        if users.count() == 1:
            data = json.dumps(list(users))
            return HttpResponse(data, mimetype='application/json')
        else:
            raise Http404
    else:
        raise Http404

#funcion encargada de actualizar la informacion de un usuario
@csrf_exempt
def update_info_user(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.POST['username'])
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.password = request.POST['passwd']
        user.position = request.POST['position']
        user.save()
        return HttpResponse('user', mimetype='application/json')
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
        user.ranking = '5.0'
        user.old = '1990-05-27'
        user.profile = 'AD'
        user.level = request.POST['level']       
        user.save()
        data = json.dumps([{'code':200}])
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
        events = Team.objects.filter(members=user).order_by('name')[:10]
        data = serializers.serialize('json', events,use_natural_keys=True)
        return HttpResponse(data, mimetype='application/json')
    else:
        raise Http404

#funcion encargada adicionar un jugador a un equipo
@csrf_exempt
def add_user_team(request):
    if request.method == 'POST':
        team = Team.objects.filter(name=request.POST['team'])
        user = User.objects.filter(username=request.POST['user'])
        team[0].members.add(user[0])
        data = serializers.serialize('json', team,use_natural_keys=True)
        return HttpResponse(data, mimetype='application/json')

    else:
        raise Http404


#funcion encargada de listar los ultimos 20 equipo de un usuario
@csrf_exempt
def get_team(request):
    if request.method == 'GET':
        print request.POST
        user = User.objects.filter(email='dherrera@ethgf.com')
        events = Team.objects.filter(members=user).order_by('name')[:10]
        data = serializers.serialize('json', events,use_natural_keys=True)
        return HttpResponse(data, mimetype='application/json')
    else:
        raise Http404

#funcion encargada de listar la totalidad de amigos
@csrf_exempt
def get_user_friends(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.POST['username'])
        friend = Friend.objects.filter(user=user).order_by('timestamp')
        data = serializers.serialize('json', friend,use_natural_keys=True)
        return HttpResponse(data, mimetype='application/json')
    else:
        raise Http404

#funcion encargada de adicionar un usuario a la lista de amigos
@csrf_exempt
def add_user_friend(request):
    if request.method == 'POST':
        user = Friend.objects.get(user=User.objects.get(username=request.POST['username']))
        friend = User.objects.get(username=request.POST['friend'])
        user.friends.add(friend);
        return HttpResponse('{code:200}', mimetype='application/json')
    else:
        raise Http404

#funcion encargada de listar los ultimos 10 mensajes que llegaron
@csrf_exempt
def get_user_message(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.POST['username'])
        message = Message.objects.filter(userto=user).order_by('timestamp')[:10]
        data = serializers.serialize('json', message,use_natural_keys=True)
        return HttpResponse(data, mimetype='application/json')
    else:
        raise Http404

#funcion encargada de listar los ultimos 10 mensajes que llegaron
@csrf_exempt
def add_user_message(request):
    if request.method == 'POST':
        userto = User.objects.get(username=request.POST['to'])
        userfrom = User.objects.get(username=request.POST['from'])
        message = Message()
        message.userto = userto
        message.userfrom = userfrom
        message.body = request.POST['body']
        message.save()
        return HttpResponse('{code:200}', mimetype='application/json')
    else:
        raise Http404
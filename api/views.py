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

@csrf_exempt
def get_info_user(request):
    
    print request.method

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
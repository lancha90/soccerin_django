from api.models import *
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def get_all_user(request):
    users = User.objects.filter(username='lancha90')
    data = serializers.serialize('json', users)
    return HttpResponse(data, mimetype='application/json')
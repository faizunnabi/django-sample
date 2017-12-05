from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import SearchData
import os
# Create your views here.


def index(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'data.txt')
    f=open(file_path)
    json_string=f.read()
    f.close()
    data = json.loads(json_string)
    print(data)
    items = []
    for item in data['business']:
        print(item)
        dt = dict()
        dt['id'] = item['id']
        dt['name'] = item['name']
        SearchData.objects.create(id=dt['id'], name=dt['name'])
    return HttpResponse("Data updated successfully !")


#def search(request, q):
  #  pass

#generics is used to create views with HTTP response
from rest_framework import generics
from .models import Worker
from .serializers import WorkerSerializer
from django.shortcuts import render 
from django.http import HttpResponse ,request

import json
 

class Workers(generics.CreateAPIView):
    worker_data = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkerListView(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


# def new(request):
#     if request.method == 'POST': 
#         #try:
#         worker = request.POST.get('worker') 
#             #count+=1
#         #except:
#             #worker = 'john'
    
        
    
#     worker_data = Worker.objects.get(name = worker)
#     worker_age = worker_data.age
#     context = {  
#             'name': worker_data.name ,
#             'age' : worker_age  ,

#         }
    
 
#     return render(request, 'home.html', context)   
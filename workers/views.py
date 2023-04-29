#generics is used to create views with HTTP response
from rest_framework import generics
from .models import Worker
from .serializers import WorkerSerializer
from django.shortcuts import render 
from django.http import HttpResponse ,request

#view to create a worker
class Workers(generics.CreateAPIView):
    worker_data = Worker.objects.all()
    serializer_class = WorkerSerializer

#view to get all workerslist
class WorkerListView(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

#to display all the data on a webpage
def display_workers(request):
   
    workers = Worker.objects.all()
    context = {'workers': workers}
    return render(request, 'index.html', context)


#generics is used to create views with HTTP response
#making necessary imports
from rest_framework import generics
from .models import Worker
from .serializers import WorkerSerializer
from django.shortcuts import render 
from django.http import HttpResponse ,request,StreamingHttpResponse
import cv2

#view to create a worker
class Workers(generics.CreateAPIView):
    worker_data = Worker.objects.all()
    serializer_class = WorkerSerializer

#view to get all workerslist
class WorkerListView(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

def index(request):
    return render(request,"content.html")

#to display all the data on a webpage
def display_workers(request):
   
    workers = Worker.objects.all()
    context = {'workers': workers}
    return render(request, 'index.html', context)


#generate frames for the video stream
def generate_frames():
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#displays video feed only
def video_feed(request):
     return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame') 
 
#displays video feed and worker details
def stream(request):
    workers = Worker.objects.all()
    context = {'workers': workers}
    return render(request,'live_feed.html',context)
"""worker_safety URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from workers.views import Workers, WorkerListView,display_workers,video_feed,index,stream
urlpatterns = [
    path("",index,name=""),
    path('admin/', admin.site.urls),
    path('workers/', WorkerListView.as_view(), name='worker_list'),
    path('workers/create/', Workers.as_view(), name='worker_create'),
    path('display_workers/', display_workers, name = 'display_workers'),
    #display just the video
    path('video_feed', video_feed, name='video_feed'),
    
    #display video with data of the workers
    path('stream/', stream, name='stream')
   
]

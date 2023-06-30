from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def form(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse("Data is submitted")

    return render(request,'form.html')


def insert_topic_data(request):
    
    if request.method=='POST':
        topic=request.POST['tn']

        CTO=Topic.objects.get_or_create(topic_name=topic)[0]
        CTO.save()
        HTO=Topic.objects.get_or_create(topic_name=topic)[0]
        HTO.save()
        VBO=Topic.objects.get_or_create(topic_name=topic)[0]
        VBO.save()
        FBO=Topic.objects.get_or_create(topic_name=topic)[0]
        FBO.save()
        KTO=Topic.objects.get_or_create(topic_name=topic)[0]
        KTO.save()
        
        
        return HttpResponse("Topic data insertion is successfully done")




    return render(request,'insert_topic_data.html')


def insert_webpage(request):
    if request.method=='POST':
        topic=request.POST['tn']
        name=request.POST['name']
        url=request.POST['ul']

        TO=Topic.objects.get(topic_name=topic)
        

        WPO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WPO.save()       
        
        print(topic)
        print(name)
        print(url)
        
        return HttpResponse("Webpage table inserion is successfully done")


    return render(request,'insert_webpage.html')




def insert_accessrecord(request):

    if request.method=='POST':
        topic=request.POST['tn']
        name=request.POST['name']
        date=request.POST['dt']
        author=request.POST['ar']


        CTO=Topic.objects.get(topic_name=topic)
        CTO.save()

        WPO=Webpage.objects.get_or_create(topic_name=CTO,name=name)[0]
        WPO.save()
        
        ARO=AccessRecord.objects.get_or_create(name=WPO,date=date,author=author)[0]
        ARO.save()

        return HttpResponse("insertion of Accessrecord model is done")



    return render(request,'insert_accessrecord.html')
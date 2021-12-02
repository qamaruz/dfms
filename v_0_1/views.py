from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from v_0_1.models import data
from django.contrib.auth.models import User
from django.core import serializers
import simplejson
import urllib
import json
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# Create your views here.


url='/v_0_1/'



def getData(request):
    if request.user.is_authenticated():
        ad= data.objects.all().order_by('date')
        ad1= [(str(d.date), d.cm, d.inch,d.time, d.sensorDate,d.firstLevel,d.secondLevel,d.thirdLevel,d.arduinoid) for d in ad]
        rad1= list(reversed(ad1))
        return JsonResponse(rad1 ,safe=False)
        
def openData(request):
    ad= data.objects.all().order_by('date')
    ad1= [(str(d.date), d.cm, d.inch,d.time, d.sensorDate,d.firstLevel,d.secondLevel,d.thirdLevel,d.arduinoid) for d in ad]
    rad1= list(reversed(ad1))
    return JsonResponse(rad1 ,safe=False)
        
def getPlotData(request):
    if request.user.is_authenticated():
        ad= data.objects.all()
        ad1= [(str(d.date), d.cm, d.inch,d.time, d.sensorDate,d.firstLevel,d.secondLevel,d.thirdLevel,d.arduinoid) for d in ad]
        return JsonResponse(ad1 ,safe=False)        


def getSensorData(request):
    if request.user.is_authenticated():
        url="http://qamaruzyun.local/data/get"
        response = urllib.urlopen(url)
        sensorData = json.loads(response.read())
        print sensorData
        d=data()
        d.cm=sensorData['value']['cm']
        d.inch=sensorData['value']['inches']
        d.sensorDate=sensorData['value']['date']
        d.time=sensorData['value']['date'][11:19]
        d.firstLevel = sensorData['value']['firstLevel']
        d.secondLevel = sensorData['value']['secondLevel']
        d.thirdLevel = sensorData['value']['thirdLevel']
        d.arduinoid = sensorData['value']['deviceid']
        d.save()
        obj = data.objects.latest('id')
        obj1= [(str(obj.date), obj.cm, obj.inch,obj.time, obj.sensorDate,obj.firstLevel,obj.secondLevel,obj.thirdLevel,obj.arduinoid)]
    
        return JsonResponse(obj1,safe=False)

def getRealSensorData(request):
    if request.user.is_authenticated():
        url="http://qamaruzyun.local/data/get"
        response = urllib.urlopen(url)
        sensorData = json.loads(response.read())
        print sensorData
        firstLevel = sensorData['value']['firstLevel']
        secondLevel = sensorData['value']['secondLevel']
        thirdLevel = sensorData['value']['thirdLevel']
    
        real = [(firstLevel,secondLevel,thirdLevel)]
        return JsonResponse(real, safe=False )

def hazardMap(request):
    if request.user.is_authenticated():
        url="http://qamaruzyun.local/data/get"
        response = urllib.urlopen(url)
        sensorData = json.loads(response.read())
        firstLevel = sensorData['value']['firstLevel']
        secondLevel = sensorData['value']['secondLevel']
        thirdLevel = sensorData['value']['thirdLevel']
        long = '114.67232912778854'
        lat =   '4.718136002726354'
        real = [(firstLevel,secondLevel,thirdLevel,long,lat)]
        return JsonResponse(real, safe=False )        

def checkSensor(request):
    if request.user.is_authenticated():
        url="http://qamaruzyun.local/data/get"
        
        try:
            response = urllib.urlopen(url)
            state='on'
        except IOError:
            state='off'
        return JsonResponse(state, safe=False )

def sendEmail(request):
    if request.user.is_authenticated():
        fromaddr = "cerenet.tech@gmail.com"
        toaddr = "qamaruz.affandy@gmail.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "WARNING WATER LEVEL RISING"
        
        body = "WARNING WARNING WARNING"
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "Brune1234")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        
        status='sent'
        return JsonResponse(status, safe=False )  

def getWeather(request):
    if request.user.is_authenticated():

        return JsonResponse(status, safe=False )             
    
    return 
@login_required(login_url=url)
def main(request):
    if request.user.is_authenticated():
        return render(request, 'v_0_1/main.html')

@login_required(login_url=url)
def sensorList(request):
    if request.user.is_authenticated():
        return render(request, 'v_0_1/newSensorStatus.html')        

@login_required(login_url=url)
def dataLog(request):
    if request.user.is_authenticated():
        return render(request, 'v_0_1/dataLog.html')    

@login_required(login_url=url)
def realTime(request):
    if request.user.is_authenticated():
        return render(request, 'v_0_1/realTime.html')            
        
def logout(request):
    auth.logout(request)
    return render_to_response('v_0_1/logout.html')        

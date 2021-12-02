from django.conf.urls import *
import v_0_1.views
from django.core.urlresolvers import reverse
from django.contrib.auth import views 
# Create your views here.

urlpatterns = [
   url(r'^$', views.login , {'template_name':'v_0_1/login.html', 'extra_context':{'next': 'main/'} }  ),

   #pages
    url(r'^main/$', v_0_1.views.main),
    url(r'^sensorlist/$', v_0_1.views.sensorList),
    url(r'^logout/$', v_0_1.views.logout),
    url(r'^datalog/$', v_0_1.views.dataLog),
    url(r'^realtime/$', v_0_1.views.realTime),
    
    #getData
    url(r'^getData/$', v_0_1.views.getData),
    url(r'^getSensorData/$', v_0_1.views.getSensorData),
    url(r'^getRealTimeData/$', v_0_1.views.getRealSensorData),
    url(r'^forHazardMap/$', v_0_1.views.hazardMap),
    url(r'^getPlotData/$', v_0_1.views.getPlotData),    
    url(r'^checkSensor/$', v_0_1.views.checkSensor),    
    url(r'^openData/$', v_0_1.views.openData),
    url(r'^getWeather/$', v_0_1.views.getWeather),        
    
    #action
     url(r'^sendEmail/$', v_0_1.views.sendEmail),
    
    ]

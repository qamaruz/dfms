from django.core.management.base import BaseCommand, CommandError
import urllib
import json
count=0
while(count==0):
    url="http://qamaruzyun.local/data/get"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    print data
#walrus operator is used to crub out unwsnted variables that are defined in code
#this helps to avoid repetition and reduce the lines of code
#it can also be used to debug the code to see if any particular line is running or not

from math import asin,cos,radians,sin,sqrt
import requests
import urllib.parse

radi = 6371

def distance(lat1,lon1,lat2,lon2):
    lat1,lon1,lat2,lon2 = map(radians,[float(lat1),float(lon1),float(lat2),float(lon2)])
    distance = 2 * radi * asin(pos:=sqrt(sin((lat2-lat1)/2)**2 + cos(lat1) * cos(lat2) * sin((lon2-lon1)/2)**2))
    return distance

def getaddr(address):
    url = 'https://nominatim.openstreetmap.org/search/' + (y:=urllib.parse.quote(address)) +'?format=json'
    response = requests.get(url).json()
    return response[0]["lat"],response[0]["lon"]

if __name__ == '__main__':
    x = getaddr(a:=input("Enter the start: "))
    y = getaddr(b:=input("Enter the destination: "))
    print("distance from {} to {} is {} km".format(a,b,distance(x[0],x[1],y[0],y[1])))
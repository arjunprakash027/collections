import requests

url = "https://quest.squadcast.tech/api/310620243005/weather/get"

city_name_1 = "Pune"
city_name_2 = "Gujarat"

def gettemp(city_name):
    r = requests.get(url,params={'q':city_name}) 
    data = r.json()

    print(data)

gettemp(city_name_1) #found out that pune is less cloudy than gujarat from the output
gettemp(city_name_2)





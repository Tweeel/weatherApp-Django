from django.shortcuts import render, redirect
import json
import urllib.request
from datetime import datetime, timezone
from django.contrib import messages
import geocoder


# Create your views here.
# def index(request):
#     if request.method == "POST":
#         city = request.POST['city']
#         api_key = '79559d6ecbdfba0abe47a0372ddeed86'
#         try:
#             res = urllib.request.urlopen(
#                 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key).read()
#         except:
#             messages.info(request, 'City not found')
#             return redirect('index')
#         json_data = json.loads(res)
#         time = datetime.fromtimestamp(int(json_data['dt']) + int(json_data['timezone']), tz=timezone.utc)
#         time_formated = time.strftime('%A, %d %I:%M %p')
#         icon = 'http://openweathermap.org/img/w/' + json_data['weather'][0]['icon'] + '.png'
#         data = {
#             "city": str(json_data['name']),
#             "description": str(json_data['weather'][0]['description']),
#             "temp": str(round(json_data['main']['temp'] - 273.15, 2)),
#             "wind_speed": str(json_data['wind']['speed']),
#             "humidity": str(json_data['main']['humidity']),
#             "pressure": str(json_data['main']['pressure']),
#             "time": str(time_formated),
#             "icon": str(icon),
#         }
#     else:
#         city = ''
#         data = {}
#     return render(request, "index.html", data)


def index(request):
    if request.method == "POST":
        city = request.POST['city']
    else:
        # get the current location using IP address
        g = geocoder.ip('me')
        # get the city name
        city = g.city
    api_key = '79559d6ecbdfba0abe47a0372ddeed86'
    try:
        res = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key).read()
    except:
        messages.info(request, 'City not found')
        return redirect('index')
    json_data = json.loads(res)
    time = datetime.fromtimestamp(int(json_data['dt']) + int(json_data['timezone']), tz=timezone.utc)
    time_formated = time.strftime('%A, %d %I:%M %p')
    icon = 'https://openweathermap.org/img/w/' + json_data['weather'][0]['icon'] + '.png'
    data = {
        "city": str(json_data['name']),
        "description": str(json_data['weather'][0]['description']),
        "temp": str(round(json_data['main']['temp'] - 273.15, 2)),
        "wind_speed": str(json_data['wind']['speed']),
        "humidity": str(json_data['main']['humidity']),
        "pressure": str(json_data['main']['pressure']),
        "time": str(time_formated),
        "icon": str(icon),
    }
    return render(request, "index.html", data)
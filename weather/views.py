

import requests
from django.shortcuts import render,redirect
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=2e37fd2364d867821f298280137eecc0'

    cities = City.objects.all()

    err_msg = ''
    message = ''
    message_class= ""

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            exist_city = City.objects.filter(name=new_city).count()
            if exist_city==0:
                r = requests.get(url.format(new_city)).json()
                if r['cod']==200:
                    form.save()
                else:
                    err_msg = f'{new_city} not found in the world'

            else:
                err_msg=f'{exist_city}already exists in Database'
        
        if err_msg:
            message=err_msg
            message_class='is-danger'
        else:
            message=f'{new_city} added Successfully !'
            message_class='is-success'


    form = CityForm()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' :float("{0:.2f}".format((r['main']['temp']-32)* 5/9)),
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            'country':r['sys']['country']
        }

        weather_data.append(city_weather)

    context = {'weather_data':weather_data,
               'form': form,
               'message':message,
               'message_class':message_class}

    return render(request,'weather/weather.html',context)

    

def delete_city(request,city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')
#  (r['main']['temp']-32)* 5/9,


import requests
from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def get_weather(city):
    # Your OpenWeatherMap API key
    api_key = 'c4f8ed272caa68e2d07059803591e452'
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Get the weather data
    response = requests.get(base_url)
    data = response.json()
    
    # Check if the request was successful
    if data["cod"] == 200:
        main = data["main"]
        weather = data["weather"][0]
        temp = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]
        
        # Create a dictionary to store the weather data
        weather_data = {
            "city": city,
            "temperature": temp,
            "pressure": pressure,
            "humidity": humidity,
            "description": description,
        }
        return weather_data
    else:
        return None

def home(request):
    
    city = 'Nairobi'
    
    if request.method == 'POST':
        city = request.POST['city']
    
    # Get the weather data
    weather_data = get_weather(city)
    
    if weather_data:
        return render(request, 'home.html', {'weather': weather_data})
    else:
        return HttpResponse("City not found!")


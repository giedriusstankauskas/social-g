from django.shortcuts import render
import requests

# Create your views here.

something = "some Text"

def weather_app(request):
    api_key = "b308b202b15b9f5a0867ea98aafbe002"
    city = "Vilnius"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    r = requests.get(url).json()

    city_weather = {
        "city": city,
        "temperature": r['main']['temp'],
        "description": r['weather'][0]['description'],
        "icon": r['weather'][0]['icon'],
    }

    context = {"city_weather": city_weather}
    return render(request, "weather/weather.html", context)



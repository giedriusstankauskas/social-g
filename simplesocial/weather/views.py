from django.shortcuts import render
import requests


def weather_app(request):
    api_key = "b308b202b15b9f5a0867ea98aafbe002"
    cities = [
        "Vilnius", "Antarctica", "London", "Paris", "Tokyo",
        "Sydney", "Mumbai", "Malibu", "Nuuk", "Kyiv",
        "Johannesburg", "Lima", "Juneau", "Yakutsk", "Oymyakon"
    ]

    weather_data = []

    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        r = requests.get(url).json()

        city_weather = {
            "city": city,
            "temperature": r['main']['temp'],
            "description": r['weather'][0]['description'],
            "icon": r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {"weather_data": weather_data}
    return render(request, "weather/weather.html", context)



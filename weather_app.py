import requests

api_key = 'ae52e357746120cfdba88061c1af96d6'

def get_weather(city):
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        return None
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        description = weather_data.json()['weather'][0]['description']
        icon_code = weather_data.json()['weather'][0]['icon']
        return {'weather': weather, 'temp': temp, 'description': description,'icon_code': icon_code }



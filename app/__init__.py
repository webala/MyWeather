import requests
from flask import Flask, request, render_template, jsonify
from flask_bootstrap import Bootstrap
from datetime import time



app = Flask(__name__)

bootstrap = Bootstrap(app)


app.config['SECRET_KEY'] = 'gangingemblainningekujanandenga'
open_weather_api_key = '41548eb1b16f86e5f5763b90d344cecd'
open_weather_api_endpoint = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

@app.route('/', methods=['POST', 'GET'])
def index():
    time_now = time
    print(time_now)
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    
    city = request.json['region']
    response = {}
    req = requests.get(open_weather_api_endpoint.format(city, open_weather_api_key))
    print(city, req.text)

    response = req.json()
    print (response['cod'])
    if response['cod']:
        if int(response['cod']) == 404:
            return jsonify ({'message': "region not found"}), 404

        elif int(response['cod']) == 200:

            main_weather = response['weather'][0]['main']
            weather_description = response['weather'][0]['description']
            temperature = response['main']['temp']
            temperature_min = response['main']['temp_min']
            temperature_max = response['main']['temp_max']
            humidity = response['main']['humidity']
            pressure = response['main']['pressure']
            visibility = response['visibility']
            wind_speed = response['wind']['speed']
            wind_degrees = response['wind']['deg']
            country = response['sys']['country']
            region = response['name']

            print(
                'main_weather', main_weather, '\n',
                'weather_description', weather_description, '\n',
                'temperature', temperature, '\n',
                'temperature_min', temperature_min, '\n',
                'temperature_max', temperature_max, '\n',
                'humidity', humidity, '\n',
                'pressure', pressure, '\n',
                'visibility', visibility, '\n',
                'wind_speed', wind_speed, '\n',
                'wind_degrees', wind_degrees, '\n',
                'country', country, '\n',
                
                )
            weather_data = {
                        'main_weather': main_weather, 
                        'weather_description': weather_description, 
                        'temperature': temperature, 
                        'temperature_min': temperature_min, 
                        'temperature_max': temperature_max, 
                        'humidity': humidity, 
                        'pressure': pressure,
                        'visibility': visibility, 
                        'wind_speed': wind_speed, 
                        'wind_degrees': wind_degrees, 
                        'country': country,
                        'region': region
                        }
            

            return jsonify(weather_data), 200



'''
| app.py is a Dynamic weather application where users c respective personal information.
|
| Project Name : Dynamic Weather App
| Developed by : BroTecs Technologies Limited
| created      : May 24, 2021 
| updated      : May 27, 2021 [Md.Rajib Hawlader]
|
| For any query and suggestion please contact at rajib104.ewubd@gmail.com
|
'''
# importing required modules 
from flask.helpers import url_for
import requests
import json
import time
from flask import Flask,jsonify,render_template,request, redirect
# Creating Flask app instance
app = Flask(__name__)
# creating route for index page
@app.route('/')
# Function to render template
# Input parameter: void
# Return parameter: jinja2 Template
def index():
    return render_template("index.html")
    
    
@app.route('/city', methods=['POST'])
def city():
    # collecting value of city from form
    city = request.form.get('key')
   # Error Handling 
    try:
        # Fetching API
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid={API KEY HERE - HIDDEN FOR SECURITY}"
        json_data = requests.get(api).json()
        # storing specific data of fetched Api inside specific variables 
        condition = json_data['weather'][0]['main']
        temprature = int(json_data['main']['temp'] - 273.15)
        minimumTemprature = int(json_data['main']['temp_min'] - 273.15)
        maximumTemprature = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        windSpeed = json_data['wind']['speed']
        sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']-21600))
        sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']-21600))
        return render_template("index.html",city = city,condition = condition,temprature=temprature,minimumTemprature = minimumTemprature,maximumTemprature = maximumTemprature,pressure = pressure, humidity = humidity,windSpeed = windSpeed, sunset = sunset, sunrise = sunrise)

        
    
    except Exception as e:
        print('Exception Occurred! Exception Type: ', type(e).__name__)
        return render_template("error.html")

# Running the App
if __name__ == "__main__":
    app.run()


  

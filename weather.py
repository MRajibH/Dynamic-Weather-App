import tkinter as tk
from typing import Text
import requests
import time
def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=fb2afc17357e7d8adb50eb7b7e9348ed"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temprature = int(json_data['main']['temp'] - 273.15)
    minimumTemprature = int(json_data['main']['temp_min'] - 273.15)
    maximumTemprature = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    windSpeed = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']-21600))
    sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']-21600))
    final_info = condition + "\n" + str(temprature) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(minimumTemprature) + "°C" + "\n" + "Max Temp: " + str(maximumTemprature) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(windSpeed) + " km/h\n" + "Sunrise: " + sunrise + " AM\n" + "Sunset: " + sunset +' PM'
    labelOne.config(text = final_info)
    labelTwo.config(text = final_data)
# creating canvas
canvas = tk.Tk() 
canvas.geometry('600x500')
canvas.title('Weather App')

fontPrimary = ("cambria",15,"bold")
fontNew = ("cambria", 35, "bold")
textField = tk.Entry(canvas, justify = "center",  font = fontNew)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)
labelOne = tk.Label(canvas, font  = fontNew)
labelOne.pack()
labelTwo = tk.Label(canvas, font  = fontNew)
labelTwo.pack()
canvas.mainloop()
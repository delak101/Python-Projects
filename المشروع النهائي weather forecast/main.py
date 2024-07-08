import tkinter as tk
import requests

def search():
    #api
    location = location_entry.get()
    api_key = "27cece8b914d75d19891a17661d06be7"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    payload={}
    headers={
    "apikey": "27cece8b914d75d19891a17661d06be7"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    if status_code != 200:
        error_label.config(text=f"Status code: {response.status_code}\nThere was a problem. Please try again later.")
    else:
        data = response.json()
        temperature = data["main"]["temp"] - 273.15 #degree in kelvin - 273.15 = degree in celsius
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        precipitation = 0 #data not available
        
        temperature_label.config(text=f"Temperature: {temperature:.2f} °C")
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_speed_label.config(text=f"Wind Speed: {wind_speed} m/s")
        pressure_label.config(text=f"Pressure: {pressure} hPa")
        precipitation_label.config(text=f"Precipitation: {precipitation}%")


#main
window = tk.Tk()
window.title("Weather Forecast")
window.minsize(width=300, height=250)

#labels
location_label = tk.Label(window, text="Location:")
location_entry = tk.Entry(window)
search_button = tk.Button(window, text="Search", command=search)

temperature_label = tk.Label(window, text="Temperature: .. °C")
humidity_label = tk.Label(window, text="Humidity: .. %")
wind_speed_label = tk.Label(window, text="Wind Speed: .. Km/h")
pressure_label = tk.Label(window, text="Pressure: .. hPa")
precipitation_label = tk.Label(window, text="Precipitation: .. %")
error_label = tk.Label(window, text="")

#layout
location_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
location_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
search_button.grid(row=0, column=2, padx=10, pady=5, sticky="w")

temperature_label.grid(column=0, row=1, columnspan=3, padx=10, pady=5, sticky="w")
humidity_label.grid(column=0, row=2, columnspan=3, padx=10, pady=5, sticky="w")
wind_speed_label.grid(column=0, row=3, columnspan=3, padx=10, pady=5, sticky="w")
pressure_label.grid(column=0, row=4, columnspan=3, padx=10, pady=5, sticky="w")
precipitation_label.grid(column=0, row=5, columnspan=3, padx=10, pady=5, sticky="w")
error_label.grid(column=0, row=6, columnspan=3, padx=10, pady=5, sticky="w")


window.mainloop()
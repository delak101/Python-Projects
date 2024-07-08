import tkinter as tk
import requests

def search():
    location = location_entry.get()
    if not location:
        error_label.config(text="Please enter a location.")
        return
    
    api_key = "27cece8b914d75d19891a17661d06be7"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        error_label.config(text=f"HTTP error occurred: \n{http_err}")
        return
    except requests.exceptions.RequestException as err:
        error_label.config(text=f"Error: \n{err}")
        return

    data = response.json()
    if response.status_code == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        precipitation = data.get("rain", {}).get("1h", 0)  # Get precipitation if available
        
        temperature_label.config(text=f"Temperature: {temperature:.2f} °C")
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_speed_label.config(text=f"Wind Speed: {wind_speed} m/s")
        pressure_label.config(text=f"Pressure: {pressure} hPa")
        precipitation_label.config(text=f"Precipitation: {precipitation} mm")
        error_label.config(text="")
    else:
        error_label.config(text=f"Error: \n{data.get('message', 'Unknown error')}")

# Main application setup
window = tk.Tk()
window.title("Weather Forecast")
window.minsize(width=300, height=250)

# Labels and entry
location_label = tk.Label(window, text="Location:")
location_entry = tk.Entry(window)
search_button = tk.Button(window, text="Search", command=search)

temperature_label = tk.Label(window, text="Temperature: .. °C")
humidity_label = tk.Label(window, text="Humidity: .. %")
wind_speed_label = tk.Label(window, text="Wind Speed: .. m/s")
pressure_label = tk.Label(window, text="Pressure: .. hPa")
precipitation_label = tk.Label(window, text="Precipitation: .. mm")
error_label = tk.Label(window, text="", fg="red")

# Layout
location_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
location_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
search_button.grid(row=0, column=2, padx=10, pady=5, sticky="w")

temperature_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky="w")
humidity_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky="w")
wind_speed_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky="w")
pressure_label.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky="w")
precipitation_label.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky="w")
error_label.grid(row=6, column=0, columnspan=3, padx=10, pady=5, sticky="w")

window.mainloop()

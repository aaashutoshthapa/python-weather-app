import tkinter as tk
from tkinter import messagebox
import requests

# Example: You should replace this with your actual config import
# from config import API_KEY

API_KEY = "eb6aee074dc448dd1f5ceed7f542b801" # Replace with your actual API key

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            return None
        weather = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "desc": data["weather"][0]["description"].title()
        }
        return weather
    except Exception as e:
        return None

def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    weather = get_weather(city)
    if weather:
        result_label.config(
            text=f"City: {weather['city']}\nTemperature: {weather['temp']}°C\nDescription: {weather['desc']}"
        )
    else:
        result_label.config(text="Could not retrieve weather data.")

root = tk.Tk()
root.title("Simple Weather App")

tk.Label(root, text="Enter City:").pack(pady=5)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=show_weather).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()
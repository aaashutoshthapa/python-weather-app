def display_weather(data):
    print(f"\nWeather in {data['city']}:\n"
          f"Temperature: {data['temperature']}°C\n"
          f"Description: {data['description']}\n"
          f"Humidity: {data['humidity']}%\n"
          f"Wind Speed: {data['wind']} m/s")

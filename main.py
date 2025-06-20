from weather_api import weather_fetch
from utils import display_weather

def main():
    city = input("Enter city name: ")
    data = weather_fetch(city)
    
    if data:
        display_weather(data)
    else:
        print("❌ Could not retrieve weather data. Please check the city name or try again later.")


if __name__ == "__main__":
    main()

from weather_api import weather_fetch
from utils import display_weather

def main():

     while True:
        city = input("Enter city name (or type 'exit' to quit): ")

        if city.lower() == 'exit':
            print("Goodbye!")
            break

        data = weather_fetch(city)
        
        if data:
            display_weather(data)
            break  # Exit loop after successful fetch
        else:
            print("❌ Invalid city or unable to fetch weather. Please try again.\n")

if __name__ == "__main__":
    main()

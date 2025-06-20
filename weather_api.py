import requests
from config import API_KEY, BASE_URL

def weather_fetch(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            return {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"]
            }
        else:
            print(f"Error from API: {data.get('message')}")
            return None
    except Exception as e:
        print("Network or parsing error:", e)
        return None
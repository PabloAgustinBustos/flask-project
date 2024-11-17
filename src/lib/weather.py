from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Kansas City"):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial").json()
    
    return weather_data

if __name__ == "__main__":
    print("\n*** Get current weather conditions ***\n")
    
    city = input("\nEnter a city name: ")

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
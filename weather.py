import requests

API = "https://wttr.in/{}?format=3"

def get_weather(city):
    try:
        res = requests.get(API.format(city))
        if res.status_code == 200:
            return res.text
        return "Error fetching weather"
    except:
        return "Network error"

if __name__ == "__main__":
    city = input("Enter city name: ")
    print(get_weather(city))

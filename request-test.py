import requests
from math import div

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    current = data["current_condition"][0]

    temperature = current["temp_C"]
    humidity = current["humidity"]
    description = current["weatherDesc"][0]["value"]

    print("Weather Report")
    print("--------------------")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", description)

except requests.exceptions.RequestException as error:
    print("Unable to fetch weather:", error)

except (KeyError, IndexError, ValueError):
    print("Unable to process weather information")

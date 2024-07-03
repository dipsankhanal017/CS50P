import requests
import sys

def main():
    print("."*10,"Weather app","."*10)
    cityName = input("City Name: ")
    cityData = getCityData(cityName)
    try:
        temperature = getTemperature(cityData)
        feelsLike = getFeelsLike(cityData)
        humidity = getHumidity(cityData)
        wind = getWind(cityData)
        sky = getSky(cityData)
        pressure = getPressure(cityData)
        visibility = getVisibility(cityData)
    except KeyError:
        print(f"Sorry, This service is not available for the city \"{cityName}\"")
        sys.exit()
    displayData(cityName.capitalize(), temperature, feelsLike, humidity, wind, sky, pressure, visibility)


def getCityData(city):
    api = "b6007cd49b78132081bb0fe2bb51fbc2"
    apiLink = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
    api_link = requests.get(apiLink)
    return api_link.json()

def getTemperature(data):
    return round(data["main"]["temp"] - 273,2)

def getFeelsLike(data):
    return round(data["main"]["feels_like"] - 273,2)

def getHumidity(data):
    return data["main"]["humidity"]

def getWind(data):
    return data["wind"]["speed"]

def getSky(data):
    return data["weather"][0]["description"]
def getPressure(data):
    return round(data["main"]["pressure"] / 1013.25,5)

def getVisibility(data):
    return data["visibility"]

def displayData(cityName, temperature, feelsLike, humidity, wind, sky, pressure, visibility):
    print(f"Weather details for {cityName}: \nTemperature: {temperature}°C\nFeels like: {feelsLike}°C\nHumidity: {humidity}%\nWind: {wind}km/hr\nSky Condition: {sky}\nPressure: {pressure}atm\nVisibility: {visibility}m")

main()

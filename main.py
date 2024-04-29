import requests
# just logic version
def fetchData(cityName):
    url = f"https://api.weatherapi.com/v1/current.json?key=8da9dc3302d94e8b915162620242904&q={cityName}&aqi=no"
    response = requests.get(url)
    weatherData = response.json()
    return weatherData

def displayWeather(weatherData):
    name = weatherData["location"]["name"]
    temperature = weatherData["current"]["temp_c"]
    weather = weatherData["current"]["condition"]["text"]
    wind = weatherData["current"]["wind_kph"]
    humidity = weatherData["current"]["humidity"]
    print(f"Information about: {name}")
    print(f"Weather Type: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Wind: {wind} km/h")
    print(f"Humidity: {humidity}%")
    
def main():
    cityName = input("Enter city name: ")
    wData = fetchData(cityName)
    displayWeather(wData)
main()
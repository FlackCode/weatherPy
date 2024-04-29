import customtkinter
import requests
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

def fetchData(cityName):
    url = f"https://api.weatherapi.com/v1/current.json?key=8da9dc3302d94e8b915162620242904&q={cityName}&aqi=no"
    response = requests.get(url)
    weatherData = response.json()
    return weatherData

def updateWeather(cityNameEntry):
    cityName = cityNameEntry.get()
    weatherData = fetchData(cityName)
    nameLabel.configure(text=f"Information about: {weatherData['location']['name']}")
    conditionLabel.configure(text=f"Weather: {weatherData['current']['condition']['text']}")
    temperatureLabel.configure(text=f"Temperature: {weatherData['current']['temp_c']}°C")
    windLabel.configure(text=f"Wind: {weatherData['current']['wind_kph']} km/h")
    humidityLabel.configure(text=f"Humidity: {weatherData['current']['humidity']}%")

root = customtkinter.CTk()
root.geometry('600x600')
root.title('Weather App')

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=70, padx=60, fill='both', expand=True)

titleLabel = customtkinter.CTkLabel(master=frame, text='Weather App', font=('Roboto', 24))
titleLabel.pack(padx=10, pady=20)

cityNameEntry = customtkinter.CTkEntry(master=frame, placeholder_text='Enter city name...', width=200)
cityNameEntry.pack()

nameLabel = customtkinter.CTkLabel(master=frame, text='', font=('Roboto', 16))
nameLabel.pack()

conditionLabel = customtkinter.CTkLabel(master=frame, text='', font=('Roboto', 16))
conditionLabel.pack()

temperatureLabel = customtkinter.CTkLabel(master=frame, text='', font=('Roboto', 16))
temperatureLabel.pack()

windLabel = customtkinter.CTkLabel(master=frame, text='', font=('Roboto', 16))
windLabel.pack()

humidityLabel = customtkinter.CTkLabel(master=frame, text='', font=('Roboto', 16))
humidityLabel.pack()

searchButton = customtkinter.CTkButton(master=frame, text='Search', command=lambda: updateWeather(cityNameEntry))
searchButton.pack(pady=12, padx=10)

root.mainloop()
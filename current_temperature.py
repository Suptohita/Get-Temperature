from math import ceil
import requests


def weather_data(cityName):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid=ae867b549e569e53fd7e081266ffc15a')
    data = response.json()

    if data['cod'] == 200:
        temperature = ceil(data['main']['temp'] - 273.15)
        return f'Today\'s temperature in {cityName.capitalize()} is {temperature} degrees Celcius.'
    else:
        print('City doesn\'t exist.\n Type 1 or 2: \n\t 1.Try again\n\t 2. Exit')

        command = input('\nYour choice (1) or (2): ')

        if command == '1' or command.lower() == 'try again':
            cityName = input('City name: ')
            return weather_data(cityName)
        elif command == '2' or command.lower() == 'exit':
            return 0
        else:
            print('Wrong Command.\nExiting...')
            return 0


cityName = input('City name: ')
temperature = weather_data(cityName)
print(temperature)

from math import ceil
import requests


def weather_data(city):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ae867b549e569e53fd7e081266ffc15a')
    data = response.json()

    if data['cod'] == 200:
        temperature = ceil(data['main']['temp'] - 273.15)
        return f'Today\'s temperature is {temperature} degree Celcius.'
    else:
        print('City doesn\'t exist')
        print('Type 1 or 2: ')
        print('\t1. Try again\n\t2. Exit')
        command = input('\nYour choice (1) or (2): ')
        if command == '1' or command.lower() == 'try again':
            city = input('City name: ')
            return weather_data(city)
        elif command == '2' or command.lower() == 'exit':
            return ''
        else:
            print('Wrong Command.\nExiting...')
            return ''


city = input('City name: ')
temperature = weather_data(city)
print(temperature)
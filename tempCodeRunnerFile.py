
    # if data['cod'] == 200:
    #     temperature = ceil(data['main']['temp'] - 273.15)
    #     return f'Today\'s temperature is in {cityName} {temperature} degree Celcius.'
    # else:
    #     print('City doesn\'t exist.\n Type 1 or 2: \n\t 1.Try again\n\t 2. Exit')

    #     command = input('\nYour choice (1) or (2): ')

    #     if command == '1' or command.lower() == 'try again':
    #         cityName = input('City name: ')
    #         return weather_data(cityName)
    #     elif command == '2' or command.lower() == 'exit':
    #         return 0
    #     else:
    #         print('Wrong Command.\nExiting...')
    #         return 0
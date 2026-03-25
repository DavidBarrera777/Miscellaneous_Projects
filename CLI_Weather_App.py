import requests
from datetime import datetime, date


#This function is used to get the current date and print it for the user
def show_date():
    today = datetime.now()
    only_date = today.date()
    print(f'Todays date is: {only_date}')


#This function uses the city name to fetch the data from openweathermap
#It takes that data for that respective city the user enters and stores it in data and return it 
def get_weather(city_name):
    API_key = ''
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url  = f"{base_url}q={city_name}&appid={API_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    return data


#This function is used to display the actual information in an organized way
#It parses the nested json data and displays it in a readable format 
def display_weather(data, city_name):
    temperature = ((data['main']['temp']) * 9/5) + 32
    print(f"\nWeather in {city_name.capitalize()}:")
    print(f"Temperature: {temperature:.1f}°F")

    feels_like = ((data['main']['feels_like']) * 9/5) + 32
    print(f"Feels like: {feels_like:.1f}°F")

    max_temp = ((data['main']['temp_max']) * 9/5) + 32
    min_temp = ((data['main']['temp_min']) * 9/5) + 32
    print(f"High: {max_temp:.1f}°F | Low: {min_temp:.1f}°F")

    humidity = data['main']['humidity']
    print(f"Humidity: {humidity}%")

    description = data['weather'][0]['description']
    print(f"Condition: {description.capitalize()}\n")
    return 


#The main function welcomes the user to the application and prompts the user to enter the name
#of the city they would like to know the current weather for 
#Has error recognition to see if the user entered an actual city that is available in the 
#openweathermap and if its not, it prompts the user to enter a different city name
#Has a loop for weather search of multiple cities
def main():
    print('Welcome the CLI Weather Application')

    while True:
        city_name = input('Enter the name of your city: ')
        data = get_weather(city_name)
        if data.get('cod') != 200:
            print('City not found. Try again')
            continue
        show_date()
        display_weather(data, city_name)
        response = input('Do you want to search for another city? y/n ')
        if response == 'y':
            continue
        else:
            break


    return 




if __name__ == '__main__':
    main()

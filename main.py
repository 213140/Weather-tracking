from api_weather_service import ApiWeatherService
from weather_data import  WeatherData
import json

# Get API Key : <https://openweathermap.org/api>
def read_json(path):
    with open(path, 'r') as json_file:
        return json.load(json_file)

# Write API request result into json file
def write_json(path, json_data):
    with open(path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

base_url = 'https://api.openweathermap.org/data/2.5/weather'
jsonapi_key = read_json('API_key.json')['key'] # 'YOUR_API_KEY'

if __name__== "__main__":
    new_service = ApiWeatherService(base_url, jsonapi_key)
    data = new_service.get_weather_data_by_city_name('London')

    write_json("logs/API_request_output.json", data)
    weather_object = WeatherData(data['main']['temp'],
                                 data['main']['humidity'],
                                 data['wind']['speed'],
                                 data['weather'][0]['description'],
                                 f"lon: {data['coord']['lon']}\n {data['coord']['lat']}")

    print(weather_object.description)
    print(weather_object.temperature)
    print(weather_object.humidity)

from API_request_functions import *
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

data = get_weather_data_by_city_name(base_url, 'London', jsonapi_key, 'metric')
write_json("API_request_output.json", data)
print(data['weather'][0]['description'])
print(data['main']['temp'])
print(data['main']['pressure'])
print(data['main']['humidity'])

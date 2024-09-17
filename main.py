import requests
import json

# Get API Key : <https://openweathermap.org/api>
def read_json(path):
    with open(path, 'r') as json_file:
        return json.load(json_file)

jsonapi_key = read_json('API_key.json')['key'] # 'YOUR_API_KEY'

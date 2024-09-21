""""
Class and all implemented functions for requesting data from API
"""
import requests

class ApiWeatherService:
    jsonapi_key: str

    def __init__(self, jsonapi_key, base_url= 'https://api.openweathermap.org/data/2.5/weather'):
        self.base_url = base_url
        self.jsonapi_key = jsonapi_key

    def get_weather_data_by_city_name(self, city_name, data_units='metric'):
        """
        API request by city name
        """
        parameters = {
            'q': city_name,
            'appid': self.jsonapi_key,
            'units': data_units
        }
        response = requests.get(self.base_url, params=parameters)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
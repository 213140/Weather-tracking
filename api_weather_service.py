""""
Class and all implemented functions for requesting data from API
"""
import requests

class ApiWeatherService:
    base_url = ""
    jsonapi_key = ""

    def __init__(self, base_url, jsonapi_key):
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
        return response.json()
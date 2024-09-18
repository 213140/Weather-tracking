""""
All implemented functions for requesting data from API
"""
import requests

def get_weather_data_by_city_name(base_url, city_name, jsonapi_key, units):
    """
    API request by city name
    """
    parameters = {
        'q': city_name,
        'appid': jsonapi_key,
        'units': units
    }
    response = requests.get(base_url, params=parameters)
    return response.json()
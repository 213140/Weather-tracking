from pytest import fail, mark
from unittest.mock import patch
from pathlib import Path
from src.api_weather_service import ApiWeatherService
from src.json_functions import *

# Get the path to the current script
current_file = Path(__file__)
parent_dir = current_file.parent

# Read key from json
key = read_json(parent_dir.parent.parent / 'API_key.json')['key']

# Create a service object for real API tests
service_for_test = ApiWeatherService(key)


""" 
Pytest allow use crete tests without class as presented below.
If finally have bigger amount of tetss can divide them on teh categories (classes).
"""
# Create a service object for mock simulation only
client = ApiWeatherService("http://mockapi.com")

@patch('src.api_weather_service.requests.get')
@mark.smoke
def test_api_using_mock_requests(mock_get):
    # Arrange
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = read_json(parent_dir.parent.parent / 'tests/test_data.json')['mock_response']
    # Act
    result = client.get_weather_data_by_city_name('London')
    # Assert
    assert len(result) == 6
    assert result['weather'][0]['description'] == "clear sky"
    assert result['main']['humidity'] == 65
    assert result['name'] == 'London'

@mark.regression
@mark.smoke
def test_api_using_real_positive_requests():
    # Arrange
    expected = (200, 'London')
    # Act
    result = service_for_test.get_weather_data_by_city_name('London')
    #Assert
    assert result['cod'] == expected[0]
    assert result['name'] == expected[1]

@mark.regression
@mark.smoke
def test_api_using_real_negative_requests_other_city():
    # Arrange
    expected = 'London'
    # Act
    result = service_for_test.get_weather_data_by_city_name('Warsaw')
    # Assert
    assert expected != result['name']

@mark.regression
def test_api_using_real_negative_requests_wrong_city():
    # Arrange
    not_existing_city_name = 'Not_existing_city'
    try:
        # Act
        result = service_for_test.get_weather_data_by_city_name(not_existing_city_name)
    except:
        pass
    else:
        # Assert
        fail("Test failed! Check City name (incorrect). Expected result : 404 Client Error: Not Found for url")



from pathlib import Path
import unittest
from unittest.mock import patch
import logging
from src.api_weather_service import ApiWeatherService
from src.json_functions import *

# Get the path to the current script
current_file = Path(__file__)
parent_dir = current_file.parent

# Read key from json
key = read_json(parent_dir.parent.parent / 'API_key.json')['key']

# Create a service object for real API tests
service_for_test = ApiWeatherService(key)


class TestAPIWeatherService(unittest.TestCase):

    logging.debug("logg1")
    def setUp(self):
        # Create a service object for mock simulation only
        self.client = ApiWeatherService("http://mockapi.com")

    @patch('src.api_weather_service.requests.get')
    def test_api_using_mock_requests(self, mock_get):
        # Arrange
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = read_json(parent_dir.parent.parent / 'tests/test_data.json')['mock_response']
        # Act
        result = self.client.get_weather_data_by_city_name('London')
        # Assert
        self.assertEqual(len(result), 6)
        self.assertEqual(result['weather'][0]['description'], "clear sky")
        self.assertEqual(result['main']['humidity'], 65)
        self.assertEqual(result['name'], 'London')

    def test_api_using_real_positive_requests(self):
        # Arrange
        expected = (200, 'London')
        # Act
        result = service_for_test.get_weather_data_by_city_name('London')
        #Assert
        self.assertEqual(result['cod'], expected[0])
        self.assertEqual(result['name'], expected[1])

    def test_api_using_real_negative_requests_other_city(self):
        # Arrange
        expected = 'London'
        # Act
        result = service_for_test.get_weather_data_by_city_name('Warsaw')
        # Assert
        self.assertNotEqual(expected, result['name'])

    def test_api_using_real_negative_requests_wrong_city(self):
        # Arrange
        not_existing_city_name = 'Not_existing_city'
        try:
            # Act
            result = service_for_test.get_weather_data_by_city_name(not_existing_city_name)
        except:
            pass
        else:
            # Assert
            self.failIf(self, "Test failed! Check City name (incorrect). Expected result : 404 Client Error: Not Found for url")

if __name__ == "__main__":
    unittest.main(verbosity=2)
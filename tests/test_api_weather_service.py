import unittest
from unittest.mock import Mock, patch
from pathlib import Path

from api_weather_service import ApiWeatherService
from json_functions import *

### Read key and base url from json
# Get the path to the current script
current_file = Path(__file__)
# Navigate one directory up
parent_dir = current_file.parent.parent
# Read url and key
base_url = read_json(parent_dir / 'tests/test_data.json')['base_url']
key = read_json(parent_dir / 'API_key.json')['key']
# Create an service object
service_for_test = ApiWeatherService(base_url, key)


class TestAPIWeatherService(unittest.TestCase):

    def setUp(self):
        self.client = ApiWeatherService("http://mockapi.com")

    @patch('api_weather_service.requests.get')
    def test_api_using_mock_requests(self, mock_get):
        # mock_response = Mock()
        # mock_response.status_code = 200
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = read_json(parent_dir / 'tests/test_data.json')['mock_response']

        result = self.client.get_weather_data_by_city_name('London')

        # Assertions
        self.assertEqual(len(result), 6)
        self.assertEqual(result['weather'][0]['description'], "clear sky")
        self.assertEqual(result['main']['humidity'], 65)
        self.assertEqual(result['name'], 'London')

    def test_api_using_real_positive_requests(self):
        # ToBeDefinedSoon
        pass

    def test_api_using_real_negative_requests(self):
        # ToBeDefinedSoon
        pass

if __name__ == "__main__":
    unittest.main(verbosity=3)
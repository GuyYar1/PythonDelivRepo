import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime

from WeatherForecast import WeatherForecast
from common_imports import *
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO  # Import StringIO from io module
from datetime import datetime


class TestWeatherForecast(unittest.TestCase):

    def setUp(self):
        # This method will be called before each test
        self.weather_forecast = WeatherForecast()

    def test_init(self):
        # Test initialization of WeatherForecast object
        weather = WeatherForecast(date_time='2024-05-30 12:00:00', temperature=25.0, humidity=70, weather_description='Sunny')
        self.assertEqual(weather.date_time, '2024-05-30 12:00:00')
        self.assertEqual(weather.temperature, 25.0)
        self.assertEqual(weather.humidity, 70)
        self.assertEqual(weather.weather_description, 'Sunny')

    @patch('weather_forecast.WeatherForecast.get_cache_key')
    @patch('weather_forecast.WeatherForecast.is_cache_valid')
    @patch('weather_forecast.requests.get')
    @patch('weather_forecast.WeatherForecast.print_forecastdata')
    @patch('weather_forecast.WeatherForecast.set_cache')
    def test_get_weatherbycity(self, mock_set_cache, mock_print_forecastdata, mock_requests_get, mock_is_cache_valid, mock_get_cache_key):
        # Mock necessary methods and attributes for testing
        mock_is_cache_valid.return_value = False
        mock_get_cache_key.return_value = 'test_cache_key'
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = {
            'city': {'name': 'Test City', 'country': 'TC'},
            'list': [{
                'dt_txt': '2024-05-30 12:00:00',
                'main': {'temp': 25.0, 'humidity': 70},
                'weather': [{'description': 'Sunny'}]
            }]
        }
        mock_print_forecastdata.return_value = ('2024-05-30 12:00:00', 70, 25.0, 'Sunny')

        # Call the method under test
        result = self.weather_forecast.get_weatherbycity('TestCity')

        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['main']['temp'], 25.0)
        self.assertEqual(result[0]['main']['humidity'], 70)
        self.assertEqual(result[0]['weather'][0]['description'], 'Sunny')
        mock_set_cache.assert_called_once_with('test_cache_key', [{'dt_txt': '2024-05-30 12:00:00', 'main': {'temp': 25.0, 'humidity': 70}, 'weather': [{'description': 'Sunny'}]}])

    def test_print_forecastdata(self):
        # Mock forecast_data for testing
        forecast_data = {
            'dt_txt': '2024-05-30 12:00:00',
            'main': {'temp': 25.0, 'humidity': 70},
            'weather': [{'description': 'Sunny'}]
        }

        # Redirect stdout to capture print statements
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            dt, humidity, temp, weather_description = self.weather_forecast.print_forecastdata(forecast_data)

            # Assertions
            self.assertEqual(dt, '2024-05-30 12:00:00')
            self.assertEqual(humidity, 70)
            self.assertEqual(temp, 25.0)
            self.assertEqual(weather_description, 'Sunny')

            # Check printed output
            expected_output = "Date & Time: 2024-05-30 12:00:00\nTemperature: 25.00°C\nHumidity: 70.00\nWeather: Sunny\n--------------------\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()

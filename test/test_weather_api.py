import os
import unittest
import requests
import datetime
from weather.weather_api import WeatherApi

class EndToEnd(unittest.TestCase):
    def setUp(self):
        self.api_key = os.environ.get("WEATHER_API_KEY")
        self.zip_code = "21202"
        self.start_date = datetime.datetime(2015, 11, 24)
        self.end_date = datetime.datetime(2015, 11, 25)

    def test_search_date_range(self):
        client = WeatherApi()
        print(client.search_date_range(self.start_date, self.end_date, self.zip_code))

    def test_invalid_key(self):
        client = WeatherApi("test")
        result = client.search_date_range(self.start_date, self.end_date, self.zip_code)
        self.assertEqual(result['weather_observations'][0]['error'], "this key does not exist")

    def test_invalid_param(self):
        client = WeatherApi()
        result = client.search_date_range(self.start_date, self.end_date, "")
        self.assertEqual(result['weather_observations'][0]['error'], "you must supply a location query")



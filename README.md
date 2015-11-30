# WeatherApi

An wrapper for WeatherUnderground API

## Overview

The weather api uses the history endpoint of the WeatherUnderground API to query the historical weather condition for a given perid of time and zip code for the location.

## Configuration

To use the WeatherUnderground API, one needs to get an api key to make requests. Don't worry its free. You can get
it [here](http://www.wunderground.com/weather/api/d/docs)

## Setup Prerequisites

1. Set `WEATHER_API_KEY` environment variable as your api key.
2. Install all the requirements in the requirements.txt `pip install -r requirements.txt`

## Usage Example

```python
from weather.weather_api import WeatherApi

\#this will automatically get your api key from the environment variable WEATHER_API_KEY
client = WeatherApi()
cient.search_day(datetime.datetime(2015,11,30), "21202")
```

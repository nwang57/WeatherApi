import datetime
from weather.downloader import download_url

class WeatherApi(object):
    """WeatherUnderground Api wrapper"""
    def __init__(self, api_key="9cfcefad7ac10e20"):
        self.api_key = api_key

    def search_date_range(self, start_date, end_date, zip_code):
        """Search weather conditions for each day between start_date and end_date"""
        result = {"zip_code": zip_code, "start_date": self.format_date(start_date), "end_date": self.format_date(end_date)}
        weather_observations = []
        for date in self.parse_date_range(start_date, end_date):
            weather_observations.append(self.search_day(date, zip_code))
        result["weather_observations"] = weather_observations
        return result

    def search_day(self, date, zip_code):
        """Search the weather history for a single day.

        :param date: Datetime. Query date for the weather condition
        :param zip_code: String. The zipcode of the location
        """
        weather_obs = {"date": self.format_date(date)}
        url = self.get_url(date, zip_code)
        response = download_url(url)
        if 'history' in response:
            weather_obs["weather_conditions"] = self.parse_day_conditions(response['history']['observations'])
        else:
            # error handling
            if 'error' in response:
                weather_obs["error"] = response['error']
            elif 'error' in response["response"]:
                weather_obs["error"] = response["response"]["error"]["description"]
            else:
                weather_obs["error"] = "Unknown Error"
        return weather_obs

    def get_url(self, date, zip_code):
        return 'http://api.wunderground.com/api/' \
               '%s/history_%s/q/%s.json' % (self.api_key, self.format_date(date), zip_code)

    def parse_date_range(self, start_date, end_date):
        """Generate a list of datetimes that are between start_date and end_date"""
        current = start_date
        delta = datetime.timedelta(days=1)
        while (current < end_date):
            yield current
            current += delta

    def format_date(self, date):
        """convert datetime object to string in YYYYMMDD format"""
        return date.strftime("%Y%m%d")

    def parse_day_conditions(self, day_obs):
        return [hour_obs['conds'] for hour_obs in day_obs]

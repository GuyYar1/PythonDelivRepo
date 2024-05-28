
from common_imports import *
import datetime


class WeatherForecast(CacheBase):
    def __init__(self, date_time=None, temperature=None, humidity=None, weather_description=None):
        super().__init__() # initiate cache
        # instance attributes
        self.date_time = date_time
        self.temperature = temperature
        self.humidity = humidity
        self.weather_description = weather_description
    def __str__(self):
        # When you call print(obj) or str(obj)
        # let the user know what is the output if just call the
        return f"Date & Time: {self.date_time}\nTemperature: {self.temperature:.2f}°C\nWeather: {self.weather_description}\n{'-' * 20}"


    def get_weatherbycity(self,cityName: str, country_code: str = None):
        """
             Pure Function, save data to a list of dictionaries uses:
                                Call 5 day / 3 hour forecast data at:
                                            https://openweathermap.org/forecast5#name5
             get_weather by city:  gets(cityName: str, country_code: str )
                   """
        cache_key = self.get_cache_key(cityName, country_code)
        self.print_timesinfo(cityName)

        if not(self.is_cache_valid(cache_key)):
            # if the cache doesnt have this data or the data retrieved more than 2 hours, consider old data

            api_url = "http://api.openweathermap.org/data/2.5/forecast"
            units = "metric"
            appidsufiix= EncodingUtils.readprofile("file.env")
            appid = extract_api_key(appidsufiix)
             #appid = "8fc9d67f835721026f13442e85c59884"  # EncodingUtils.encode_to_base64 doesnt support
            city = cityName
            country = country_code

            if not check_internet():
                print(f"check your internet connection - seems that you have an issue\n")
                print(f"Your query is not in the mem cache or file cache, fix the issue and re run")
                exit()

            if country is None:
                 response = requests.get(api_url, params={"q": city, "units": units, "appid": appid})
                # api.openweathermap.org/data/2.5/forecast?q=London&units=metric&appid=8fc9d67f835721026f13442e85c59884
            else:
                response = requests.get(api_url, params={"q": city + "," + country,  "units": units, "appid": appid})
            print("Data retrieved by restfull API gateway ...")

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()
                # Display the data
                city = data['city']['name']
                country = data['city']['country']
                print(f"Weather Forecast for {city}, {country}. Please ensure that this is what you requested \n")

                # Iterate through the forecast list and print details
                #forecast_list = []

                for forecast_data in data['list']:
                    dt, humidity, temp, weather_description = self.print_forecastdata(forecast_data)
                    # Initiate results structure, current dont use it. could be saved to DB later on
                    WeatherForecast(dt, temp, humidity, weather_description)

                # save to cache
                self.set_cache(cache_key, data['list'])
                return data['list']


                # Now forecast_list contains a list of WeatherForecast objects
            else:
                print("Failed to retrieve data")
                return None
        else:
        #  the data retrived by caching
            print("Data retrieved by mem cache or file cache")
            cache_data = self.get_from_cache(cache_key)
            for forecast_cache_data in cache_data:
                self.print_forecastdata(forecast_cache_data)
            return cache_data

    def print_forecastdata(self, forecast_data):
        dt = forecast_data['dt_txt']
        temp = forecast_data['main']['temp']  # Units are metric: Celsius
        humidity = forecast_data['main']['humidity']  # Units are metric: Celsius
        weather_description = forecast_data['weather'][0]['description']
        print(f"Date & Time: {dt}")
        print(f"Temperature: {temp:.2f}°C")
        print(f"Humidity: {humidity:.2f}")
        print(f"Weather: {weather_description}")
        print("-" * 20)
        return dt, humidity, temp, weather_description

    def print_timesinfo(self, cityName):
        timenow = datetime.datetime.now()
        formatted_time = timenow.strftime("%Y-%m-%d %H:%M:%S")  # Custom format without "T"
        current_timeTZ = get_current_time_by_city(cityName)
        formatted_time = timenow.strftime("%Y-%m-%d %H:%M:%S")  # Custom format without "T"
        print(f"The current time is:{formatted_time} The time in the relevant City is:{current_timeTZ}")


'''

The 3 functions below is just a play around other services that block calls more than i calls in t period. therefore i use net to renew ip in case of other than 200=ok arrived. 1 extra try.


    def get_cityweather_bylanlon(self, lat, lon):
        """
            Not in use , working but just to understand better the APIs

        :param lat:
        :param lon:
        :return:
        """
        api_url = "http://api.openweathermap.org/data/2.5/forecast"
        units = "metric"
        appid = "938c93a1b831c3a45a54ec14dce62288"

        response = requests.get(api_url, params={"lat": lat, "lon": lon, "units": units, "appid": appid})
        # api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid=938c93a1b831c3a45a54ec14dce62288

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Display the data
            city = data['city']['name']
            print(data['city'])
            print(data)
            country = data['city']['country']
            print(f"Weather Forecast for {city}, {country}:\n")

            # Iterate through the forecast list and print details
            for forecast in data['list']:
                dt = forecast['dt_txt']
                temp = forecast['main']['temp']  # Units are metric: Celsius
                weather_description = forecast['weather'][0]['description']
                print(f"Date & Time: {dt}")
                print(f"Temperature: {temp:.2f}°C")
                print(f"Weather: {weather_description}")
                print("-" * 20)

        else:
            print("Failed to retrieve data")

        # If you want to save the data in a proper object, you can create a class for it
        # Parse the response and save in a list of WeatherForecast objects
        forecast_list = []
        for forecast in data['list']:
            date_time = forecast['dt_txt']
            temperature = forecast['main']['temp']  # Celsius due to units
            weather_description = forecast['weather'][0]['description']
            forecast_list.append(WeatherForecast(date_time, temperature, weather_description))

        print("This is Class Printing  below")
        # Display the forecasts
        for forecast in forecast_list:
            print(forecast)


    def getcordibycity(self, city: str = "Holon"):
        # Make the API call
        # https://realpython.com/python-requests/#query-string-parameters
        # https://docs.python.org/3/library/urllib.parse.html
        renewip()  # avoid blocking by policy
        base_url = "https://nominatim.openstreetmap.org/search"

        params = {
            "city": city,
            "format": "json"  # Specify JSON format
        }
        # response1 = b'<html><body>Hello World</body></html>'
        # data_str = b''.join(response1).decode('utf-8')
        lat = 1.00
        lon = 1.00
        response1 = requests.get(base_url, params)

        if (response1.status_code) == 200:
            # Decode bytes to string
            data_str = b''.join(response1).decode('utf-8')
            # Parse JSON data
            data = json.loads(data_str)
            print(data)
            # API details
            lat = (data[0]["lat"])  # "44.34"
            lon = (data[0]["lon"])  # "10.99"
        else:
            print(" error on lat lon response - please check ... - abort")

        return [lat, lon]


    def getweatherbycity_3paty(self, city_name):
        lat, lon = self.getcordibycity(city_name)
        return self.get_cityweather_bylanlon(lat, lon)


'''

    # OOP
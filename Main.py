# colab: !pip install requests
#  python -m pip install requests
#  install geopy
# pip install geopy timezonefinder # PIp on terminal
# pip install geopy timezonefinder pytz
# # Import Files

from WeatherForecast import WeatherForecast
from common_imports import *

wc_obj = WeatherForecast()

city_name = input("Enter city Name?")
country_code = input("Enter country code? if you dont have type: N  -->")
country_code = None if country_code == "N" else country_code


print(f"The selected city_name is: {city_name} in the country code: {str(country_code)}")


#wc_obj.get_weatherbycity(city_name)
wc_obj.get_weatherbycity(city_name, country_code)


#time_zone = get_time_zone_by_city(city_name)

#if time_zone:
 #   print(f"Time Zone of {city_name}: {time_zone}")
# colab: !pip install requests
#  python -m pip install requests
#  install geopy
# pip install geopy timezonefinder # PIp on terminal
# pip install geopy timezonefinder pytz
# pip install python-dotenv # halt due to conflicts
# pip install file

## Import Files

from WeatherForecast import *
from common_imports import *

wc_obj = WeatherForecast()

city_name = input("Enter city Name?")
country_code = input("Enter country code? if you dont have type: N  -->")
country_code = None if country_code == "N" else country_code


print(f"The selected city_name is: {city_name} in the country code: {str(country_code)}")


wc_obj.get_weatherbycity(city_name, country_code)


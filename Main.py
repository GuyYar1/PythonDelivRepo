# colab: !pip install requests
#  python -m pip install requests
#  install geopy
# pip install geopy timezonefinder # PIp on terminal
# pip install geopy timezonefinder pytz
# pip install python-dotenv # halt due to conflicts
# pip install file
# pip install streamlit


from WeatherForecast import *
from common_imports import *

wc_obj = WeatherForecast()

#forecast_list_cache = {
#                "city": None, "countrycode": None, "listresult": []}

doagain = True


while doagain:

    try:
        # Case sensitive
        city_name = input("Enter city Name:")
        country_code = input("Enter country code, if you dont have type enter:N  -->")
        country_code = None if country_code == "N" else country_code

        # function retrieved the data list but for now there is no use. optional.
        wc_obj.get_weatherbycity(city_name, country_code)

        print(f"The selected city_name is: {city_name} in the country code: {str(country_code)}")

        user_input = input("Please enter 1 to Continue or 0 to Exit: -->")
        doagain = True if user_input == "1" else False
        print(f"The program ended due to user selection: {user_input}")

    except ValueError:
        print("Invalid input. That is not a number. Please try again. Exit...")



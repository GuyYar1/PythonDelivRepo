from common_imports import *

def get_time_zone_by_city(city_name):
    try:
        time_zones = pytz.all_timezones
        for tz in time_zones:
            if city_name.lower() in tz.lower().replace("_", " "):
                return tz
        return None  # Return None if city not found in time zones
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


def get_current_time_by_city(city_name):
    try:
        # Get time zone
        time_zone = pytz.timezone(get_time_zone_by_city(city_name))
        if not time_zone:
            return f"Time zone information not found for {city_name}."

        # Get current time in the specified time zone
        current_time = datetime.now(time_zone)

        # Format the current time nicely
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S %Z')

        return f"The current time in {city_name} is {formatted_time}."

    except Exception as e:
        return f"Error occurred: {e}"
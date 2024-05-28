import streamlit as st
from WeatherForecast import WeatherForecast  # Replace YourModule with your actual module name


def main():
    st.title('Weather Forecast App')
    city = st.text_input('Enter city name', 'London')
    country = st.text_input('Enter country code (optional)', '')

    if st.button('Get Weather'):
        weather_forecast = WeatherForecast()
        forecast_list = weather_forecast.get_weatherbycity(city, country)

        if forecast_list:
            for forecast in forecast_list:
                st.write(forecast)
        else:
            st.write('Failed to retrieve weather data.')


if __name__ == '__main__':
    main()
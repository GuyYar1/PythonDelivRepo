import streamlit as st
from WeatherForecast import WeatherForecast  # Replace YourModule with your actual module name

# How to run: open powershell type: streamlit run app.py
def main():
    st.title('Weather Forecast App')
    city = st.text_input('Enter city name', 'London')
    country = st.text_input('Enter country code (optional)', '')

    if st.button('Get Weather'):
        weather_forecast = WeatherForecast()
        forecast_list = weather_forecast.get_weatherbycity(city, country)

        if forecast_list:

            for forecast in forecast_list:
                dt = forecast['dt_txt']
                temp = forecast['main']['temp']  # Units are metric: Celsius
                humidity = forecast['main']['humidity']  # Units are metric: Celsius
                weather_description = forecast['weather'][0]['description']
                st.write(f"The selected city_name is: {city} in the country code: {str(country)}")
                st.write(weather_forecast.print_timesinfo(city, "streamlit"))
                st.write("-" * 20)
                st.write(f"Date & Time: {dt}")
                st.write(f"Temperature: {temp:.2f}°C")
                st.write(f"Humidity: {humidity:.2f}")
                st.write(f"Weather: {weather_description}")
                st.write("-" * 20)
        else:
            st.write('Failed to retrieve weather data.')


if __name__ == '__main__':
    main()

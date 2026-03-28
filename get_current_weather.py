from langchain.tools import tool
from pydantic import BaseModel, Field
import requests

# Define the input schema for your weather tool
class WeatherInput(BaseModel):
    """Input for getting current weather information."""
    latitude: float = Field(description="The latitude of the location.")
    longitude: float = Field(description="The longitude of the location.")
    unit: str = Field(default="celsius", description="The unit for temperature (e.g., 'celsius', 'fahrenheit').")

@tool(args_schema=WeatherInput)
def get_current_weather(latitude: float, longitude: float, unit: str = "celsius") -> str:
    """
    Fetches the current weather conditions for a given geographical coordinate.
    Uses the Open-Meteo API to get temperature, weather code, and wind speed.
    """
    try:
        # Construct the API URL for Open-Meteo
        api_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={latitude}&longitude={longitude}&current_weather=true"
            f"&temperature_unit={unit}&wind_speed_unit=ms&precipitation_unit=mm"
        )
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        weather_data = response.json()

        if "current_weather" in weather_data:
            current = weather_data["current_weather"]
            temperature = current.get("temperature")
            wind_speed = current.get("windspeed")
            weather_code = current.get("weathercode")

            return (
                f"Current weather at Latitude {latitude}, Longitude {longitude}:\n"
                f"Temperature: {temperature}°{unit.upper()[0]}\n"
                f"Wind Speed: {wind_speed} m/s\n"
                f"Weather Code: {weather_code} (Refer to Open-Meteo WMO Codes for details)"
            )
        else:
            return "Could not retrieve current weather data from the API."

    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
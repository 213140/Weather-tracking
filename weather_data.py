from datetime import datetime

class WeatherData:
    temperature: float = 0.0
    humidity: float = 0
    wind_speed: dict
    description: str = ""
    location: str = ""

    def __init__(self, temperature, humidity, wind_speed, description, location):
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.description = description
        self.location = location

    def get_temperature(self):
        return self.temperature

    def get_weather_description(self):
        return self.description
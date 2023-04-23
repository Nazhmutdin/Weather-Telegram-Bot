from datetime import datetime
from config import *
import requests
import json


class WeatherParser:

    def __init__(self):
        self.s = requests.Session()
    
    def get_wind_direction(self, text:dict) -> str:
        deg = text["wind"]["deg"]
        deg = round(deg / 45) * 45

        if deg == 360:
            deg = 0

        if deg == 0:
            return "North"
        elif deg == 45:
            return "NorthEast"
        elif deg == 90:
            return "East"
        elif deg == 135:
            return "SouthEast"
        elif deg == 180:
            return "South"
        elif deg == 225:
            return "SouthWest"
        elif deg == 270:
            return "West"
        else:
            return "NorthWest"
        

    def parse_data(self, text:json) -> str:
        dataJson = text
        data = {
            "location": dataJson["name"],
            "temperature": dataJson["main"]["temp"],
            "temperature_feeling": dataJson['main']['feels_like'],
            "pressure": dataJson["main"]["pressure"],
            "humidity": dataJson["main"]["humidity"],
            "description": dataJson["weather"][0]["description"],
            "wend_speed": dataJson["wind"]["speed"],
            "wend_direction": self.get_wind_direction(text=dataJson),
            "sunrise": str(datetime.fromtimestamp(dataJson["sys"]["sunrise"])),
            "sunset": str(datetime.fromtimestamp(dataJson["sys"]["sunset"]))
        }

        return data

    def get_data_coord(self, latitude:float, longitude: float) -> json:
        return self.parse_data(self.s.get(CURRENT_WEATHER_API_CALL_COORD.format(latitude=latitude, longitude=longitude), timeout=3).json())
        
    
    def get_data_city(self, city_name:str) -> json:
        return self.parse_data(self.s.get(CURRENT_WEATHER_API_CALL_CITY.format(city=city_name), timeout=3).json())
    
    def pretty_output(self, data:dict):
        text = ""
        for key, value in data.items():
            text += f"{key}: {value}\n"
        
        return text.strip()


if __name__ == "__main__":
    parser = WeatherParser()
    print(parser.pretty_output(parser.get_data_city(city_name="Moscow")))
    print(parser.s.headers)
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


WEATHER_BTN = InlineKeyboardButton(text="Weather", callback_data="weather")
SUN_BTN = InlineKeyboardButton(text="sunrise and sunset", callback_data="sun")

CITY_MODE = InlineKeyboardButton(text="Your city name", callback_data="city")
LOCATION_MODE = InlineKeyboardButton(text="Your location", callback_data="location")

Inline = InlineKeyboardMarkup(row_width=2).add(WEATHER_BTN, SUN_BTN)
Markup = InlineKeyboardMarkup(row_width=2).add(CITY_MODE, LOCATION_MODE)


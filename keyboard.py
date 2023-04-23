from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


CITY_MODE = InlineKeyboardButton(text="Your city name", callback_data="city")
LOCATION_MODE = InlineKeyboardButton(text="Your location", callback_data="location")

Markup = InlineKeyboardMarkup(row_width=2).add(CITY_MODE, LOCATION_MODE)


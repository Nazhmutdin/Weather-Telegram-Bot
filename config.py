BOT_API_TOKEN = 'YOUR_BOT_TOKEN'
WEATHER_API_KEY = 'YOUR_API_KEY'

CURRENT_WEATHER_API_CALL_COORD = (
    'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=' + WEATHER_API_KEY + '&units=metric'
)

CURRENT_WEATHER_API_CALL_CITY = (
    'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=' + WEATHER_API_KEY + '&units=metric'
)

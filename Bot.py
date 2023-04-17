import logging
from aiogram import Bot, Dispatcher, executor, types

from config import BOT_API_TOKEN
from keyboard import Markup
from Parser import WeatherParser


class WeatherBot:

    def __init__(self):

        self.parser = WeatherParser()
        self.bot = Bot(token=BOT_API_TOKEN)
        self.dp = Dispatcher(self.bot)

        logging.basicConfig(level=logging.INFO, filename="info.log")


    def get_keyboard():
        keyboard = types.ReplyKeyboardMarkup()
        LOCATION_MODE = types.KeyboardButton(text="Share location", request_location=True)
        keyboard.add(LOCATION_MODE)
        return keyboard


    async def welcome(self, message: types.Message):
        reply = "Hi, I'm WeatherBot! \n"
        await message.reply(reply, reply_markup=Markup)


    async def callback_city(self, callback: types.CallbackQuery):
        await callback.message.answer(text="Please, enter your city!")
        await self.bot.answer_callback_query(callback.id)


    async def callback_location(self, callback: types.CallbackQuery):
        await callback.message.answer(text="Please, share your location!", reply_markup=self.get_keyboard())
        await self.bot.answer_callback_query(callback.id)


    async def handle_location(self, message: types.Message):
        data = self.parser.get_data_coord(latitude=message.location.latitude, longitude=message.location.longitude)
        await message.answer(f"latitude: {message.location.latitude}  longitude: {message.location.longitude}")


    async def get_name(self, message: types.Message):
        data = self.parser.get_data_city(city_name=message.text)
        await message.reply(text=self.parser.pretty_output(data))


    def reqister_handlers(self):
        self.dp.register_callback_query_handler(self.callback_city, text="city")
        self.dp.register_callback_query_handler(self.callback_location, text="location")
        self.dp.register_message_handler(self.handle_location, content_types=["location"])
        self.dp.register_message_handler(self.welcome, commands=['start'])
        self.dp.register_message_handler(self.get_name)


    def main(self):
        self.reqister_handlers()
        executor.start_polling(self.dp, skip_updates=True)



if __name__ == "__main__":
    bot = WeatherBot()
    bot.main()

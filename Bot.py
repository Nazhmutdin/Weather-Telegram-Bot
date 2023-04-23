import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_API_TOKEN
from keyboard import Markup
from states import CityState, CoordState



class WeatherBot(CityState, CoordState):

    def __init__(self):
        self.bot = Bot(token=BOT_API_TOKEN)
        self.dp = Dispatcher(self.bot, storage=MemoryStorage())

        logging.basicConfig(level=logging.INFO, filename="info.log")


    async def welcome(self, message: types.Message):
        reply = "Hi, I'm WeatherBot! \n"
        await message.reply(reply, reply_markup=Markup)


    def reqister_handlers(self):
        self.dp.register_callback_query_handler(self.request_city_name, text = "city")
        self.dp.register_message_handler(self.handle_city_request, state=CityState.city_name)
        self.dp.register_callback_query_handler(self.request_user_location, text="location")
        self.dp.register_message_handler(self.handle_location_request, content_types=["location"], state=CoordState.coordinates)
        self.dp.register_message_handler(self.welcome, commands=['start'])


    def main(self):
        self.reqister_handlers()
        executor.start_polling(self.dp, skip_updates=True)


if __name__ == "__main__":
    bot = WeatherBot()
    bot.main()

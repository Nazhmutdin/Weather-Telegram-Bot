from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram import types

from Parser import WeatherParser



class CityState(StatesGroup):

    city_name = State()
    parser = WeatherParser()

    async def request_city_name(self, callback: types.CallbackQuery):
        await callback.message.answer("Please, enter your city!")
        await self.city_name.set()
        await callback.answer(callback.id)


    async def handle_city_request(self, message: types.Message, state: FSMContext):
        await state.update_data(city_name=message.text)
        data = await state.get_data()
        data = self.parser.get_data_city(city_name=data["city_name"])
        await message.answer(self.parser.pretty_output(data))
        await state.finish()


class CoordState(StatesGroup):

    coordinates = State()
    parser = WeatherParser()

    
    async def request_user_location(self, callback: types.CallbackQuery):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        LOCATION_MODE = types.KeyboardButton(text="Share location", request_location=True)
        keyboard.add(LOCATION_MODE)
        await callback.message.answer("Please, share your location!", reply_markup=keyboard)
        await self.coordinates.set()
        await callback.answer(callback.id)
    

    async def handle_location_request(self, message: types.Message, state: FSMContext):
        await state.update_data(coordinates=[message.location.latitude, message.location.longitude])
        data = await state.get_data()
        data_answer = self.parser.get_data_coord(latitude=data["coordinates"][0], longitude=data["coordinates"][0])
        await message.answer(text=self.parser.pretty_output(data=data_answer))
        await state.finish()

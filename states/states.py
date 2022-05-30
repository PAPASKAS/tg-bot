from aiogram.dispatcher.filters.state import StatesGroup, State


class VideosState(StatesGroup):
    first_video = State()
    second_video = State()
    third_video = State()
    fourth_video = State()
    fifth_video = State()


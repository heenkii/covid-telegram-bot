from aiogram.dispatcher.filters.state import State, StatesGroup


class user_states(StatesGroup):
    main_page = State()
    countries_page = State()
    find_page = State()
    info_page = State()

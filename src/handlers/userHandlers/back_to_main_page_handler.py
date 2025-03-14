from FSM import user_states
from aiogram import types
from keyboards.default import main_keyboard
from loader import dp, bot


@dp.message_handler(text="Вернуться к главному меню 🔄", state="*")
async def back_to_main_screen(message: types.Message):
    await user_states.main_page.set()
    await bot.send_message(
        message.from_user.id, "Главное меню 🔁", reply_markup=main_keyboard
    )

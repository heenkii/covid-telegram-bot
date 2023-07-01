from keyboards.default import main_keyboard
from loader import dp, bot
from aiogram import types
from FSM import user_states
@dp.message_handler(commands=["start"], state="*")
async def start(message: types.Message):
    await user_states.main_page.set()
    await bot.send_message(message.from_user.id,
                           "Бип-бип...\nПривет!\nЭтот бот был разработан для распространения информации о короновирусной инфекции (Covid-19)🦠")
    await bot.send_sticker(message.from_user.id,
                           "CAACAgIAAxkBAAIIgF65ucQNXFE8q86mjl_E3OuLiPXzAALOAQACVp29Cq2jmuzmnvpMGQQ")
    await bot.send_message(message.from_user.id,
                           "Нажми одну из кнопок внизу\n😉 🔽",
                           reply_markup=main_keyboard)


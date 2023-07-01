from aiogram import executor
from handlers import dp
from loader import bot

import asyncio

from utils.sqlighter import Database


# update statistic
async def update_data(whait_for=3600):
    while True:
        db = Database()
        db.update_data()
        await asyncio.sleep(whait_for)


async def start_bot(_):
    me = await bot.get_me()
    print(f"""\n--------------------------
Bot {me.first_name} start
--------------------------\n""")

    # async run bot and update static
if __name__ == "__main__":
    asyncio.get_event_loop().create_task(update_data(10800))
    executor.start_polling(dp, on_startup=start_bot, skip_updates=True)

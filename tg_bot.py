from aiogram import Bot, Dispatcher, executor, types
from config import token
from config import user_id
import json
from main import chek_news_update
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
import asyncio

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.reply("Успешно")



async def news_every_minute():
    while True:
        fresh_new = chek_news_update()

        if len(fresh_new) >=1:
            for k,v in sorted(fresh_new.items()):
                news = f"{hbold((v['article_title']))}\n {hunderline(v['article_price'])} \n {v['article_link']}"

                await bot.send_message(user_id, news)

        await asyncio.sleep(10)
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_minute())
    executor.start_polling(dp)

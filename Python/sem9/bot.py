from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Command
from config import TOKEN
from calc import calc_main

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nЯ много чего умею!\nПодробнее: /help")

@dp.message_handler(commands=['start', 'help'])

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Калькулятор: /eval (здесь должно быть ваше выражение)")

@dp.message_handler(commands=['eval'])
async def process_start_command(message: types.Message, command: Command):
    await message.reply(f"А вот что мы насчитали: {calc_main(command.args)}")

# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, calc_main(msg.text))

if __name__ == '__main__':
    executor.start_polling(dp)
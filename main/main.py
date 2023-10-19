from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


TOKEN = "6888660701:AAF7q_1qGV8pEfA_4W9FNw3l2KW2YqQiNKU"
bot = Bot(TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('/delete'))


@dp.message_handler(commands=['create'])
async def create_command(message: types.Message):
    await message.answer(text='меню создано',
                         reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['delete'])
async def delete_command(message: types.Message):
    await message.answer(text='меню удалено',
                         reply_markup=ReplyKeyboardRemove())
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp)

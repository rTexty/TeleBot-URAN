from config import token
from settings import CustomInputFile
import logging
from aiogram import Bot, Dispatcher,types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile
from aiogram.filters import CommandStart, Command
import asyncio

from keyboards import services_keyboard, back_keyboard

selected_text = None
path_to_img = 'img/services.jpeg'
photo = CustomInputFile(path_to_img, filename='services.jpeg')

ADMIN_CHAT_ID = ['5944980799', '821572310']

# Устанавливаем уровень логгирования
logging.basicConfig(level=logging.INFO)

# Инициализируем бота и диспетчера
bot = Bot(token=token)
dp = Dispatcher()
      
# Обработка команды /start
@dp.message(CommandStart())
async def start(message: types.Message):
    # Предложение выбрать тип услуги
    await message.answer_photo(photo=photo, caption="Привет! Выберите тип услуги:", reply_markup=services_keyboard)



# Обработка выбора типа услуги
@dp.callback_query(lambda callback_query: callback_query.data)
async def process_service(callback_query: types.CallbackQuery,):
    # Retrieve the callback_data from the callback_query object
    callback_data = callback_query.data
    await callback_query.answer(text=f"Вы выбрали {callback_data}")
    await bot.answer_callback_query(callback_query.id)
    # Find the button with the matching callback_data and retrieve its text
    global selected_text
    for row in services_keyboard.inline_keyboard:
       for button in row:
           if button.callback_data == callback_data:
               selected_text = button.text
               break
       else:
           continue
       break
   
    if selected_text is not None and callback_query.data != 'Назад':
       await bot.send_message(callback_query.from_user.id, f"Вы выбрали {selected_text}. Теперь отправьте требования и пожелания к заказу", reply_markup=back_keyboard)
    if callback_query.data == 'Назад':
        await bot.delete_message(chat_id= callback_query.from_user.id, message_id=callback_query.message.message_id)
        # Обработка всех сообщений, кроме команд и запросов на выбор типа услуги

@dp.message(lambda message: not message.text.startswith('/') and not message.text.startswith('service'))
async def handle_message(message: types.Message,):
    # Проверяем, был ли пользователь предварительно выбран тип услуги
    if True:
        # Отправляем сообщение администраторам с данными от пользователя
        admin_message = f"Новое сообщение от пользователя {message.from_user.username} (ID: {message.from_user.id}):\n\n" \
                        f"Тип услуги: {selected_text}\n" \
                        f"Требования и пожелания к заказу: {message.text}\n" \
                        f"Логин Telegram: {message.from_user.username}"
        for admin in ADMIN_CHAT_ID:
            await bot.send_message(chat_id=admin, text=admin_message)
        await bot.send_message(chat_id=message.from_user.id, text="Ваш заказ принят!\nСкоро с Вами свяжется менеджер для обсуждения деталей!")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    if __name__ == '__main__':
        await dp.start_polling(bot)

asyncio.run(main())
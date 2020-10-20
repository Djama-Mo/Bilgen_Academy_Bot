from telebot import TeleBot
from telebot.types import Message
from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton
import os


TOKEN = ''

bot = TeleBot(token=TOKEN)


say_hello = os.environ.get('say_hello')

@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    markup = ReplyKeyboardMarkup()
    button_kz = KeyboardButton('Қазақша')
    button_ru = KeyboardButton('Русский')
    markup.row(button_kz, button_ru)
    bot.send_message(chat_id=message.chat.id, text=say_hello, reply_markup=markup)

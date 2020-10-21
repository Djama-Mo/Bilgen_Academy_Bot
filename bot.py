from telebot import TeleBot
from telebot.types import Message
from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton


def main():
    bot.polling()


TOKEN = '1025880897:AAGRpeQHuxmZSpf8DEhLSEjUgC0fgg2fU3U'

bot = TeleBot(token=TOKEN)


def status_kz(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_teacher = KeyboardButton('Мұғалім')
    button_student = KeyboardButton('Оқушы')
    markup.row(button_teacher, button_student)
    bot.send_message(chat_id=id, text='Дәрежеңіз', reply_markup=markup)


def status_ru(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_teacher = KeyboardButton('Преподаватель')
    button_student = KeyboardButton('Ученик')
    markup.row(button_teacher, button_student)
    bot.send_message(chat_id=id, text='Ваш статус', reply_markup=markup)


def info_1(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton('Tanymger')
    button_2 = KeyboardButton('Bilgen Tech')
    button_3 = KeyboardButton('Oysana')
    button_4 = KeyboardButton('Тоғызқұмалақ')
    button_5 = KeyboardButton('Білікті педагог')
    markup.row(button_1, button_2, button_3, button_4, button_5)
    bot.send_message(chat_id=id, text='...', reply_markup=markup)


def student_kz(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton('Курстар')
    button_2 = KeyboardButton('Олимпиадалар')
    markup.row(button_1, button_2)
    bot.send_message(chat_id=id, text='...', reply_markup=markup)


def info_2(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton('Bilgen UBT')
    button_2 = KeyboardButton('Bilgen Tech')
    markup.row(button_1, button_2)
    bot.send_message(chat_id=id, text='...', reply_markup=markup)


def info_3(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton('Bilgen Baige/Alaman')
    button_2 = KeyboardButton('Bala/Bilik Time')
    markup.row(button_1, button_2)
    bot.send_message(chat_id=id, text='...', reply_markup=markup)


def info_4(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton('Tanymger')
    button_2 = KeyboardButton('Bilgen Tech')
    button_3 = KeyboardButton('Oysana')
    button_4 = KeyboardButton('Тоғызқұмалақ')
    button_5 = KeyboardButton('Квалифицированный педагог')
    markup.row(button_1, button_2, button_3, button_4, button_5)
    bot.send_message(chat_id=id, text='...', reply_markup=markup)


def student_ru(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton('Курсы')
    button_2 = KeyboardButton('Олимпиады')
    markup.row(button_1, button_2)
    bot.send_message(chat_id=id, text='...', reply_markup=markup)



@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_kz = KeyboardButton('🇰🇿 Қазақша')
    button_ru = KeyboardButton('🇷🇺 Русский')
    markup.add(button_kz, button_ru)
    bot.send_message(chat_id=message.chat.id, text=say_hello, reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def language_kz(message: Message):
    id_ = message.chat.id
    if message.text == '🇰🇿 Қазақша':
        status_kz(id=id_)
    elif message.text == '🇷🇺 Русский':
        status_ru(id=id_)
    elif message.text == 'Мұғалім':
        info_1(id=id_)
    elif message.text == 'Оқушы':
        student_kz(id=id_)
    elif message.text == 'Курстар':
        info_2(id=id_)
    elif message.text == 'Олимпиадалар':
        info_3(id=id_)
    elif message.text == 'Преподаватель':
        info_4(id=id_)
    elif message.text == 'Ученик':
        student_ru(id=id_)
    elif message.text == 'Курсы':
        info_2(id=id_)
    elif message.text == 'Олимпиады':
        info_3(id=id_)


say_hello = 'Здравствуйте, Вас приветствует Bilgen Academy, выберите пожалуйста язык'


if __name__ == '__main__':
    main()

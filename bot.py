# import time
import requests
# from html2text import HTML2Text
from telebot import TeleBot
from telebot.types import KeyboardButton
from telebot.types import Message
from telebot.types import ReplyKeyboardMarkup
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
# from mysql import connector
import redis_cache
from MySQL_db import *
import re
import random
from string import ascii_letters
from string import digits
from telebot.types import Poll
from telebot.types import CallbackQuery
from telebot.apihelper import ApiTelegramException
import hashlib
from txt_vars import *

import doda_olymp
import ped_start_olymp
import sprint_1
import sprint_10
import sprint_11
import sprint_2
import sprint_3
import sprint_4
import sprint_5
import sprint_6
import sprint_7
import sprint_8
import sprint_9
import subjects_11
import subjects_10
import subjects_9
import subjects_8
import subjects_7
import subjects_6
import subjects_5
import subjects_4
import subjects_3
import subjects_2
import subjects_1
import ped_olymp
import time_kz
import time_ru


config.fileConfig('log.ini', disable_existing_loggers=False)
logger = getLogger(__name__)


def main():
    bot.polling(none_stop=True)


TOKEN = '1444931205:AAFd87IYZON5mVbfxi9-zVGf45mkLYXvPLY'

bot = TeleBot(token=TOKEN)


buttons = dict()

iin_flag = 0  # 0 if sign up; 1 if sign in
class_flag = 0
question_id = 0

quizes = {'user_id': ['quiz_id', 'msg_id', 'callback']}

user_now = {'user_id': 'lang'}


def prefix(sub):
    pi = [0] * len(sub)
    for i in range(1, len(sub)):
        j = pi[i - 1]
        while j > 0 and sub[j] != sub[i]:
            j = pi[j - 1]
        if sub[j] == sub[i]:
            j = j + 1
        pi[i] = j
    return pi


def kmp(string, sub):
    index = -1
    pi = prefix(sub)
    j = 0
    for i in range(len(string)):
        while j > 0 and sub[j] != string[i]:
            j = pi[j - 1]
        if sub[j] == string[i]:
            j = j + 1
        if j == len(sub):
            index = i - len(sub) + 1
            break
    return index


# def connect_bilgen():
#     db = connector.connect(host='94.247.135.53',
#                            user='telegramUser',
#                            password='!QAZ2wsx')
#
#     return db


def dec_password(password):
    dec_pass = hashlib.md5(password).hexdigest()
    return dec_pass


def sign_up_in_kz(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_sign_up = KeyboardButton('Тіркеу')
    button_sign_in = KeyboardButton('Кіру')
    button_reset_pass = KeyboardButton('Кілт сөзді ұмыттыңыз ба?')
    markup.add(button_sign_in).add(button_sign_up).add(button_reset_pass)
    bot.send_message(chat_id=id, text='Дәрежеңіз', reply_markup=markup)


def sign_up_in_ru(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_sign_up = KeyboardButton('Регистрация')
    button_sign_in = KeyboardButton('Авторизация')
    button_reset_pass = KeyboardButton('Восстановить пароль')
    markup.add(button_sign_in).add(button_sign_up).add(button_reset_pass)
    bot.send_message(chat_id=id, text='Выберите', reply_markup=markup)


def sign_up_ru(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_contact = KeyboardButton('Байланыс нөмірімен бөлісу\n\nПоделиться контактом', request_contact=True)
    markup.add(button_contact)
    bot.send_message(chat_id=id, text=enter_the_number_text, reply_markup=markup)


def pass_forget(message):
    markup = InlineKeyboardMarkup()
    text = 'Сіздің ЖСН WhatsApp чатына жазыңыз және сізге көмектеседі ⬇️\n\n' \
           'Напишите в чат в WhatsApp Ваш ИИН и Вам помогут ⬇️'
    button = InlineKeyboardButton(text='WhatsApp', url='wa.me/77783873039')
    markup.add(button)
    try:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
    except ApiTelegramException:
        pass
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(chat_id=message.chat.id, text=text, reply_markup=markup)


def sign_in_ru(id):
    bot.send_message(chat_id=id, text='Кілт сөз\n\nПароль')


def iin(id):
    bot.send_message(chat_id=id, text='ЖСН\n\nИИН')


def fio(id):
    bot.send_message(chat_id=id, text='Аты-жөніңіз\n\nВаше ФИО')


def check_id(id):
    bot.send_message(chat_id=id, text='send the id')


def select_region(id, message_id):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Атырауская область', callback_data='Атырауская область')
    button_2 = InlineKeyboardButton(text='Восточно-Казахстанская область', callback_data='ВКО')
    button_3 = InlineKeyboardButton(text='Костанайская область', callback_data='Костанайская область')
    button_4 = InlineKeyboardButton(text='Мангистауская область', callback_data='Мангистауская область')
    button_5 = InlineKeyboardButton(text='Кызылординская область', callback_data='Кызылординская область')
    button_6 = InlineKeyboardButton(text='Жамбылская область', callback_data='Жамбылская область')
    button_7 = InlineKeyboardButton(text='Карагандинская область', callback_data='Карагандинская область')
    button_8 = InlineKeyboardButton(text='Туркистанская область', callback_data='Туркистанская область')
    button_9 = InlineKeyboardButton(text='Западно-Казахстанская область', callback_data='ЗКО')
    button_10 = InlineKeyboardButton(text='Акмолинская область', callback_data='Акмолинская область')
    button_11 = InlineKeyboardButton(text='Актюбинская область', callback_data='Актюбинская область')
    button_12 = InlineKeyboardButton(text='Павлодарская область', callback_data='Павлодарская область')
    button_13 = InlineKeyboardButton(text='Северно-Казахстанская область', callback_data='СКО')
    button_15 = InlineKeyboardButton(text='Алматинская область', callback_data='Алматинская область')

    button_14 = InlineKeyboardButton(text='Нур-Султан', callback_data='Нур-Султан')
    button_16 = InlineKeyboardButton(text='Алматы', callback_data='Алматы')
    button_17 = InlineKeyboardButton(text='Шымкент', callback_data='Шымкент')

    markup_url.add(button_1).add(button_2).add(button_3).add(button_4).add(button_5).add(button_6).add(button_7).\
        add(button_8).add(button_9).add(button_10).add(button_11).add(button_12).add(button_13).add(button_14).\
        add(button_15).add(button_16).add(button_17)

    bot.delete_message(chat_id=id, message_id=message_id)
    bot.send_message(chat_id=id, text='\n\nВыберите регион...\n\n', reply_markup=markup_url)


def select_region_kz(id, message_id):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Атырау облысы', callback_data='Атырау облысы')
    button_2 = InlineKeyboardButton(text='Шығыс Қазақстан облысы', callback_data='Шығыс Қазақстан облысы')
    button_3 = InlineKeyboardButton(text='Қостанай облысы', callback_data='Қостанай облысы')
    button_4 = InlineKeyboardButton(text='Маңғыстау облысы', callback_data='Маңғыстау облысы')
    button_5 = InlineKeyboardButton(text='Қызылорда облысы', callback_data='Қызылорда облысы')
    button_6 = InlineKeyboardButton(text='Жамбыл облысы', callback_data='Жамбыл облысы')
    button_7 = InlineKeyboardButton(text='Қарағанды облысы', callback_data='Қарағанды облысы')
    button_8 = InlineKeyboardButton(text='Түркістан облысы', callback_data='Түркістан облысы')
    button_9 = InlineKeyboardButton(text='Батыс Қазақстан облысы', callback_data='Батыс Қазақстан облысы')
    button_10 = InlineKeyboardButton(text='Ақмола облысы', callback_data='Ақмола облысы')
    button_11 = InlineKeyboardButton(text='Ақтөбе облысы', callback_data='Ақтөбе облысы')
    button_12 = InlineKeyboardButton(text='Павлодар облысы', callback_data='Павлодар облысы')
    button_13 = InlineKeyboardButton(text='Солтүстік Қазақстан облысы', callback_data='Солтүстік Қазақстан облысы')
    button_15 = InlineKeyboardButton(text='Алматы облысы', callback_data='Алматы облысы')

    button_14 = InlineKeyboardButton(text='Нұр-Сұлтан', callback_data='Нұр-Сұлтан')
    button_16 = InlineKeyboardButton(text='Алматы қаласы', callback_data='Алматы қаласы')
    button_17 = InlineKeyboardButton(text='Шымкент қаласы', callback_data='Шымкент қаласы')

    markup_url.add(button_1).add(button_2).add(button_3).add(button_4).add(button_5).add(button_6).add(button_7).\
        add(button_8).add(button_9).add(button_10).add(button_11).add(button_12).add(button_13).add(button_14).\
        add(button_15).add(button_16).add(button_17)

    bot.delete_message(chat_id=id, message_id=message_id)
    bot.send_message(chat_id=id, text='\n\nТаңдаңыз...\n\n', reply_markup=markup_url)


def select_class(id, message_id):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='1 класс', callback_data='1 класс')
    button_2 = InlineKeyboardButton(text='2 класс', callback_data='2 класс')
    button_3 = InlineKeyboardButton(text='3 класс', callback_data='3 класс')
    button_4 = InlineKeyboardButton(text='4 класс', callback_data='4 класс')
    button_5 = InlineKeyboardButton(text='5 класс', callback_data='5 класс')
    button_6 = InlineKeyboardButton(text='6 класс', callback_data='6 класс')
    button_7 = InlineKeyboardButton(text='7 класс', callback_data='7 класс')
    button_8 = InlineKeyboardButton(text='8 класс', callback_data='8 класс')
    button_9 = InlineKeyboardButton(text='9 класс', callback_data='9 класс')
    button_10 = InlineKeyboardButton(text='10 класс', callback_data='10 класс')
    button_11 = InlineKeyboardButton(text='11 класс', callback_data='11 класс')
    button_teach = InlineKeyboardButton(text='Преподаватель', callback_data='Преподаватель')

    markup_url.add(button_1, button_2, button_3).add(button_4, button_5, button_6).add(button_7,
        button_8, button_9).add(button_10, button_11).add(button_teach)
    try:
        bot.delete_message(id, message_id)
    except ApiTelegramException:
        pass
    bot.send_message(chat_id=id, text='\n\nВыберите класс...\n\n', reply_markup=markup_url)


def select_class_kz(id, message_id):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='1 сынып', callback_data='1 сынып')
    button_2 = InlineKeyboardButton(text='2 сынып', callback_data='2 сынып')
    button_3 = InlineKeyboardButton(text='3 сынып', callback_data='3 сынып')
    button_4 = InlineKeyboardButton(text='4 сынып', callback_data='4 сынып')
    button_5 = InlineKeyboardButton(text='5 сынып', callback_data='5 сынып')
    button_6 = InlineKeyboardButton(text='6 сынып', callback_data='6 сынып')
    button_7 = InlineKeyboardButton(text='7 сынып', callback_data='7 сынып')
    button_8 = InlineKeyboardButton(text='8 сынып', callback_data='8 сынып')
    button_9 = InlineKeyboardButton(text='9 сынып', callback_data='9 сынып')
    button_10 = InlineKeyboardButton(text='10 сынып', callback_data='10 сынып')
    button_11 = InlineKeyboardButton(text='11 сынып', callback_data='11 сынып')
    button_teach = InlineKeyboardButton(text='Мұғалім', callback_data='Мұғалім')

    markup_url.add(button_1, button_2, button_3).add(button_4, button_5, button_6).add(button_7,
        button_8, button_9).add(button_10, button_11).add(button_teach)
    try:
        bot.delete_message(id, message_id)
    except ApiTelegramException:
        pass
    bot.send_message(chat_id=id, text='\n\nСыныпты таңдаңыз...\n\n', reply_markup=markup_url)


@bot.callback_query_handler(func=lambda callback: callback.data == '11 класс')
def send_class(callback):
    send_class_info(callback)


@bot.callback_query_handler(func=lambda callback: callback.data == '10 класс')
def send_class(callback):
    send_class_info(callback)


@bot.callback_query_handler(func=lambda callback: callback.data == '9 класс')
def send_class(callback):
    send_class_info(callback)


@bot.callback_query_handler(func=lambda callback: callback.data == '8 класс')
def send_class(callback):
    send_class_info(callback)


@bot.callback_query_handler(func=lambda callback: callback.data == '7 класс')
def send_class(callback):
    send_class_info(callback)


@bot.callback_query_handler(func=lambda callback: callback.data == '6 класс')
def send_class(callback):
    send_class_info(callback)


@bot.callback_query_handler(func=lambda callback: callback.data == '5 класс')
def send_class(callback):
    send_class_info(callback)


@bot.callback_query_handler(func=lambda callback: callback.data == '4 класс')
def send_class(callback):
    send_class_info(callback)


@bot.callback_query_handler(func=lambda callback: callback.data == '3 класс')
def send_class(callback):
    send_class_info(callback)


@bot.callback_query_handler(func=lambda callback: callback.data == '2 класс')
def send_class(callback):
    send_class_info(callback)


@bot.callback_query_handler(func=lambda callback: callback.data == '1 класс')
def send_class(callback):
    send_class_info(callback)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Преподаватель')
def send_class(callback):
    send_class_info(callback)

################################################################################################          KZ


@bot.callback_query_handler(func=lambda callback: callback.data == '1 сынып')
def send_class(callback):
    send_class_info(callback, 'kz')


@bot.callback_query_handler(func=lambda callback: callback.data == '2 сынып')
def send_class(callback):
    send_class_info(callback, 'kz')


@bot.callback_query_handler(func=lambda callback: callback.data == '3 сынып')
def send_class(callback):
    send_class_info(callback, 'kz')


@bot.callback_query_handler(func=lambda callback: callback.data == '4 сынып')
def send_class(callback):
    send_class_info(callback, 'kz')


@bot.callback_query_handler(func=lambda callback: callback.data == '5 сынып')
def send_class(callback):
    send_class_info(callback, 'kz')


@bot.callback_query_handler(func=lambda callback: callback.data == '6 сынып')
def send_class(callback):
    send_class_info(callback, 'kz')


@bot.callback_query_handler(func=lambda callback: callback.data == '7 сынып')
def send_class(callback):
    send_class_info(callback, 'kz')


@bot.callback_query_handler(func=lambda callback: callback.data == '8 сынып')
def send_class(callback):
    send_class_info(callback, 'kz')


@bot.callback_query_handler(func=lambda callback: callback.data == '9 сынып')
def send_class(callback):
    send_class_info(callback, 'kz')


@bot.callback_query_handler(func=lambda callback: callback.data == '10 сынып')
def send_class(callback):
    send_class_info(callback, 'kz')


@bot.callback_query_handler(func=lambda callback: callback.data == '11 сынып')
def send_class(callback):
    send_class_info(callback, 'kz')


@bot.callback_query_handler(func=lambda callback: callback.data == 'Мұғалім')
def send_class(callback):
    send_class_info(callback, 'kz')


def password_gen():
    dictionary = ascii_letters + digits
    password = ''
    for _ in range(8):
        password += random.choice(dictionary)
    return password.encode('utf-8')

@bot.callback_query_handler(func=lambda callback: callback.data == 'Сменить класс')
def edit_class(callback):
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    global class_flag
    class_flag = 1
    select_class(callback.message.chat.id, callback.message.message_id)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Сменить класс kz')
def edit_class(callback):
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    global class_flag
    class_flag = 1
    select_class_kz(callback.message.chat.id, callback.message.message_id)


# def status_kz(id):
#     markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     button_teacher = KeyboardButton('Мұғалім')
#     button_student = KeyboardButton('Оқушы')
#     button_alippe = KeyboardButton('Bilgen Әліппе')
#     markup.add(button_teacher).add(button_student).add(button_alippe)
#     bot.send_message(chat_id=id, text='Дәрежеңіз', reply_markup=markup)
#
#
# def status_ru(id):
#     markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     button_teacher = KeyboardButton('Преподаватель')
#     button_student = KeyboardButton('Ученик')
#     markup.add(button_teacher).add(button_student)
#     bot.send_message(chat_id=id, text='Ваш статус', reply_markup=markup)


def alippe(id):
    markup = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Сатып алу', url='wa.me/77783873039')
    button_2 = InlineKeyboardButton(text='Видео нұсқаулық', callback_data='Видео нұсқаулық')

    markup.add(button_1).add(button_2)

    bot.send_message(chat_id=id, text=alippe_txt, reply_markup=markup)


def info_1(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button_1 = KeyboardButton('Tanymger Expert')
    button_2 = KeyboardButton('Tanymger Tech')
    button_3 = KeyboardButton('Oysana')
    button_4 = KeyboardButton('Тоғызқұмалақ')

    button_back = KeyboardButton('Кері оралy 🔙')  # y

    markup.add(button_1).add(button_2).add(button_3).add(button_4).add(button_back)
    bot.send_message(chat_id=id, text=info_1_str, reply_markup=markup)


def info_1_2(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button_1 = KeyboardButton('Tanymger Tech')
    button_2 = KeyboardButton('Білікті педагог')

    button_back = KeyboardButton('Кері оралy 🔙')  # y

    markup.add(button_1).add(button_2).add(button_back)
    bot.send_message(chat_id=id, text=info_1_2_str, reply_markup=markup)


def teacher_kz(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button_1 = KeyboardButton('Кyрстар')  # y
    button_2 = KeyboardButton('Олимпиадалаp')  # p

    button_back = KeyboardButton('Кері оралу 🔙')

    markup.add(button_1).add(button_2).add(button_back)
    bot.send_message(chat_id=id, text='Tаңдаңыз', reply_markup=markup)


def student_kz(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button_1 = KeyboardButton('Курстар')
    button_2 = KeyboardButton('Олимпиадалар')

    button_back = KeyboardButton('Кері оралу 🔙')

    markup.add(button_1).add(button_2).add(button_back)
    bot.send_message(chat_id=id, text='Tаңдаңыз', reply_markup=markup)


def info_2(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button_1 = KeyboardButton('Bilgen UBT')
    button_2 = KeyboardButton('Bilgen Tech')

    button_back = KeyboardButton('Кері  оралу 🔙')

    markup.add(button_1).add(button_2).add(button_back)
    bot.send_message(chat_id=id, text=info_2_str, reply_markup=markup)


def info_3(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button_1 = KeyboardButton('Bilgen Baige/Alaman')
    button_2 = KeyboardButton('Bala/Bilik Time')
    button_3 = KeyboardButton('Bilgen Sprint')

    button_back = KeyboardButton('Кері  оралу 🔙')

    markup.add(button_1).add(button_2).add(button_3).add(button_back)
    bot.send_message(chat_id=id, text=info_3_str, reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Курс 0')
def info_4(callback: CallbackQuery):
    markup = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton('Tanymger  Expert', callback_data='C_TE_ru')
    button_2 = InlineKeyboardButton('Tanymger  Tech', callback_data='C_TT_ru')
    button_3 = InlineKeyboardButton('Toғызқұмалақ', callback_data='C_9qq_ru')

    button_menu = InlineKeyboardButton(text=f'🎛 Главное меню', callback_data='ru')

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    markup.add(button_1).add(button_2).add(button_3).add(button_menu)
    bot.send_message(chat_id=callback.message.chat.id, text=info_4_str, reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'C_TE_ru')
def tan_ex(callback: CallbackQuery):
    send_info(id=callback.message.chat.id, text=choose_ru, lng='ru', condition='Tanymger  Expert', flag=1)


@bot.callback_query_handler(func=lambda callback: callback.data == 'C_TT_ru')
def tan_tech(callback: CallbackQuery):
    send_info(id=callback.message.chat.id, text=choose_ru, lng='ru', condition='Tanymger  Tech', flag=1)


@bot.callback_query_handler(func=lambda callback: callback.data == 'C_9qq_ru')
def tog_qq(callback: CallbackQuery):
    send_info(id=callback.message.chat.id, text=choose_ru, lng='ru', condition='Toғызқұмалақ', flag=1)


def mugalim(callback: CallbackQuery):
    markup = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton('Tanymger Expert', callback_data='C_TE_kz')
    button_2 = InlineKeyboardButton('Tanymger Tech', callback_data='C_TT_kz')
    button_3 = InlineKeyboardButton('Тоғызқұмалақ', callback_data='C_9qq_kz')

    button_menu = InlineKeyboardButton(text=f'🎛 Басты бет', callback_data='kz')

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    markup.add(button_1).add(button_2).add(button_3).add(button_menu)
    bot.send_message(chat_id=callback.message.chat.id, text=info_1_str, reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Курс 0kz')
def info_4(callback: CallbackQuery):
    mugalim(callback)


@bot.callback_query_handler(func=lambda callback: callback.data == 'C_TE_kz')
def tan_ex(callback: CallbackQuery):
    send_info(id=callback.message.chat.id, text=choose_kz, lng='kz', condition='Tanymger Expert', flag=1)


@bot.callback_query_handler(func=lambda callback: callback.data == 'C_TT_kz')
def tan_tech(callback: CallbackQuery):
    send_info(id=callback.message.chat.id, text=choose_kz, lng='kz', condition='Tanymger Tech', flag=1)


@bot.callback_query_handler(func=lambda callback: callback.data == 'C_9qq_kz')
def tog_qq(callback: CallbackQuery):
    send_info(id=callback.message.chat.id, text=choose_kz, lng='kz', condition='Тоғызқұмалақ', flag=1)


def info_4_2(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button_1 = KeyboardButton('Tanymger  Tech')
    button_2 = KeyboardButton('Квалифицированный педагог')

    button_back = KeyboardButton('Назaд 🔙')  # a''

    markup.add(button_1).add(button_2).add(button_back)
    bot.send_message(chat_id=id, text=info_4_2_str, reply_markup=markup)


def student_ru(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button_1 = KeyboardButton('Курсы')
    button_2 = KeyboardButton('Олимпиады')

    button_back = KeyboardButton('Назад 🔙')

    markup.add(button_1).add(button_2).add(button_back)
    bot.send_message(chat_id=id, text='Выберите', reply_markup=markup)


def teacher_ru(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button_1 = KeyboardButton('Kypсы')  # Kyp
    button_2 = KeyboardButton('Oлимпиады')  # O

    button_back = KeyboardButton('Назад 🔙')

    markup.add(button_1).add(button_2).add(button_back)
    bot.send_message(chat_id=id, text='Выберите', reply_markup=markup)

#
# @bot.callback_query_handler(func=lambda callback: callback.data == 'Курс ')
# def info_5(callback: CallbackQuery):
#     markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#
#     button_1 = KeyboardButton('Bilgen  Tech')
#
#     button_back = KeyboardButton('Haзaд 🔙')  # Ha
#
#     markup.add(button_1).add(button_back)
#     bot.send_message(chat_id=callback.message.chat.id, text=info_5_str, reply_markup=markup)


def info_6(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button_1 = KeyboardButton('Bilgen  Baige/Alaman')
    button_2 = KeyboardButton('Bala/Bilik  Time')
    button_3 = KeyboardButton('Bilgen  Sprint')

    button_back = KeyboardButton('Haзaд 🔙')  # Ha

    markup.add(button_1).add(button_2).add(button_3).add(button_back)
    bot.send_message(chat_id=id, text=info_6_str, reply_markup=markup)


def send_info(id, text, lng, condition, flag=0):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Тіркелу', url='https://bilgen.academy/intranet/custom_signup_new.php')
    button_2 = InlineKeyboardButton(text='Төлем жүйесі', callback_data='Пополнение kz')
    button_3 = InlineKeyboardButton(text='Регистрация', url='https://bilgen.academy/intranet/custom_signup_new.php')
    button_4 = InlineKeyboardButton(text='Способ оплаты', url='https://bilgen.academy/api/gateway/')

    if condition != 'Квалифицированный педагог':
        button_chat_kz = InlineKeyboardButton(text=f'{condition} Чатқа өту', callback_data=f'{condition} Чатқа өту')
        button_chat_ru = InlineKeyboardButton(text=f'Перейти в чат {condition}', callback_data=
                                                    f'Перейти в чат {condition}')
    else:
        button_chat_kz = InlineKeyboardButton(text=f'Чатқа өту', callback_data=f'Чатқа өту')
        button_chat_ru = InlineKeyboardButton(text=f'Перейти в чат', callback_data='Перейти в чат')

    button_5 = InlineKeyboardButton(text=text, callback_data=condition)

    if lng == 'kz':
        if flag:
            markup_url.add(button_1).add(button_2).add(button_chat_kz).add(button_5)
        else:
            markup_url.add(button_1).add(button_2).add(button_5)
        bot.send_message(chat_id=id, text='Таңдаңыз...', reply_markup=markup_url)
    else:
        if flag:
            markup_url.add(button_3).add(button_4).add(button_chat_ru).add(button_5)
        else:
            markup_url.add(button_3).add(button_4).add(button_5)
        bot.send_message(chat_id=id, text='Выберите...', reply_markup=markup_url)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{togyzqumalaq_kz} Чатқа өту')
def tgz_chat_kz(callback):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Атырау облысы', url='https://t.me/atyrau_9qq')
    button_2 = InlineKeyboardButton(text='Шығыс Қазақстан облысы',
                                    url='https://t.me/joinchat/Hgaq8BcHjsy_Doyimn4-LA')
    button_3 = InlineKeyboardButton(text='Қостанай облысы', url='https://t.me/joinchat/Hgaq8BddeqgB4rTUxXeMqQ')
    button_4 = InlineKeyboardButton(text='Маңғыстау облысы', url='https://t.me/joinchat/Hgaq8BiIOvjvPZtfTmaIFA')
    button_5 = InlineKeyboardButton(text='Қызылорда облысы', url='https://t.me/joinchat/Hgaq8BkcHlc7duFH9Fxykg')
    button_6 = InlineKeyboardButton(text='Жамбыл облысы', url='https://t.me/joinchat/Hgaq8Bko-L8-cFQm01Fy4A')
    button_7 = InlineKeyboardButton(text='Қарағанды облысы', url='https://t.me/joinchat/Hgaq8Bmgu-tRVqMtL9bprA')
    button_8 = InlineKeyboardButton(text='Шымкент облысы', url='https://t.me/joinchat/Hgaq8BnOyF-yzft6cGi_-Q')
    button_9 = InlineKeyboardButton(text='Батыс Қазақстан облысы', url='https://t.me/joinchat/Hgaq8BrDRa6bFe3UYnLdiw')
    button_10 = InlineKeyboardButton(text='Ақмола облысы', url='https://t.me/joinchat/Hgaq8By9R9Z6wP9w9Om8Dw')
    button_11 = InlineKeyboardButton(text='Ақтөбе облысы', url='https://t.me/joinchat/Hgaq8BzAHjOrWyIBAmAh4Q')
    button_12 = InlineKeyboardButton(text='Павлодар облысы', url='https://t.me/joinchat/Hgaq8BvBsGyRMccmS3Q-Iw')
    button_13 = InlineKeyboardButton(text='Солтүстік Қазақстан облысы',
                                     url='https://t.me/joinchat/Hgaq8B2zlfaZwLbtMljm_A')
    button_14 = InlineKeyboardButton(text='Нұр-Сұлтан', url='https://t.me/joinchat/Hgaq8Bn74OCEEBkLbOPYlg')
    button_15 = InlineKeyboardButton(text='Алматы облысы', url='https://t.me/almaty_oblysy_9qq')

    button_16 = InlineKeyboardButton(text='Алматы қаласы', callback_data='Алматы қаласы 9QQ')

    markup_url.add(button_1).add(button_2).add(button_3).add(button_4).add(button_5).add(button_6).add(button_7).\
        add(button_8).add(button_9).add(button_10).add(button_11).add(button_12).add(button_13).add(button_14).\
        add(button_15).add(button_16)
    bot.send_message(chat_id=callback.message.chat.id, text='\n\nТаңдаңыз...\n\n', reply_markup=markup_url)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Перейти в чат {togyzqumalaq_ru}')
def tgz_chat_ru(callback):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Атырауская область', url='https://t.me/atyrau_9qq')
    button_2 = InlineKeyboardButton(text='Восточно-Казахстанская область',
                                    url='https://t.me/joinchat/Hgaq8BcHjsy_Doyimn4-LA')
    button_3 = InlineKeyboardButton(text='Костанайская область', url='https://t.me/joinchat/Hgaq8BddeqgB4rTUxXeMqQ')
    button_4 = InlineKeyboardButton(text='Мангистауская область', url='https://t.me/joinchat/Hgaq8BiIOvjvPZtfTmaIFA')
    button_5 = InlineKeyboardButton(text='Кызылординская область', url='https://t.me/joinchat/Hgaq8BkcHlc7duFH9Fxykg')
    button_6 = InlineKeyboardButton(text='Жамбылская область', url='https://t.me/joinchat/Hgaq8Bko-L8-cFQm01Fy4A')
    button_7 = InlineKeyboardButton(text='Карагандинская область', url='https://t.me/joinchat/Hgaq8Bmgu-tRVqMtL9bprA')
    button_8 = InlineKeyboardButton(text='Шымкентская область', url='https://t.me/joinchat/Hgaq8BnOyF-yzft6cGi_-Q')
    button_9 = InlineKeyboardButton(text='Западно-Казахстанская область',
                                    url='https://t.me/joinchat/Hgaq8BrDRa6bFe3UYnLdiw')
    button_10 = InlineKeyboardButton(text='Акмолинская область', url='https://t.me/joinchat/Hgaq8By9R9Z6wP9w9Om8Dw')
    button_11 = InlineKeyboardButton(text='Актюбинская область', url='https://t.me/joinchat/Hgaq8BzAHjOrWyIBAmAh4Q')
    button_12 = InlineKeyboardButton(text='Павлодарская область', url='https://t.me/joinchat/Hgaq8BvBsGyRMccmS3Q-Iw')
    button_13 = InlineKeyboardButton(text='Северно-Казахстанская область',
                                     url='https://t.me/joinchat/Hgaq8B2zlfaZwLbtMljm_A')
    button_14 = InlineKeyboardButton(text='Нур-Султан', url='https://t.me/joinchat/Hgaq8Bn74OCEEBkLbOPYlg')
    button_15 = InlineKeyboardButton(text='Алматинская область', url='https://t.me/almaty_oblysy_9qq')

    button_16 = InlineKeyboardButton(text='Алматы', callback_data='Алматы 9QQ')

    markup_url.add(button_1).add(button_2).add(button_3).add(button_4).add(button_5).add(button_6).add(button_7).\
        add(button_8).add(button_9).add(button_10).add(button_11).add(button_12).add(button_13).add(button_14).\
        add(button_15).add(button_16)
    bot.send_message(chat_id=callback.message.chat.id, text='\n\nВыберите...\n\n', reply_markup=markup_url)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Алматы қаласы 9QQ')
def tgz_almaty_kz(callback):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Жетісу ауданы', url='https://t.me/joinchat/Hgaq8BfxmkZ0tzfZ7Hx6Hw')
    button_2 = InlineKeyboardButton(text='Бостандық ауданы', url='https://t.me/joinchat/Hgaq8BgRw9wL03UMareBZQ')
    button_3 = InlineKeyboardButton(text='Алмалы ауданы', url='https://t.me/joinchat/Hgaq8BkDwijojNOsQa4TWQ')
    button_4 = InlineKeyboardButton(text='Алатау ауданы', url='https://t.me/joinchat/Hgaq8B09m0FzwpB17GQmfg')
    button_5 = InlineKeyboardButton(text='Наурызбай ауданы', url='https://t.me/joinchat/Hgaq8BsanCBNBwJwV0aGKA')
    button_6 = InlineKeyboardButton(text='Медеу ауданы', url='https://t.me/joinchat/Hgaq8BtnQc4WZAt_Nw1m1w')
    button_7 = InlineKeyboardButton(text='Түрксіб ауданы', url='https://t.me/joinchat/Hgaq8BjlBYjP_hwGAmym9A')
    button_8 = InlineKeyboardButton(text='Әуезов ауданы', url='https://t.me/joinchat/Hgaq8Flgq25rGtZ0Xdht6w')

    markup_url.add(button_1).add(button_2).add(button_3).add(button_4).add(button_5).add(button_6).add(button_7). \
        add(button_8)
    bot.send_message(chat_id=callback.message.chat.id, text='\n\nТаңдаңыз...\n\n', reply_markup=markup_url)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Алматы 9QQ')
def tgz_almaty_ru(callback):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Жетысуский район', url='https://t.me/joinchat/Hgaq8BfxmkZ0tzfZ7Hx6Hw')
    button_2 = InlineKeyboardButton(text='Бостандыкский район', url='https://t.me/joinchat/Hgaq8BgRw9wL03UMareBZQ')
    button_3 = InlineKeyboardButton(text='Алмалинский район', url='https://t.me/joinchat/Hgaq8BkDwijojNOsQa4TWQ')
    button_4 = InlineKeyboardButton(text='Алатауский район', url='https://t.me/joinchat/Hgaq8B09m0FzwpB17GQmfg')
    button_5 = InlineKeyboardButton(text='Наурызбайский район', url='https://t.me/joinchat/Hgaq8BsanCBNBwJwV0aGKA')
    button_6 = InlineKeyboardButton(text='Медеуский район', url='https://t.me/joinchat/Hgaq8BtnQc4WZAt_Nw1m1w')
    button_7 = InlineKeyboardButton(text='Турксибский район', url='https://t.me/joinchat/Hgaq8BjlBYjP_hwGAmym9A')
    button_8 = InlineKeyboardButton(text='Ауезовский район', url='https://t.me/joinchat/Hgaq8Flgq25rGtZ0Xdht6w')

    markup_url.add(button_1).add(button_2).add(button_3).add(button_4).add(button_5).add(button_6).add(button_7). \
        add(button_8)
    bot.send_message(chat_id=callback.message.chat.id, text='\n\nВыберите...\n\n', reply_markup=markup_url)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{tanymger_tech_kz} Чатқа өту')
def tanymger_tech_chat_kz(callback):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Tanymger Tech', url='https://t.me/joinchat/IfxKFBQqT4211bJqMtVcKg')

    markup_url.add(button_1)
    bot.send_message(chat_id=callback.message.chat.id, text='\n\nТаңдаңыз...\n\n', reply_markup=markup_url)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Перейти в чат {tanymger_tech_ru}')
def tanymger_tech_chat_kz(callback):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Tanymger Tech', url='https://t.me/joinchat/IfxKFBQqT4211bJqMtVcKg')

    markup_url.add(button_1)
    bot.send_message(chat_id=callback.message.chat.id, text='\n\nВыберите...\n\n', reply_markup=markup_url)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{tanymger_expert_kz} Чатқа өту')
def tanymger_expert_chat_kz(callback):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Tanymger Expert', url='https://t.me/joinchat/IfxKFBpLXpRAh2DHvgyjLQ')

    markup_url.add(button_1)
    bot.send_message(chat_id=callback.message.chat.id, text='\n\nТаңдаңыз...\n\n', reply_markup=markup_url)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Перейти в чат {tanymger_expert_ru}')
def tanymger_expert_chat_kz(callback):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Tanymger Expert', url='https://t.me/joinchat/IfxKFBpLXpRAh2DHvgyjLQ')

    markup_url.add(button_1)
    bot.send_message(chat_id=callback.message.chat.id, text='\n\nВыберите...\n\n', reply_markup=markup_url)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Пополнение kz')
def reply_video(callback):
    try:
        markup = InlineKeyboardMarkup()
        button_home = InlineKeyboardButton(text='🎛 Басты бет', callback_data='kz')
        markup.add(button_home)

        bot.send_video(chat_id=callback.message.chat.id, data=open('./Pay_method/KASPI.mp4', 'rb'))
        bot.send_message(chat_id=callback.message.chat.id, text='https://kaspi.kz/pay/education', reply_markup=markup)
    except ConnectionError:
        pass


@bot.callback_query_handler(func=lambda callback: callback.data == 'Видео нұсқаулық')
def reply_alippe(callback):
    try:
        bot.send_video(chat_id=callback.message.chat.id, data=open('./alippe/BilGen Alippe.mp4', 'rb'))
    except ConnectionError:
        pass


##############################################################################################  KZ
##############################################################################################  KZ
##############################################################################################  KZ
##############################################################################################  TEACHER
@bot.callback_query_handler(func=lambda callback: callback.data == 'Tanymger Expert')
def reply_condition_tanymger_kz(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(tanymger_ru_path, 'rb'))
    except ConnectionError:
        pass

##############################################################################################
@bot.callback_query_handler(func=lambda callback: callback.data == 'Tanymger Tech')
def reply_condition_tan_tech_kz(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(tech_kz_path, 'rb'))
    except ConnectionError:
        pass

##############################################################################################
@bot.callback_query_handler(func=lambda callback: callback.data == 'Bilgen Tech' or callback.data == 'Tanymger Tech')
def reply_condition_bilgen_tech_kz(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(bilgen_tech_path, 'rb'))
    except ConnectionError:
        pass

##############################################################################################
@bot.callback_query_handler(func=lambda callback: callback.data == 'Oysana')
def reply_condition_oysana_kz(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(oys_kz_path, 'rb'))
    except ConnectionError:
        pass

##############################################################################################
@bot.callback_query_handler(func=lambda callback: callback.data == 'Тоғызқұмалақ')
def reply_condition_togyz_kz(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(tog_kz_path, 'rb'))
    except ConnectionError:
        pass

##############################################################################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Пол{pedagog_kz}')
def reply_condition_teacher_kz(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(techr_kz_path, 'rb'))
    except ConnectionError:
        pass

##############################################################################################  KZ
##############################################################################################  STUDENT
@bot.callback_query_handler(func=lambda callback: callback.data == 'Bilgen UBT')
def reply_condition_ubt_kz(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(ubt_kz_path, 'rb'))
    except ConnectionError:
        pass

##############################################################################################
@bot.callback_query_handler(func=lambda callback: callback.data == 'Bilgen Baige/Alaman')
def reply_condition_alaman_kz(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(baige_kz_path, 'rb'))
    except ConnectionError:
        pass

##############################################################################################
@bot.callback_query_handler(func=lambda callback: callback.data == 'Bala/Bilik Time')
def reply_condition_bilik_kz(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(bilik_kz_path, 'rb'))
    except ConnectionError:
        pass
##############################################################################################
@bot.callback_query_handler(func=lambda callback: callback.data == 'Bilgen Sprint')
def reply_condition_sprint_kz(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(bilgen_sprint_path_kz, 'rb'))
    except ConnectionError:
        pass
##############################################################################################


##############################################################################################  RU
##############################################################################################  RU
##############################################################################################  RU
##############################################################################################  TEACHER
@bot.callback_query_handler(func=lambda callback: callback.data == 'Tanymger  Expert')
def reply_condition_tanymger_ru(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(tanymger_ru_path, 'rb'))
    except ConnectionError:
        pass

##############################################################################################
@bot.callback_query_handler(func=lambda callback: callback.data == 'Tanymger  Tech')
def reply_condition_bilgen_tech_ru(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(tech_ru_path, 'rb'))
    except ConnectionError:
        pass

##############################################################################################
@bot.callback_query_handler(func=lambda callback: callback.data == 'Toғызқұмалақ')
def reply_condition_togyz_ru(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(tog_ru_path, 'rb'))
    except ConnectionError:
        pass

##############################################################################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Пол{pedagog_ru}')
def reply_condition_teacher_ru(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(techr_ru_path, 'rb'))
    except ConnectionError:
        pass

##############################################################################################  RU
##############################################################################################  STUDENT
##############################################################################################
@bot.callback_query_handler(func=lambda callback: callback.data == 'Bilgen  Baige/Alaman')
def reply_condition_alaman_ru(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(baige_ru_path, 'rb'))
    except ConnectionError:
        pass

##############################################################################################
@bot.callback_query_handler(func=lambda callback: callback.data == 'Bala/Bilik  Time')
def reply_condition_bilik_ru(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(bilik_ru_path, 'rb'))
    except ConnectionError:
        pass

############################################################################################    TIME RU
############################################################################################    TIME RU
@bot.callback_query_handler(func=lambda callback: callback.data == f'{matem}11')
def b_mat_ru_11(callback):
    time_ru.b_mat_11(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum}11')
def b_gum_ru_11(callback):
    time_ru.b_gum_11(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_mat_11_ru')
def mat_test(callback):
    start_test(callback, 1000, 238)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_gum_11_ru')
def gum_test(callback):
    start_test(callback, 1000, 248)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{matem}10')
def b_mat_ru_10(callback):
    time_ru.b_mat_10(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum}10')
def b_gum_ru_10(callback):
    time_ru.b_gum_10(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_mat_10_ru')
def mat_test(callback):
    start_test(callback, 1000, 232)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_gum_10_ru')
def gum_test(callback):
    start_test(callback, 1000, 247)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{matem}9')
def b_mat_ru_9(callback):
    time_ru.b_mat_9(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum}9')
def b_gum_ru_9(callback):
    time_ru.b_gum_9(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_mat_9_ru')
def mat_test(callback):
    start_test(callback, 1000, 225)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_gum_9_ru')
def gum_test(callback):
    start_test(callback, 1000, 245)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{matem}8')
def b_mat_ru_8(callback):
    time_ru.b_mat_8(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum}8')
def b_gum_ru_8(callback):
    time_ru.b_gum_8(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_mat_8_ru')
def mat_test(callback):
    start_test(callback, 1000, 224)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_gum_8_ru')
def gum_test(callback):
    start_test(callback, 1000, 244)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{matem}7')
def b_mat_ru_7(callback):
    time_ru.b_mat_7(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum}7')
def b_gum_ru_7(callback):
    time_ru.b_gum_7(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_mat_7_ru')
def mat_test(callback):
    start_test(callback, 1000, 223)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_gum_7_ru')
def gum_test(callback):
    start_test(callback, 1000, 243)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{matem}6')
def b_mat_ru_6(callback):
    time_ru.b_mat_6(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum}6')
def b_gum_ru_6(callback):
    time_ru.b_gum_6(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_mat_6_ru')
def mat_test(callback):
    start_test(callback, 1000, 222)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_gum_6_ru')
def gum_test(callback):
    start_test(callback, 1000, 242)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{matem}5')
def b_mat_ru_5(callback):
    time_ru.b_mat_5(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum}5')
def b_gum_ru_5(callback):
    time_ru.b_gum_5(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_mat_5_ru')
def mat_test(callback):
    start_test(callback, 1000, 158)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_gum_5_ru')
def gum_test(callback):
    start_test(callback, 1000, 241)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_ru}4')
def b_gum_ru_4(callback):
    time_ru.b_time_4(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_time_4_ru')
def mat_test(callback):
    start_test(callback, 1000, 162)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_ru}3')
def b_gum_ru_3(callback):
    time_ru.b_time_3(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_time_3_ru')
def mat_test(callback):
    start_test(callback, 1000, 161)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_ru}2')
def b_gum_ru_2(callback):
    time_ru.b_time_2(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_time_2_ru')
def mat_test(callback):
    start_test(callback, 1000, 160)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_ru}1')
def b_gum_ru_1(callback):
    time_ru.b_time_1(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_time_1_ru')
def mat_test(callback):
    start_test(callback, 1000, 159)
############################################################################################    TIME RU
############################################################################################    TIME RU

############################################################################################    TIME KZ
############################################################################################    TIME KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'{mat_kz}11')
def b_mat_kz_11(callback):
    time_kz.b_mat_11(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum_kz}11')
def b_gum_kz_11(callback):
    time_kz.b_gum_11(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_mat_11_kz')
def mat_test(callback):
    start_test(callback, 1000, 238)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_gum_11_kz')
def gum_test(callback):
    start_test(callback, 1000, 248)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{mat_kz}10')
def b_mat_kz_10(callback):
    time_kz.b_mat_10(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum_kz}10')
def b_gum_kz_10(callback):
    time_kz.b_gum_10(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_mat_10_kz')
def mat_test(callback):
    start_test(callback, 1000, 232)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_gum_10_kz')
def gum_test(callback):
    start_test(callback, 1000, 247)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{mat_kz}9')
def b_mat_kz_9(callback):
    time_kz.b_mat_9(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum_kz}9')
def b_gum_kz_9(callback):
    time_kz.b_gum_9(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_mat_9_kz')
def mat_test(callback):
    start_test(callback, 1000, 225)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_gum_9_kz')
def gum_test(callback):
    start_test(callback, 1000, 245)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{mat_kz}8')
def b_mat_kz_8(callback):
    time_kz.b_mat_8(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum_kz}8')
def b_gum_kz_8(callback):
    time_kz.b_gum_8(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_mat_8_kz')
def mat_test(callback):
    start_test(callback, 1000, 224)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_gum_8_kz')
def gum_test(callback):
    start_test(callback, 1000, 244)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{mat_kz}7')
def b_mat_kz_7(callback):
    time_kz.b_mat_7(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum_kz}7')
def b_gum_kz_7(callback):
    time_kz.b_gum_7(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_mat_7_kz')
def mat_test(callback):
    start_test(callback, 1000, 223)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_gum_7_kz')
def gum_test(callback):
    start_test(callback, 1000, 243)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{mat_kz}6')
def b_mat_kz_6(callback):
    time_kz.b_mat_6(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum_kz}6')
def b_gum_kz_6(callback):
    time_kz.b_gum_6(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_mat_6_kz')
def mat_test(callback):
    start_test(callback, 1000, 222)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_gum_6_kz')
def gum_test(callback):
    start_test(callback, 1000, 242)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{mat_kz}5')
def b_mat_kz_5(callback):
    time_kz.b_mat_5(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum_kz}5')
def b_gum_kz_5(callback):
    time_kz.b_gum_5(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_mat_5_kz')
def mat_test(callback):
    start_test(callback, 1000, 158)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_gum_5_kz')
def gum_test(callback):
    start_test(callback, 1000, 241)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_kz}4')
def b_gum_kz_4(callback):
    time_kz.b_time_4(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_time_4_kz')
def mat_test(callback):
    start_test(callback, 1000, 162)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_kz}3')
def b_gum_kz_3(callback):
    time_kz.b_time_3(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_time_3_kz')
def mat_test(callback):
    start_test(callback, 1000, 161)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_kz}2')
def b_gum_kz_2(callback):
    time_kz.b_time_2(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_time_2_kz')
def mat_test(callback):
    start_test(callback, 1000, 160)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_kz}1')
def b_gum_kz_1(callback):
    time_kz.b_time_1(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'b_time_1_kz')
def mat_test(callback):
    start_test(callback, 1000, 159)
############################################################################################    TIME kz
############################################################################################    TIME kz

############################################################################################    SPRINT 11 RU
############################################################################################    SPRINT 11 RU
############################################################################################    SPRINT 11 RU
@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_phys_11_ru')
def fiz_test(callback):
    start_test(callback, 350, 1783)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_11_ru')
def mat_test(callback):
    start_test(callback, 350, 1778)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_11_ru')
def kaz_test(callback):
    start_test(callback, 350, 1764)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_xim_11_ru')
def xim_test(callback):
    start_test(callback, 350, 1788)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_inf_11_ru')
def inf_test(callback):
    start_test(callback, 350, 1784)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hkz_11_ru')
def hkz_test(callback):
    start_test(callback, 350, 1771)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_bio_11_ru')
def bio_test(callback):
    start_test(callback, 350, 1840)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_11_ru')
def kazl_test(callback):
    start_test(callback, 350, 1864)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_ang_11_ru')
def ang_test(callback):
    start_test(callback, 350, 1853)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_geo_11_ru')
def geo_test(callback):
    start_test(callback, 350, 1850)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hm_11_ru')
def hm_test(callback):
    start_test(callback, 350, 503)

############################################################################################    SPRINT 11
@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}fiz 11')
def sprint_phys_ru_11(callback):
    sprint_11.sprint_subject_11_ru(callback, bot, 'phys')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}mat 11')
def sprint_mat_ru_11(callback):
    sprint_11.sprint_subject_11_ru(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kaz 11')
def sprint_kaz_ru_11(callback):
    sprint_11.sprint_subject_11_ru(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}xim 11')
def sprint_xim_ru_11(callback):
    sprint_11.sprint_subject_11_ru(callback, bot, 'xim')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}informatika 11')
def sprint_inf_11(callback):
    sprint_11.sprint_subject_11_ru(callback, bot, 'inf')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}hkz 11')
def sprint_hkz_ru_11(callback):
    sprint_11.sprint_subject_11_ru(callback, bot, 'hkz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}bio 11')
def sprint_bio_ru_11(callback):
    sprint_11.sprint_subject_11_ru(callback, bot, 'bio')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kazl 11')
def sprint_kazl_ru_11(callback):
    sprint_11.sprint_subject_11_ru(callback, bot, 'kazl')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}ang 11')
def sprint_ang_ru_11(callback):
    sprint_11.sprint_subject_11_ru(callback, bot, 'ang')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}geo 11')
def sprint_geo_ru_11(callback):
    sprint_11.sprint_subject_11_ru(callback, bot, 'geo')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}hm 11')
def sprint_hm_ru_11(callback):
    sprint_11.sprint_subject_11_ru(callback, bot, 'hm')
############################################################################################    SPRINT 11 RU
############################################################################################    SPRINT 11 RU // KZ
############################################################################################    SPRINT 11 KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_phys_11_kz')
def fiz_test(callback):
    start_test(callback, 350, 1783)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_11_kz')
def mat_test(callback):
    start_test(callback, 350, 1778)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_11_kz')
def kaz_test(callback):
    start_test(callback, 350, 1764)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_xim_11_kz')
def xim_test(callback):
    start_test(callback, 350, 1788)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_inf_11_kz')
def inf_test(callback):
    start_test(callback, 350, 1784)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hkz_11_kz')
def hkz_test(callback):
    start_test(callback, 350, 1771)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_bio_11_kz')
def bio_test(callback):
    start_test(callback, 350, 1840)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_11_kz')
def kazl_test(callback):
    start_test(callback, 350, 1864)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_ang_11_kz')
def ang_test(callback):
    start_test(callback, 350, 1853)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_geo_11_kz')
def geo_test(callback):
    start_test(callback, 350, 1850)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hm_11_kz')
def hm_test(callback):
    start_test(callback, 350, 503)

############################################################################################    SPRINT 11
@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}fiz 11')
def sprint_phys_kz_11(callback):
    sprint_11.sprint_subject_11_kz(callback, bot, 'phys')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}mat 11')
def sprint_mat_kz_11(callback):
    sprint_11.sprint_subject_11_kz(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kaz 11')
def sprint_kaz_kz_11(callback):
    sprint_11.sprint_subject_11_kz(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}xim 11')
def sprint_xim_kz_11(callback):
    sprint_11.sprint_subject_11_kz(callback, bot, 'xim')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}informatika 11')
def sprint_inf_11(callback):
    sprint_11.sprint_subject_11_kz(callback, bot, 'inf')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}hkz 11')
def sprint_hkz_kz_11(callback):
    sprint_11.sprint_subject_11_kz(callback, bot, 'hkz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}bio 11')
def sprint_bio_kz_11(callback):
    sprint_11.sprint_subject_11_kz(callback, bot, 'bio')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kazl 11')
def sprint_kazl_kz_11(callback):
    sprint_11.sprint_subject_11_kz(callback, bot, 'kazl')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}ang 11')
def sprint_ang_kz_11(callback):
    sprint_11.sprint_subject_11_kz(callback, bot, 'ang')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}geo 11')
def sprint_geo_kz_11(callback):
    sprint_11.sprint_subject_11_kz(callback, bot, 'geo')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}hm 11')
def sprint_hm_kz_11(callback):
    sprint_11.sprint_subject_11_kz(callback, bot, 'hm')
############################################################################################    SPRINT 11 kz
############################################################################################    SPRINT 11 kz
############################################################################################    SPRINT 11 kz


############################################################################################    SPRINT 10 RU
############################################################################################    SPRINT 10 RU
############################################################################################    SPRINT 10 RU
@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_phys_10_ru')
def fiz_test(callback):
    start_test(callback, 350, 1782)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_10_ru')
def mat_test(callback):
    start_test(callback, 350, 1777)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_10_ru')
def kaz_test(callback):
    start_test(callback, 350, 1763)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_xim_10_ru')
def xim_test(callback):
    start_test(callback, 350, 1787)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_inf_10_ru')
def inf_test(callback):
    start_test(callback, 350, 1784)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hkz_10_ru')
def hkz_test(callback):
    start_test(callback, 350, 1770)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_bio_10_ru')
def bio_test(callback):
    start_test(callback, 350, 1867)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_10_ru')
def kazl_test(callback):
    start_test(callback, 350, 1858)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_ang_10_ru')
def ang_test(callback):
    start_test(callback, 350, 1843)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_geo_10_ru')
def geo_test(callback):
    start_test(callback, 350, 1865)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hm_10_ru')
def hm_test(callback):
    start_test(callback, 350, 1862)

############################################################################################    SPRINT 10
@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}fiz 10')
def sprint_phys_ru_10(callback):
    sprint_10.sprint_subject_10_ru(callback, bot, 'phys')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}mat 10')
def sprint_mat_ru_10(callback):
    sprint_10.sprint_subject_10_ru(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kaz 10')
def sprint_kaz_ru_10(callback):
    sprint_10.sprint_subject_10_ru(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}xim 10')
def sprint_xim_ru_10(callback):
    sprint_10.sprint_subject_10_ru(callback, bot, 'xim')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}informatika 10')
def sprint_inf_10(callback):
    sprint_10.sprint_subject_10_ru(callback, bot, 'inf')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}hkz 10')
def sprint_hkz_ru_10(callback):
    sprint_10.sprint_subject_10_ru(callback, bot, 'hkz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}bio 10')
def sprint_bio_ru_10(callback):
    sprint_10.sprint_subject_10_ru(callback, bot, 'bio')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kazl 10')
def sprint_kazl_ru_10(callback):
    sprint_10.sprint_subject_10_ru(callback, bot, 'kazl')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}ang 10')
def sprint_ang_ru_10(callback):
    sprint_10.sprint_subject_10_ru(callback, bot, 'ang')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}geo 10')
def sprint_geo_ru_10(callback):
    sprint_10.sprint_subject_10_ru(callback, bot, 'geo')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}hm 10')
def sprint_hm_ru_10(callback):
    sprint_10.sprint_subject_10_ru(callback, bot, 'hm')
############################################################################################    SPRINT 10 RU
############################################################################################    SPRINT 10 RU // KZ
############################################################################################    SPRINT 10 KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_phys_10_kz')
def fiz_test(callback):
    start_test(callback, 350, 1782)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_10_kz')
def mat_test(callback):
    start_test(callback, 350, 1777)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_10_kz')
def kaz_test(callback):
    start_test(callback, 350, 1763)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_xim_10_kz')
def xim_test(callback):
    start_test(callback, 350, 1787)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_inf_10_kz')
def inf_test(callback):
    start_test(callback, 350, 1784)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hkz_10_kz')
def hkz_test(callback):
    start_test(callback, 350, 1770)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_bio_10_kz')
def bio_test(callback):
    start_test(callback, 350, 1867)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_10_kz')
def kazl_test(callback):
    start_test(callback, 350, 1858)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_ang_10_kz')
def ang_test(callback):
    start_test(callback, 350, 1843)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_geo_10_kz')
def geo_test(callback):
    start_test(callback, 350, 1865)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hm_10_kz')
def hm_test(callback):
    start_test(callback, 350, 1862)

############################################################################################    SPRINT 10
@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}fiz 10')
def sprint_phys_kz_10(callback):
    sprint_10.sprint_subject_10_kz(callback, bot, 'phys')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}mat 10')
def sprint_mat_kz_10(callback):
    sprint_10.sprint_subject_10_kz(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kaz 10')
def sprint_kaz_kz_10(callback):
    sprint_10.sprint_subject_10_kz(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}xim 10')
def sprint_xim_kz_10(callback):
    sprint_10.sprint_subject_10_kz(callback, bot, 'xim')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}informatika 10')
def sprint_inf_10(callback):
    sprint_10.sprint_subject_10_kz(callback, bot, 'inf')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}hkz 10')
def sprint_hkz_kz_10(callback):
    sprint_10.sprint_subject_10_kz(callback, bot, 'hkz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}bio 10')
def sprint_bio_kz_10(callback):
    sprint_10.sprint_subject_10_kz(callback, bot, 'bio')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kazl 10')
def sprint_kazl_kz_10(callback):
    sprint_10.sprint_subject_10_kz(callback, bot, 'kazl')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}ang 10')
def sprint_ang_kz_10(callback):
    sprint_10.sprint_subject_10_kz(callback, bot, 'ang')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}geo 10')
def sprint_geo_kz_10(callback):
    sprint_10.sprint_subject_10_kz(callback, bot, 'geo')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}hm 10')
def sprint_hm_kz_10(callback):
    sprint_10.sprint_subject_10_kz(callback, bot, 'hm')
############################################################################################    SPRINT 10 kz
############################################################################################    SPRINT 10 kz
############################################################################################    SPRINT 10 kz

############################################################################################    SPRINT 9 RU
############################################################################################    SPRINT 9 RU
############################################################################################    SPRINT 9 RU
@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_phys_9_ru')
def fiz_test(callback):
    start_test(callback, 350, 1781)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_9_ru')
def mat_test(callback):
    start_test(callback, 350, 1776)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_9_ru')
def kaz_test(callback):
    start_test(callback, 350, 1762)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_xim_9_ru')
def xim_test(callback):
    start_test(callback, 350, 1786)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_inf_9_ru')
def inf_test(callback):
    start_test(callback, 350, 1784)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hkz_9_ru')
def hkz_test(callback):
    start_test(callback, 350, 1769)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_bio_9_ru')
def bio_test(callback):
    start_test(callback, 350, 1846)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_9_ru')
def kazl_test(callback):
    start_test(callback, 350, 503)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_ang_9_ru')
def ang_test(callback):
    start_test(callback, 350, 1824)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_geo_9_ru')
def geo_test(callback):
    start_test(callback, 350, 1826)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hm_9_ru')
def hm_test(callback):
    start_test(callback, 350, 1861)

############################################################################################    SPRINT 9
@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}fiz 9')
def sprint_phys_ru_9(callback):
    sprint_9.sprint_subject_9_ru(callback, bot, 'phys')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}mat 9')
def sprint_mat_ru_9(callback):
    sprint_9.sprint_subject_9_ru(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kaz 9')
def sprint_kaz_ru_9(callback):
    sprint_9.sprint_subject_9_ru(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}xim 9')
def sprint_xim_ru_9(callback):
    sprint_9.sprint_subject_9_ru(callback, bot, 'xim')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}informatika 9')
def sprint_inf_9(callback):
    sprint_9.sprint_subject_9_ru(callback, bot, 'inf')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}hkz 9')
def sprint_hkz_ru_9(callback):
    sprint_9.sprint_subject_9_ru(callback, bot, 'hkz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}bio 9')
def sprint_bio_ru_9(callback):
    sprint_9.sprint_subject_9_ru(callback, bot, 'bio')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kazl 9')
def sprint_kazl_ru_9(callback):
    sprint_9.sprint_subject_9_ru(callback, bot, 'kazl')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}ang 9')
def sprint_ang_ru_9(callback):
    sprint_9.sprint_subject_9_ru(callback, bot, 'ang')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}geo 9')
def sprint_geo_ru_9(callback):
    sprint_9.sprint_subject_9_ru(callback, bot, 'geo')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}hm 9')
def sprint_hm_ru_9(callback):
    sprint_9.sprint_subject_9_ru(callback, bot, 'hm')
############################################################################################    SPRINT 9 RU
############################################################################################    SPRINT 9 RU // KZ
############################################################################################    SPRINT 9 KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_phys_9_kz')
def fiz_test(callback):
    start_test(callback, 350, 1781)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_9_kz')
def mat_test(callback):
    start_test(callback, 350, 1776)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_9_kz')
def kaz_test(callback):
    start_test(callback, 350, 1762)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_xim_9_kz')
def xim_test(callback):
    start_test(callback, 350, 1786)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_inf_9_kz')
def inf_test(callback):
    start_test(callback, 350, 1784)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hkz_9_kz')
def hkz_test(callback):
    start_test(callback, 350, 1769)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_bio_9_kz')
def bio_test(callback):
    start_test(callback, 350, 1846)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_9_kz')
def kazl_test(callback):
    start_test(callback, 350, 503)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_ang_9_kz')
def ang_test(callback):
    start_test(callback, 350, 1824)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_geo_9_kz')
def geo_test(callback):
    start_test(callback, 350, 1826)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hm_9_kz')
def hm_test(callback):
    start_test(callback, 350, 1861)

############################################################################################    SPRINT 9
@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}fiz 9')
def sprint_phys_kz_9(callback):
    sprint_9.sprint_subject_9_kz(callback, bot, 'phys')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}mat 9')
def sprint_mat_kz_9(callback):
    sprint_9.sprint_subject_9_kz(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kaz 9')
def sprint_kaz_kz_9(callback):
    sprint_9.sprint_subject_9_kz(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}xim 9')
def sprint_xim_kz_9(callback):
    sprint_9.sprint_subject_9_kz(callback, bot, 'xim')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}informatika 9')
def sprint_inf_9(callback):
    sprint_9.sprint_subject_9_kz(callback, bot, 'inf')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}hkz 9')
def sprint_hkz_kz_9(callback):
    sprint_9.sprint_subject_9_kz(callback, bot, 'hkz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}bio 9')
def sprint_bio_kz_9(callback):
    sprint_9.sprint_subject_9_kz(callback, bot, 'bio')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kazl 9')
def sprint_kazl_kz_9(callback):
    sprint_9.sprint_subject_9_kz(callback, bot, 'kazl')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}ang 9')
def sprint_ang_kz_9(callback):
    sprint_9.sprint_subject_9_kz(callback, bot, 'ang')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}geo 9')
def sprint_geo_kz_9(callback):
    sprint_9.sprint_subject_9_kz(callback, bot, 'geo')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}hm 9')
def sprint_hm_kz_9(callback):
    sprint_9.sprint_subject_9_kz(callback, bot, 'hm')
############################################################################################    SPRINT 9 kz
############################################################################################    SPRINT 9 kz
############################################################################################    SPRINT 9 kz


############################################################################################    SPRINT 8 RU
############################################################################################    SPRINT 8 RU
############################################################################################    SPRINT 8 RU
@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_phys_8_ru')
def fiz_test(callback):
    start_test(callback, 350, 1780)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_8_ru')
def mat_test(callback):
    start_test(callback, 350, 1775)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_8_ru')
def kaz_test(callback):
    start_test(callback, 350, 1761)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_xim_8_ru')
def xim_test(callback):
    start_test(callback, 350, 1785)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_inf_8_ru')
def inf_test(callback):
    start_test(callback, 350, 1784)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hkz_8_ru')
def hkz_test(callback):
    start_test(callback, 350, 1768)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_bio_8_ru')
def bio_test(callback):
    start_test(callback, 350, 1839)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_8_ru')
def kazl_test(callback):
    start_test(callback, 350, 1854)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_ang_8_ru')
def ang_test(callback):
    start_test(callback, 350, 1823)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_geo_8_ru')
def geo_test(callback):
    start_test(callback, 350, 1844)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hm_8_ru')
def hm_test(callback):
    start_test(callback, 350, 1860)

############################################################################################    SPRINT 8
@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}fiz 8')
def sprint_phys_ru_8(callback):
    sprint_8.sprint_subject_8_ru(callback, bot, 'phys')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}mat 8')
def sprint_mat_ru_8(callback):
    sprint_8.sprint_subject_8_ru(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kaz 8')
def sprint_kaz_ru_8(callback):
    sprint_8.sprint_subject_8_ru(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}xim 8')
def sprint_xim_ru_8(callback):
    sprint_8.sprint_subject_8_ru(callback, bot, 'xim')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}informatika 8')
def sprint_inf_8(callback):
    sprint_8.sprint_subject_8_ru(callback, bot, 'inf')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}hkz 8')
def sprint_hkz_ru_8(callback):
    sprint_8.sprint_subject_8_ru(callback, bot, 'hkz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}bio 8')
def sprint_bio_ru_8(callback):
    sprint_8.sprint_subject_8_ru(callback, bot, 'bio')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kazl 8')
def sprint_kazl_ru_8(callback):
    sprint_8.sprint_subject_8_ru(callback, bot, 'kazl')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}ang 8')
def sprint_ang_ru_8(callback):
    sprint_8.sprint_subject_8_ru(callback, bot, 'ang')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}geo 8')
def sprint_geo_ru_8(callback):
    sprint_8.sprint_subject_8_ru(callback, bot, 'geo')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}hm 8')
def sprint_hm_ru_8(callback):
    sprint_8.sprint_subject_8_ru(callback, bot, 'hm')
############################################################################################    SPRINT 8 RU
############################################################################################    SPRINT 8 RU // KZ
############################################################################################    SPRINT 8 KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_phys_8_kz')
def fiz_test(callback):
    start_test(callback, 350, 1780)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_8_kz')
def mat_test(callback):
    start_test(callback, 350, 1775)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_8_kz')
def kaz_test(callback):
    start_test(callback, 350, 1761)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_xim_8_kz')
def xim_test(callback):
    start_test(callback, 350, 1785)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_inf_8_kz')
def inf_test(callback):
    start_test(callback, 350, 1784)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hkz_8_kz')
def hkz_test(callback):
    start_test(callback, 350, 1768)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_bio_8_kz')
def bio_test(callback):
    start_test(callback, 350, 1839)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_8_kz')
def kazl_test(callback):
    start_test(callback, 350, 1854)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_ang_8_kz')
def ang_test(callback):
    start_test(callback, 350, 1823)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_geo_8_kz')
def geo_test(callback):
    start_test(callback, 350, 1844)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hm_8_kz')
def hm_test(callback):
    start_test(callback, 350, 1860)

############################################################################################    SPRINT 8
@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}fiz 8')
def sprint_phys_kz_8(callback):
    sprint_8.sprint_subject_8_kz(callback, bot, 'phys')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}mat 8')
def sprint_mat_kz_8(callback):
    sprint_8.sprint_subject_8_kz(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kaz 8')
def sprint_kaz_kz_8(callback):
    sprint_8.sprint_subject_8_kz(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}xim 8')
def sprint_xim_kz_8(callback):
    sprint_8.sprint_subject_8_kz(callback, bot, 'xim')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}informatika 8')
def sprint_inf_8(callback):
    sprint_8.sprint_subject_8_kz(callback, bot, 'inf')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}hkz 8')
def sprint_hkz_kz_8(callback):
    sprint_8.sprint_subject_8_kz(callback, bot, 'hkz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}bio 8')
def sprint_bio_kz_8(callback):
    sprint_8.sprint_subject_8_kz(callback, bot, 'bio')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kazl 8')
def sprint_kazl_kz_8(callback):
    sprint_8.sprint_subject_8_kz(callback, bot, 'kazl')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}ang 8')
def sprint_ang_kz_8(callback):
    sprint_8.sprint_subject_8_kz(callback, bot, 'ang')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}geo 8')
def sprint_geo_kz_8(callback):
    sprint_8.sprint_subject_8_kz(callback, bot, 'geo')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}hm 8')
def sprint_hm_kz_8(callback):
    sprint_8.sprint_subject_8_kz(callback, bot, 'hm')
############################################################################################    SPRINT 8 kz
############################################################################################    SPRINT 8 kz
############################################################################################    SPRINT 8 kz

############################################################################################    SPRINT 7 RU
############################################################################################    SPRINT 7 RU
############################################################################################    SPRINT 7 RU
@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_phys_7_ru')
def fiz_test(callback):
    start_test(callback, 350, 1779)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_7_ru')
def mat_test(callback):
    start_test(callback, 350, 1773)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_7_ru')
def kaz_test(callback):
    start_test(callback, 350, 1760)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_xim_7_ru')
def xim_test(callback):
    start_test(callback, 350, 503)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_inf_7_ru')
def inf_test(callback):
    start_test(callback, 350, 1784)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hkz_7_ru')
def hkz_test(callback):
    start_test(callback, 350, 1767)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_bio_7_ru')
def bio_test(callback):
    start_test(callback, 350, 1838)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_7_ru')
def kazl_test(callback):
    start_test(callback, 350, 1793)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_ang_7_ru')
def ang_test(callback):
    start_test(callback, 350, 1822)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_geo_7_ru')
def geo_test(callback):
    start_test(callback, 350, 1829)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hm_7_ru')
def hm_test(callback):
    start_test(callback, 350, 1859)

############################################################################################    SPRINT 7
@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}fiz 7')
def sprint_phys_ru_7(callback):
    sprint_7.sprint_subject_7_ru(callback, bot, 'phys')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}mat 7')
def sprint_mat_ru_7(callback):
    sprint_7.sprint_subject_7_ru(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kaz 7')
def sprint_kaz_ru_7(callback):
    sprint_7.sprint_subject_7_ru(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}xim 7')
def sprint_xim_ru_7(callback):
    sprint_7.sprint_subject_7_ru(callback, bot, 'xim')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}informatika 7')
def sprint_inf_7(callback):
    sprint_7.sprint_subject_7_ru(callback, bot, 'inf')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}hkz 7')
def sprint_hkz_ru_7(callback):
    sprint_7.sprint_subject_7_ru(callback, bot, 'hkz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}bio 7')
def sprint_bio_ru_7(callback):
    sprint_7.sprint_subject_7_ru(callback, bot, 'bio')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kazl 7')
def sprint_kazl_ru_7(callback):
    sprint_7.sprint_subject_7_ru(callback, bot, 'kazl')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}ang 7')
def sprint_ang_ru_7(callback):
    sprint_7.sprint_subject_7_ru(callback, bot, 'ang')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}geo 7')
def sprint_geo_ru_7(callback):
    sprint_7.sprint_subject_7_ru(callback, bot, 'geo')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}hm 7')
def sprint_hm_ru_7(callback):
    sprint_7.sprint_subject_7_ru(callback, bot, 'hm')
############################################################################################    SPRINT 7 RU
############################################################################################    SPRINT 7 RU // KZ
############################################################################################    SPRINT 7 KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_phys_7_kz')
def fiz_test(callback):
    start_test(callback, 350, 1779)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_7_kz')
def mat_test(callback):
    start_test(callback, 350, 1773)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_7_kz')
def kaz_test(callback):
    start_test(callback, 350, 1760)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_xim_7_kz')
def xim_test(callback):
    start_test(callback, 350, 503)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_inf_7_kz')
def inf_test(callback):
    start_test(callback, 350, 1784)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hkz_7_kz')
def hkz_test(callback):
    start_test(callback, 350, 1767)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_bio_7_kz')
def bio_test(callback):
    start_test(callback, 350, 1838)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_7_kz')
def kazl_test(callback):
    start_test(callback, 350, 1793)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_ang_7_kz')
def ang_test(callback):
    start_test(callback, 350, 1822)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_geo_7_kz')
def geo_test(callback):
    start_test(callback, 350, 1829)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hm_7_kz')
def hm_test(callback):
    start_test(callback, 350, 1859)

############################################################################################    SPRINT 7
@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}fiz 7')
def sprint_phys_kz_7(callback):
    sprint_7.sprint_subject_7_kz(callback, bot, 'phys')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}mat 7')
def sprint_mat_kz_7(callback):
    sprint_7.sprint_subject_7_kz(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kaz 7')
def sprint_kaz_kz_7(callback):
    sprint_7.sprint_subject_7_kz(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}xim 7')
def sprint_xim_kz_7(callback):
    sprint_7.sprint_subject_7_kz(callback, bot, 'xim')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}informatika 7')
def sprint_inf_7(callback):
    sprint_7.sprint_subject_7_kz(callback, bot, 'inf')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}hkz 7')
def sprint_hkz_kz_7(callback):
    sprint_7.sprint_subject_7_kz(callback, bot, 'hkz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}bio 7')
def sprint_bio_kz_7(callback):
    sprint_7.sprint_subject_7_kz(callback, bot, 'bio')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kazl 7')
def sprint_kazl_kz_7(callback):
    sprint_7.sprint_subject_7_kz(callback, bot, 'kazl')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}ang 7')
def sprint_ang_kz_7(callback):
    sprint_7.sprint_subject_7_kz(callback, bot, 'ang')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}geo 7')
def sprint_geo_kz_7(callback):
    sprint_7.sprint_subject_7_kz(callback, bot, 'geo')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}hm 7')
def sprint_hm_kz_7(callback):
    sprint_7.sprint_subject_7_kz(callback, bot, 'hm')
############################################################################################    SPRINT 7 kz
############################################################################################    SPRINT 7 kz
############################################################################################    SPRINT 7 kz

############################################################################################    SPRINT 6 RU
############################################################################################    SPRINT 6 RU
############################################################################################    SPRINT 6 RU
@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_est_6_ru')
def fiz_test(callback):
    start_test(callback, 350, 1827)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_6_ru')
def mat_test(callback):
    start_test(callback, 350, 1774)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_6_ru')
def kaz_test(callback):
    start_test(callback, 350, 1759)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_inf_6_ru')
def inf_test(callback):
    start_test(callback, 350, 1784)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hkz_6_ru')
def hkz_test(callback):
    start_test(callback, 350, 1766)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_bio_6_ru')
def bio_test(callback):
    start_test(callback, 350, 1866)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_6_ru')
def kazl_test(callback):
    start_test(callback, 350, 1848)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_ang_6_ru')
def ang_test(callback):
    start_test(callback, 350, 1800)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_geo_6_ru')
def geo_test(callback):
    start_test(callback, 350, 1845)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hm_6_ru')
def hm_test(callback):
    start_test(callback, 350, 1857)

############################################################################################    SPRINT 6
@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}est 6')
def sprint_est_ru_6(callback):
    sprint_6.sprint_subject_6_ru(callback, bot, 'est')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}mat 6')
def sprint_mat_ru_6(callback):
    sprint_6.sprint_subject_6_ru(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kaz 6')
def sprint_kaz_ru_6(callback):
    sprint_6.sprint_subject_6_ru(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}informatika 6')
def sprint_inf_6(callback):
    sprint_6.sprint_subject_6_ru(callback, bot, 'inf')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}hkz 6')
def sprint_hkz_ru_6(callback):
    sprint_6.sprint_subject_6_ru(callback, bot, 'hkz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}bio 6')
def sprint_bio_ru_6(callback):
    sprint_6.sprint_subject_6_ru(callback, bot, 'bio')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kazl 6')
def sprint_kazl_ru_6(callback):
    sprint_6.sprint_subject_6_ru(callback, bot, 'kazl')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}ang 6')
def sprint_ang_ru_6(callback):
    sprint_6.sprint_subject_6_ru(callback, bot, 'ang')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}geo 6')
def sprint_geo_ru_6(callback):
    sprint_6.sprint_subject_6_ru(callback, bot, 'geo')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}hm 6')
def sprint_hm_ru_6(callback):
    sprint_6.sprint_subject_6_ru(callback, bot, 'hm')
############################################################################################    SPRINT 6 RU
############################################################################################    SPRINT 6 RU // KZ
############################################################################################    SPRINT 6 KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_est_6_kz')
def est_test(callback):
    start_test(callback, 350, 1827)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_6_kz')
def mat_test(callback):
    start_test(callback, 350, 1774)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_6_kz')
def kaz_test(callback):
    start_test(callback, 350, 1759)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_inf_6_kz')
def inf_test(callback):
    start_test(callback, 350, 1784)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hkz_6_kz')
def hkz_test(callback):
    start_test(callback, 350, 1766)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_bio_6_kz')
def bio_test(callback):
    start_test(callback, 350, 1866)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_6_kz')
def kazl_test(callback):
    start_test(callback, 350, 1848)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_ang_6_kz')
def ang_test(callback):
    start_test(callback, 350, 1800)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_geo_6_kz')
def geo_test(callback):
    start_test(callback, 350, 1845)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hm_6_kz')
def hm_test(callback):
    start_test(callback, 350, 1857)

############################################################################################    SPRINT 6
@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}est 6')
def sprint_est_kz_6(callback):
    sprint_6.sprint_subject_6_kz(callback, bot, 'est')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}mat 6')
def sprint_mat_kz_6(callback):
    sprint_6.sprint_subject_6_kz(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kaz 6')
def sprint_kaz_kz_6(callback):
    sprint_6.sprint_subject_6_kz(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}informatika 6')
def sprint_inf_6(callback):
    sprint_6.sprint_subject_6_kz(callback, bot, 'inf')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}hkz 6')
def sprint_hkz_kz_6(callback):
    sprint_6.sprint_subject_6_kz(callback, bot, 'hkz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}bio 6')
def sprint_bio_kz_6(callback):
    sprint_6.sprint_subject_6_kz(callback, bot, 'bio')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kazl 6')
def sprint_kazl_kz_6(callback):
    sprint_6.sprint_subject_6_kz(callback, bot, 'kazl')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}ang 6')
def sprint_ang_kz_6(callback):
    sprint_6.sprint_subject_6_kz(callback, bot, 'ang')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}geo 6')
def sprint_geo_kz_6(callback):
    sprint_6.sprint_subject_6_kz(callback, bot, 'geo')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}hm 6')
def sprint_hm_kz_6(callback):
    sprint_6.sprint_subject_6_kz(callback, bot, 'hm')
############################################################################################    SPRINT 6 kz
############################################################################################    SPRINT 6 kz
############################################################################################    SPRINT 6 kz


############################################################################################    SPRINT 5 RU
############################################################################################    SPRINT 5 RU
############################################################################################    SPRINT 5 RU
@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_est_5_ru')
def fiz_test(callback):
    start_test(callback, 350, 1827)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_5_ru')
def mat_test(callback):
    start_test(callback, 350, 1772)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_5_ru')
def kaz_test(callback):
    start_test(callback, 350, 1758)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_inf_5_ru')
def inf_test(callback):
    start_test(callback, 350, 1784)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hkz_5_ru')
def hkz_test(callback):
    start_test(callback, 350, 1765)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_bio_5_ru')
def bio_test(callback):
    start_test(callback, 350, 503)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_5_ru')
def kazl_test(callback):
    start_test(callback, 350, 1847)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_ang_5_ru')
def ang_test(callback):
    start_test(callback, 350, 1825)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_geo_5_ru')
def geo_test(callback):
    start_test(callback, 350, 503)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hm_5_ru')
def hm_test(callback):
    start_test(callback, 350, 1856)

############################################################################################    SPRINT 5
@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}est 5')
def sprint_est_ru_5(callback):
    sprint_5.sprint_subject_5_ru(callback, bot, 'est')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}mat 5')
def sprint_mat_ru_5(callback):
    sprint_5.sprint_subject_5_ru(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kaz 5')
def sprint_kaz_ru_5(callback):
    sprint_5.sprint_subject_5_ru(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}informatika 5')
def sprint_inf_5(callback):
    sprint_5.sprint_subject_5_ru(callback, bot, 'inf')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}hkz 5')
def sprint_hkz_ru_5(callback):
    sprint_5.sprint_subject_5_ru(callback, bot, 'hkz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kazl 5')
def sprint_kazl_ru_5(callback):
    sprint_5.sprint_subject_5_ru(callback, bot, 'kazl')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}ang 5')
def sprint_ang_ru_5(callback):
    sprint_5.sprint_subject_5_ru(callback, bot, 'ang')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}geo 5')
def sprint_geo_ru_5(callback):
    sprint_5.sprint_subject_5_ru(callback, bot, 'geo')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}hm 5')
def sprint_hm_ru_5(callback):
    sprint_5.sprint_subject_5_ru(callback, bot, 'hm')
############################################################################################    SPRINT 5 RU
############################################################################################    SPRINT 5 RU // KZ
############################################################################################    SPRINT 5 KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_est_5_kz')
def est_test(callback):
    start_test(callback, 350, 503)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_5_kz')
def mat_test(callback):
    start_test(callback, 350, 1772)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_5_kz')
def kaz_test(callback):
    start_test(callback, 350, 1758)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_inf_5_kz')
def inf_test(callback):
    start_test(callback, 350, 1784)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hkz_5_kz')
def hkz_test(callback):
    start_test(callback, 350, 1765)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_5_kz')
def kazl_test(callback):
    start_test(callback, 350, 1847)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_ang_5_kz')
def ang_test(callback):
    start_test(callback, 350, 1825)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_geo_5_kz')
def geo_test(callback):
    start_test(callback, 350, 503)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_hm_5_kz')
def hm_test(callback):
    start_test(callback, 350, 1856)

############################################################################################    SPRINT 5
@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}est 5')
def sprint_est_kz_5(callback):
    sprint_5.sprint_subject_5_kz(callback, bot, 'est')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}mat 5')
def sprint_mat_kz_5(callback):
    sprint_5.sprint_subject_5_kz(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kaz 5')
def sprint_kaz_kz_5(callback):
    sprint_5.sprint_subject_5_kz(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}informatika 5')
def sprint_inf_5(callback):
    sprint_5.sprint_subject_5_kz(callback, bot, 'inf')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}hkz 5')
def sprint_hkz_kz_5(callback):
    sprint_5.sprint_subject_5_kz(callback, bot, 'hkz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kazl 5')
def sprint_kazl_kz_5(callback):
    sprint_5.sprint_subject_5_kz(callback, bot, 'kazl')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}ang 5')
def sprint_ang_kz_5(callback):
    sprint_5.sprint_subject_5_kz(callback, bot, 'ang')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}geo 5')
def sprint_geo_kz_5(callback):
    sprint_5.sprint_subject_5_kz(callback, bot, 'geo')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}hm 5')
def sprint_hm_kz_5(callback):
    sprint_5.sprint_subject_5_kz(callback, bot, 'hm')
############################################################################################    SPRINT 5 kz
############################################################################################    SPRINT 5 kz
############################################################################################    SPRINT 5 kz


############################################################################################    SPRINT 4
############################################################################################    SPRINT 4
############################################################################################    SPRINT 4
@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_4_ru')
def mat_test(callback):
    start_test(callback, 350, 1799)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_4_ru')
def kaz_test(callback):
    start_test(callback, 350, 1792)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_4_ru')
def kazl_test(callback):
    start_test(callback, 350, 1796)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}mat 4')
def sprint_mat_ru_4(callback):
    sprint_4.sprint_subject_4_ru(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kaz 4')
def sprint_kaz_ru_4(callback):
    sprint_4.sprint_subject_4_ru(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kazl 4')
def sprint_kazl_ru_4(callback):
    sprint_4.sprint_subject_4_ru(callback, bot, 'kazl')


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_4_kz')
def mat_test(callback):
    start_test(callback, 350, 1799)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_4_kz')
def kaz_test(callback):
    start_test(callback, 350, 1792)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_4_kz')
def kazl_test(callback):
    start_test(callback, 350, 1796)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}mat 4')
def sprint_mat_kz_4(callback):
    sprint_4.sprint_subject_4_kz(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kaz 4')
def sprint_kaz_kz_4(callback):
    sprint_4.sprint_subject_4_kz(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kazl 4')
def sprint_kazl_kz_4(callback):
    sprint_4.sprint_subject_4_kz(callback, bot, 'kazl')
############################################################################################    SPRINT 4
############################################################################################    SPRINT 4
############################################################################################    SPRINT 4


############################################################################################    SPRINT 3
############################################################################################    SPRINT 3
############################################################################################    SPRINT 3
@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_3_ru')
def mat_test(callback):
    start_test(callback, 350, 1798)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_3_ru')
def kaz_test(callback):
    start_test(callback, 350, 1791)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_3_ru')
def kazl_test(callback):
    start_test(callback, 350, 1794)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}mat 3')
def sprint_mat_ru_3(callback):
    sprint_3.sprint_subject_3_ru(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kaz 3')
def sprint_kaz_ru_3(callback):
    sprint_3.sprint_subject_3_ru(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kazl 3')
def sprint_kazl_ru_3(callback):
    sprint_3.sprint_subject_3_ru(callback, bot, 'kazl')


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_3_kz')
def mat_test(callback):
    start_test(callback, 350, 1798)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_3_kz')
def kaz_test(callback):
    start_test(callback, 350, 1791)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_3_kz')
def kazl_test(callback):
    start_test(callback, 350, 1794)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}mat 3')
def sprint_mat_kz_3(callback):
    sprint_3.sprint_subject_3_kz(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kaz 3')
def sprint_kaz_kz_3(callback):
    sprint_3.sprint_subject_3_kz(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kazl 3')
def sprint_kazl_kz_3(callback):
    sprint_3.sprint_subject_3_kz(callback, bot, 'kazl')
############################################################################################    SPRINT 3
############################################################################################    SPRINT 3
############################################################################################    SPRINT 3


############################################################################################    SPRINT 2
############################################################################################    SPRINT 2
############################################################################################    SPRINT 2
@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_2_ru')
def mat_test(callback):
    start_test(callback, 350, 1797)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_2_ru')
def kaz_test(callback):
    start_test(callback, 350, 1790)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_2_ru')
def kazl_test(callback):
    start_test(callback, 350, 1795)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}mat 2')
def sprint_mat_ru_2(callback):
    sprint_2.sprint_subject_2_ru(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kaz 2')
def sprint_kaz_ru_2(callback):
    sprint_2.sprint_subject_2_ru(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kazl 2')
def sprint_kazl_ru_2(callback):
    sprint_2.sprint_subject_2_ru(callback, bot, 'kazl')


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_2_kz')
def mat_test(callback):
    start_test(callback, 350, 1797)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_2_kz')
def kaz_test(callback):
    start_test(callback, 350, 1790)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kazl_2_kz')
def kazl_test(callback):
    start_test(callback, 350, 1795)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}mat 2')
def sprint_mat_kz_2(callback):
    sprint_2.sprint_subject_2_kz(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kaz 2')
def sprint_kaz_kz_2(callback):
    sprint_2.sprint_subject_2_kz(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kazl 2')
def sprint_kazl_kz_2(callback):
    sprint_2.sprint_subject_2_kz(callback, bot, 'kazl')
############################################################################################    SPRINT 2
############################################################################################    SPRINT 2
############################################################################################    SPRINT 2


############################################################################################    SPRINT 1
############################################################################################    SPRINT 1
############################################################################################    SPRINT 1
@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_1_ru')
def mat_test(callback):
    start_test(callback, 350, 1797)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_1_ru')
def kaz_test(callback):
    start_test(callback, 350, 1790)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}mat 1')
def sprint_mat_ru_1(callback):
    sprint_1.sprint_subject_1_ru(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru}kaz 1')
def sprint_kaz_ru_1(callback):
    sprint_1.sprint_subject_1_ru(callback, bot, 'kaz')


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_mat_1_kz')
def mat_test(callback):
    start_test(callback, 350, 1797)


@bot.callback_query_handler(func=lambda callback: callback.data == f'spr_kaz_1_kz')
def kaz_test(callback):
    start_test(callback, 350, 1790)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}mat 1')
def sprint_mat_kz_1(callback):
    sprint_1.sprint_subject_1_kz(callback, bot, 'mat')


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz}kaz 1')
def sprint_kaz_kz_1(callback):
    sprint_1.sprint_subject_1_kz(callback, bot, 'kaz')
############################################################################################    SPRINT 1
############################################################################################    SPRINT 1
############################################################################################    SPRINT 1

############################################################################################    DODA
############################################################################################    DODA
############################################################################################    DODA
@bot.callback_query_handler(func=lambda callback: callback.data == f'ling_1_ru')
def ling_1_ru(callback):
    doda_olymp.doda_subject_ru(callback, bot, '1', f'{doda_dir_lan_ru}')


@bot.callback_query_handler(func=lambda callback: callback.data == f'log_1_ru')
def log_1_ru(callback):
    doda_olymp.doda_subject_ru(callback, bot, '1', f'{doda_dir_log_ru}')


@bot.callback_query_handler(func=lambda callback: callback.data == f'ling_1_kz')
def ling_1_ru(callback):
    doda_olymp.doda_subject_kz(callback, bot, '1', f'{doda_dir_lan_kz}')


@bot.callback_query_handler(func=lambda callback: callback.data == f'log_1_kz')
def log_1_ru(callback):
    doda_olymp.doda_subject_kz(callback, bot, '1', f'{doda_dir_log_kz}')


@bot.callback_query_handler(func=lambda callback: callback.data == f'ling_2_ru')
def ling_2_ru(callback):
    doda_olymp.doda_subject_ru(callback, bot, '2', f'{doda_dir_lan_ru}')


@bot.callback_query_handler(func=lambda callback: callback.data == f'log_2_ru')
def log_2_ru(callback):
    doda_olymp.doda_subject_ru(callback, bot, '2', f'{doda_dir_log_ru}')


@bot.callback_query_handler(func=lambda callback: callback.data == f'ling_2_kz')
def ling_2_ru(callback):
    doda_olymp.doda_subject_kz(callback, bot, '2', f'{doda_dir_lan_kz}')


@bot.callback_query_handler(func=lambda callback: callback.data == f'log_2_kz')
def log_2_ru(callback):
    doda_olymp.doda_subject_kz(callback, bot, '2', f'{doda_dir_log_kz}')


@bot.callback_query_handler(func=lambda callback: callback.data == f'ling_3_ru')
def ling_3_ru(callback):
    doda_olymp.doda_subject_ru(callback, bot, '3', f'{doda_dir_lan_ru}')


@bot.callback_query_handler(func=lambda callback: callback.data == f'log_3_ru')
def log_3_ru(callback):
    doda_olymp.doda_subject_ru(callback, bot, '3', f'{doda_dir_log_ru}')


@bot.callback_query_handler(func=lambda callback: callback.data == f'ling_3_kz')
def ling_3_ru(callback):
    doda_olymp.doda_subject_kz(callback, bot, '3', f'{doda_dir_lan_kz}')


@bot.callback_query_handler(func=lambda callback: callback.data == f'log_3_kz')
def log_3_ru(callback):
    doda_olymp.doda_subject_kz(callback, bot, '3', f'{doda_dir_log_kz}')


@bot.callback_query_handler(func=lambda callback: callback.data == f'ling_4_ru')
def ling_4_ru(callback):
    doda_olymp.doda_subject_ru(callback, bot, '4', f'{doda_dir_lan_ru}')


@bot.callback_query_handler(func=lambda callback: callback.data == f'log_4_ru')
def log_4_ru(callback):
    doda_olymp.doda_subject_ru(callback, bot, '4', f'{doda_dir_log_ru}')


@bot.callback_query_handler(func=lambda callback: callback.data == f'ling_4_kz')
def ling_4_ru(callback):
    doda_olymp.doda_subject_kz(callback, bot, '4', f'{doda_dir_lan_kz}')


@bot.callback_query_handler(func=lambda callback: callback.data == f'log_4_kz')
def log_4_ru(callback):
    doda_olymp.doda_subject_kz(callback, bot, '4', f'{doda_dir_log_kz}')


############################################################################################    DODA
############################################################################################    DODA
############################################################################################    DODA

############################################################################################    DODA
############################################################################################    DODA
############################################################################################    DODA
@bot.callback_query_handler(func=lambda callback: callback.data == f'doda_{doda_dir_lan_ru}_1_ru')
def ling_1_ru(callback):
    start_test(callback, 1500, 1834)


@bot.callback_query_handler(func=lambda callback: callback.data == f'doda_{doda_dir_log_ru}_1_ru')
def log_1_ru(callback):
    start_test(callback, 1500, 1830)


@bot.callback_query_handler(func=lambda callback: callback.data == f'doda_{doda_dir_lan_kz}_1_kz')
def ling_1_ru(callback):
    start_test(callback, 1500, 1834)


@bot.callback_query_handler(func=lambda callback: callback.data == f'doda_{doda_dir_log_kz}_1_kz')
def log_1_ru(callback):
    start_test(callback, 1500, 1830)


@bot.callback_query_handler(func=lambda callback: callback.data == f'doda_{doda_dir_lan_ru}_2_ru')
def ling_2_ru(callback):
    start_test(callback, 1500, 1835)


@bot.callback_query_handler(func=lambda callback: callback.data == f'doda_{doda_dir_log_ru}_2_ru')
def log_2_ru(callback):
    start_test(callback, 1500, 1831)


@bot.callback_query_handler(func=lambda callback: callback.data == f'doda_{doda_dir_lan_kz}_2_kz')
def ling_2_ru(callback):
    start_test(callback, 1500, 1835)


@bot.callback_query_handler(func=lambda callback: callback.data == f'doda_{doda_dir_log_kz}_2_kz')
def log_2_ru(callback):
    start_test(callback, 1500, 1831)


@bot.callback_query_handler(func=lambda callback: callback.data == f'doda_{doda_dir_lan_ru}_3_ru')
def ling_3_ru(callback):
    start_test(callback, 1500, 1836)


@bot.callback_query_handler(func=lambda callback: callback.data == f'doda_{doda_dir_log_ru}_3_ru')
def log_3_ru(callback):
    start_test(callback, 1500, 1832)


@bot.callback_query_handler(func=lambda callback: callback.data == f'doda_{doda_dir_lan_kz}_3_kz')
def ling_3_ru(callback):
    start_test(callback, 1500, 1836)


@bot.callback_query_handler(func=lambda callback: callback.data == f'doda_{doda_dir_log_kz}_3_kz')
def log_3_ru(callback):
    start_test(callback, 1500, 1832)


@bot.callback_query_handler(func=lambda callback: callback.data == f'doda_{doda_dir_lan_ru}_4_ru')
def ling_4_ru(callback):
    start_test(callback, 1500, 1837)


@bot.callback_query_handler(func=lambda callback: callback.data == f'doda_{doda_dir_log_ru}_4_ru')
def log_4_ru(callback):
    start_test(callback, 1500, 1833)


@bot.callback_query_handler(func=lambda callback: callback.data == f'doda_{doda_dir_lan_kz}_4_kz')
def ling_4_ru(callback):
    start_test(callback, 1500, 1837)


@bot.callback_query_handler(func=lambda callback: callback.data == f'doda_{doda_dir_log_kz}_4_kz')
def log_4_ru(callback):
    start_test(callback, 1500, 1833)


############################################################################################    DODA
############################################################################################    DODA
############################################################################################    DODA

############################################  11 class  SUBJECTS ###########################################
############################################  11 class  SUBJECTS ###########################################
############################################  11 class  SUBJECTS ###########################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Информатика {sprint_ru}11')
def informatika(callback):
    subjects_11.informatika(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_ru} 11')
def matematika(callback):
    subjects_11.matematika(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_ru} 11')
def kaz_yaz(callback):
    subjects_11.kaz_yaz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_ru} 11')
def kaz_lit(callback):
    subjects_11.kaz_lit(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Био {sprint_ru} 11')
def bio(callback):
    subjects_11.bio(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Хим {sprint_ru} 11')
def xim(callback):
    subjects_11.xim(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Физ {sprint_ru} 11')
def fiz(callback):
    subjects_11.fiz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Иск {sprint_ru} 11')
def hkz(callback):
    subjects_11.hkz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мира {sprint_ru} 11')
def hm(callback):
    subjects_11.hm(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Гео {sprint_ru} 11')
def geo(callback):
    subjects_11.geo(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Анг {sprint_ru} 11')
def ang(callback):
    subjects_11.ang(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{matem} 11')
def mat_bil(callback):
    subjects_11.mat_bil(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum} 11')
def gum_bil(callback):
    subjects_11.gum_bil(callback, bot)

######################################################################################################     KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'Информатика {sprint_kz}11')
def informatika(callback):
    subjects_11.informatika_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_kz} 11')
def matematika(callback):
    subjects_11.matematika_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_kz} 11')
def kaz_yaz(callback):
    subjects_11.kaz_yaz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_kz} 11')
def kaz_lit(callback):
    subjects_11.kaz_lit_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Био {sprint_kz} 11')
def bio(callback):
    subjects_11.bio_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Хим {sprint_kz} 11')
def xim(callback):
    subjects_11.xim_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Физ {sprint_kz} 11')
def fiz(callback):
    subjects_11.fiz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Иск {sprint_kz} 11')
def hkz(callback):
    subjects_11.hkz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мира {sprint_kz} 11')
def hm(callback):
    subjects_11.hm_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Гео {sprint_kz} 11')
def geo(callback):
    subjects_11.geo_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Анг {sprint_kz} 11')
def ang(callback):
    subjects_11.ang_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{mat_kz} 11')
def mat_bil(callback):
    subjects_11.mat_bil_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum_kz} 11')
def gum_bil(callback):
    subjects_11.gum_bil_kz(callback, bot)
############################################  11 class  SUBJECTS ###########################################
############################################  11 class  SUBJECTS ###########################################
############################################  11 class  SUBJECTS ###########################################

############################################  10 class  SUBJECTS ###########################################
############################################  10 class  SUBJECTS ###########################################
############################################  10 class  SUBJECTS ###########################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Информатика {sprint_ru}10')
def informatika(callback):
    subjects_10.informatika(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_ru} 10')
def matematika(callback):
    subjects_10.matematika(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_ru} 10')
def kaz_yaz(callback):
    subjects_10.kaz_yaz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_ru} 10')
def kaz_lit(callback):
    subjects_10.kaz_lit(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Био {sprint_ru} 10')
def bio(callback):
    subjects_10.bio(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Хим {sprint_ru} 10')
def xim(callback):
    subjects_10.xim(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Физ {sprint_ru} 10')
def fiz(callback):
    subjects_10.fiz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Иск {sprint_ru} 10')
def hkz(callback):
    subjects_10.hkz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мира {sprint_ru} 10')
def hm(callback):
    subjects_10.hm(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Гео {sprint_ru} 10')
def geo(callback):
    subjects_10.geo(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Анг {sprint_ru} 10')
def ang(callback):
    subjects_10.ang(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{matem} 10')
def mat_bil(callback):
    subjects_10.mat_bil(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum} 10')
def gum_bil(callback):
    subjects_10.gum_bil(callback, bot)
######################################################################################################     KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'Информатика {sprint_kz}10')
def informatika(callback):
    subjects_10.informatika_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_kz} 10')
def matematika(callback):
    subjects_10.matematika_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_kz} 10')
def kaz_yaz(callback):
    subjects_10.kaz_yaz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_kz} 10')
def kaz_lit(callback):
    subjects_10.kaz_lit_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Био {sprint_kz} 10')
def bio(callback):
    subjects_10.bio_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Хим {sprint_kz} 10')
def xim(callback):
    subjects_10.xim_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Физ {sprint_kz} 10')
def fiz(callback):
    subjects_10.fiz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Иск {sprint_kz} 10')
def hkz(callback):
    subjects_10.hkz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мира {sprint_kz} 10')
def hm(callback):
    subjects_10.hm_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Гео {sprint_kz} 10')
def geo(callback):
    subjects_10.geo_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Анг {sprint_kz} 10')
def ang(callback):
    subjects_10.ang_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{mat_kz} 10')
def mat_bil(callback):
    subjects_10.mat_bil_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum_kz} 10')
def gum_bil(callback):
    subjects_10.gum_bil_kz(callback, bot)
############################################  10 class  SUBJECTS ###########################################
############################################  10 class  SUBJECTS ###########################################
############################################  10 class  SUBJECTS ###########################################


############################################  9 class  SUBJECTS ###########################################
############################################  9 class  SUBJECTS ###########################################
############################################  9 class  SUBJECTS ###########################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Информатика {sprint_ru}9')
def informatika(callback):
    subjects_9.informatika(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_ru} 9')
def matematika(callback):
    subjects_9.matematika(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_ru} 9')
def kaz_yaz(callback):
    subjects_9.kaz_yaz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_ru} 9')
def kaz_lit(callback):
    subjects_9.kaz_lit(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Био {sprint_ru} 9')
def bio(callback):
    subjects_9.bio(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Хим {sprint_ru} 9')
def xim(callback):
    subjects_9.xim(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Физ {sprint_ru} 9')
def fiz(callback):
    subjects_9.fiz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Иск {sprint_ru} 9')
def hkz(callback):
    subjects_9.hkz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мира {sprint_ru} 9')
def hm(callback):
    subjects_9.hm(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Гео {sprint_ru} 9')
def geo(callback):
    subjects_9.geo(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Анг {sprint_ru} 9')
def ang(callback):
    subjects_9.ang(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{matem} 9')
def mat_bil(callback):
    subjects_9.mat_bil(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum} 9')
def gum_bil(callback):
    subjects_9.gum_bil(callback, bot)

######################################################################################################     KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'Информатика {sprint_kz}9')
def informatika(callback):
    subjects_9.informatika_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_kz} 9')
def matematika(callback):
    subjects_9.matematika_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_kz} 9')
def kaz_yaz(callback):
    subjects_9.kaz_yaz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_kz} 9')
def kaz_lit(callback):
    subjects_9.kaz_lit_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Био {sprint_kz} 9')
def bio(callback):
    subjects_9.bio_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Хим {sprint_kz} 9')
def xim(callback):
    subjects_9.xim_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Физ {sprint_kz} 9')
def fiz(callback):
    subjects_9.fiz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Иск {sprint_kz} 9')
def hkz(callback):
    subjects_9.hkz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мира {sprint_kz} 9')
def hm(callback):
    subjects_9.hm_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Гео {sprint_kz} 9')
def geo(callback):
    subjects_9.geo_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Анг {sprint_kz} 9')
def ang(callback):
    subjects_9.ang_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{mat_kz} 9')
def mat_bil(callback):
    subjects_9.mat_bil_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum_kz} 9')
def gum_bil(callback):
    subjects_9.gum_bil_kz(callback, bot)
############################################  9 class  SUBJECTS ###########################################
############################################  9 class  SUBJECTS ###########################################
############################################  9 class  SUBJECTS ###########################################


############################################  8 class  SUBJECTS ###########################################
############################################  8 class  SUBJECTS ###########################################
############################################  8 class  SUBJECTS ###########################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Информатика {sprint_ru}8')
def informatika(callback):
    subjects_8.informatika(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_ru} 8')
def matematika(callback):
    subjects_8.matematika(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_ru} 8')
def kaz_yaz(callback):
    subjects_8.kaz_yaz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_ru} 8')
def kaz_lit(callback):
    subjects_8.kaz_lit(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Био {sprint_ru} 8')
def bio(callback):
    subjects_8.bio(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Хим {sprint_ru} 8')
def xim(callback):
    subjects_8.xim(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Физ {sprint_ru} 8')
def fiz(callback):
    subjects_8.fiz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Иск {sprint_ru} 8')
def hkz(callback):
    subjects_8.hkz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мира {sprint_ru} 8')
def hm(callback):
    subjects_8.hm(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Гео {sprint_ru} 8')
def geo(callback):
    subjects_8.geo(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Анг {sprint_ru} 8')
def ang(callback):
    subjects_8.ang(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{matem} 8')
def mat_bil(callback):
    subjects_8.mat_bil(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum} 8')
def gum_bil(callback):
    subjects_8.gum_bil(callback, bot)
######################################################################################################     KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'Информатика {sprint_kz}8')
def informatika(callback):
    subjects_8.informatika_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_kz} 8')
def matematika(callback):
    subjects_8.matematika_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_kz} 8')
def kaz_yaz(callback):
    subjects_8.kaz_yaz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_kz} 8')
def kaz_lit(callback):
    subjects_8.kaz_lit_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Био {sprint_kz} 8')
def bio(callback):
    subjects_8.bio_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Хим {sprint_kz} 8')
def xim(callback):
    subjects_8.xim_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Физ {sprint_kz} 8')
def fiz(callback):
    subjects_8.fiz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Иск {sprint_kz} 8')
def hkz(callback):
    subjects_8.hkz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мира {sprint_kz} 8')
def hm(callback):
    subjects_8.hm_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Гео {sprint_kz} 8')
def geo(callback):
    subjects_8.geo_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Анг {sprint_kz} 8')
def ang(callback):
    subjects_8.ang_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{mat_kz} 8')
def mat_bil(callback):
    subjects_8.mat_bil_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum_kz} 8')
def gum_bil(callback):
    subjects_8.gum_bil_kz(callback, bot)
############################################  8 class  SUBJECTS ###########################################
############################################  8 class  SUBJECTS ###########################################
############################################  8 class  SUBJECTS ###########################################


############################################  7 class  SUBJECTS ###########################################
############################################  7 class  SUBJECTS ###########################################
############################################  7 class  SUBJECTS ###########################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Информатика {sprint_ru}7')
def informatika(callback):
    subjects_7.informatika(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_ru} 7')
def matematika(callback):
    subjects_7.matematika(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_ru} 7')
def kaz_yaz(callback):
    subjects_7.kaz_yaz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_ru} 7')
def kaz_lit(callback):
    subjects_7.kaz_lit(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Био {sprint_ru} 7')
def bio(callback):
    subjects_7.bio(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Хим {sprint_ru} 7')
def xim(callback):
    subjects_7.xim(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Физ {sprint_ru} 7')
def fiz(callback):
    subjects_7.fiz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Иск {sprint_ru} 7')
def hkz(callback):
    subjects_7.hkz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мира {sprint_ru} 7')
def hm(callback):
    subjects_7.hm(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Гео {sprint_ru} 7')
def geo(callback):
    subjects_7.geo(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Анг {sprint_ru} 7')
def ang(callback):
    subjects_7.ang(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{matem} 7')
def mat_bil(callback):
    subjects_7.mat_bil(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum} 7')
def gum_bil(callback):
    subjects_7.gum_bil(callback, bot)
######################################################################################################     KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'Информатика {sprint_kz}7')
def informatika(callback):
    subjects_7.informatika_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_kz} 7')
def matematika(callback):
    subjects_7.matematika_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_kz} 7')
def kaz_yaz(callback):
    subjects_7.kaz_yaz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_kz} 7')
def kaz_lit(callback):
    subjects_7.kaz_lit_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Био {sprint_kz} 7')
def bio(callback):
    subjects_7.bio_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Хим {sprint_kz} 7')
def xim(callback):
    subjects_7.xim_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Физ {sprint_kz} 7')
def fiz(callback):
    subjects_7.fiz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Иск {sprint_kz} 7')
def hkz(callback):
    subjects_7.hkz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мира {sprint_kz} 7')
def hm(callback):
    subjects_7.hm_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Гео {sprint_kz} 7')
def geo(callback):
    subjects_7.geo_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Анг {sprint_kz} 7')
def ang(callback):
    subjects_7.ang_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{mat_kz} 7')
def mat_bil(callback):
    subjects_7.mat_bil_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum_kz} 7')
def gum_bil(callback):
    subjects_7.gum_bil_kz(callback, bot)
############################################  7 class  SUBJECTS ###########################################
############################################  7 class  SUBJECTS ###########################################
############################################  7 class  SUBJECTS ###########################################


############################################  6 class  SUBJECTS ###########################################
############################################  6 class  SUBJECTS ###########################################
############################################  6 class  SUBJECTS ###########################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Информатика {sprint_ru}6')
def informatika(callback):
    subjects_6.informatika(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_ru} 6')
def matematika(callback):
    subjects_6.matematika(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_ru} 6')
def kaz_yaz(callback):
    subjects_6.kaz_yaz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_ru} 6')
def kaz_lit(callback):
    subjects_6.kaz_lit(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Био {sprint_ru} 6')
def bio(callback):
    subjects_6.bio(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Ест {sprint_ru} 6')
def est(callback):
    subjects_6.est(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Иск {sprint_ru} 6')
def hkz(callback):
    subjects_6.hkz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мира {sprint_ru} 6')
def hm(callback):
    subjects_6.hm(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Гео {sprint_ru} 6')
def geo(callback):
    subjects_6.geo(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Анг {sprint_ru} 6')
def ang(callback):
    subjects_6.ang(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{matem} 6')
def mat_bil(callback):
    subjects_6.mat_bil(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum} 6')
def gum_bil(callback):
    subjects_6.gum_bil(callback, bot)

######################################################################################################     KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'Информатика {sprint_kz}6')
def informatika(callback):
    subjects_6.informatika_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_kz} 6')
def matematika(callback):
    subjects_6.matematika_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_kz} 6')
def kaz_yaz(callback):
    subjects_6.kaz_yaz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_kz} 6')
def kaz_lit(callback):
    subjects_6.kaz_lit_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Био {sprint_kz} 6')
def bio(callback):
    subjects_6.bio_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Ест {sprint_kz} 6')
def est(callback):
    subjects_6.est_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Иск {sprint_kz} 6')
def hkz(callback):
    subjects_6.hkz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мира {sprint_kz} 6')
def hm(callback):
    subjects_6.hm_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Гео {sprint_kz} 6')
def geo(callback):
    subjects_6.geo_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Анг {sprint_kz} 6')
def ang(callback):
    subjects_6.ang_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{mat_kz} 6')
def mat_bil(callback):
    subjects_6.mat_bil_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum_kz} 6')
def gum_bil(callback):
    subjects_6.gum_bil_kz(callback, bot)
############################################  6 class  SUBJECTS ###########################################


############################################  5 class  SUBJECTS ###########################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Информатика {sprint_ru}5')
def informatika(callback):
    subjects_5.informatika(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_ru} 5')
def matematika(callback):
    subjects_5.matematika(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_ru} 5')
def kaz_yaz(callback):
    subjects_5.kaz_yaz(callback, bot)

@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_ru} 5')
def kaz_lit(callback):
    subjects_5.kaz_lit(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Ест {sprint_ru} 5')
def est(callback):
    subjects_5.est(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Иск {sprint_ru} 5')
def hkz(callback):
    subjects_5.hkz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мира {sprint_ru} 5')
def hm(callback):
    subjects_5.hm(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Гео {sprint_ru} 5')
def geo(callback):
    subjects_5.geo(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Анг {sprint_ru} 5')
def ang(callback):
    subjects_5.ang(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{matem} 5')
def mat_bil(callback):
    subjects_5.mat_bil(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum} 5')
def gum_bil(callback):
    subjects_5.gum_bil(callback, bot)

######################################################################################################     KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'Информатика {sprint_kz}5')
def informatika(callback):
    subjects_5.informatika_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_kz} 5')
def matematika(callback):
    subjects_5.matematika_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_kz} 5')
def kaz_yaz(callback):
    subjects_5.kaz_yaz_kz(callback, bot)

@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_kz} 5')
def kaz_lit(callback):
    subjects_5.kaz_lit_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Ест {sprint_kz} 5')
def est(callback):
    subjects_5.est_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Иск {sprint_kz} 5')
def hkz(callback):
    subjects_5.hkz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мира {sprint_kz} 5')
def hm(callback):
    subjects_5.hm_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Гео {sprint_kz} 5')
def geo(callback):
    subjects_5.geo_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Анг {sprint_kz} 5')
def ang(callback):
    subjects_5.ang_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{mat_kz} 5')
def mat_bil(callback):
    subjects_5.mat_bil_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{gum_kz} 5')
def gum_bil(callback):
    subjects_5.gum_bil_kz(callback, bot)
############################################  5 class  SUBJECTS ###########################################
############################################  5 class  SUBJECTS ###########################################
############################################  5 class  SUBJECTS ###########################################


############################################  11 class  ###########################################
############################################  11 class  ###########################################
############################################  11 class  ###########################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 11')
def reply_list_ru(callback):
    subjects_11.reply_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru} 11')
def reply_sprint_ru(callback):
    subjects_11.reply_sprint_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_ru} 11')
def reply_sprint_list_ru(callback):
    subjects_11.reply_sprint_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_ru} 11')
def reply_bilik_time_ru(callback):
    subjects_11.reply_bilik_time_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_ru} 11')
def reply_bilik_time_list_ru(callback):
    subjects_11.reply_bilik_time_list_ru(callback, bot)

###################################################################################################        KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 11kz')
def reply_list_ru(callback):
    subjects_11.reply_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz} 11')
def reply_sprint_ru(callback):
    subjects_11.reply_sprint_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_kz} 11')
def reply_sprint_list_ru(callback):
    subjects_11.reply_sprint_list_kz(callback, bot)

@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_kz} 11')
def reply_bilik_time_ru(callback):
    subjects_11.reply_bilik_time_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_kz} 11')
def reply_bilik_time_list_ru(callback):
    subjects_11.reply_bilik_time_list_kz(callback, bot)
#######################################   11 class   #######################################
#######################################   11 class   #######################################
#######################################   11 class   #######################################

#######################################   10 class   #######################################
#######################################   10 class   #######################################
#######################################   10 class   #######################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 10')
def reply_list_ru(callback):
    subjects_10.reply_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru} 10')
def reply_sprint_ru(callback):
    subjects_10.reply_sprint_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_ru} 10')
def reply_sprint_list_ru(callback):
    subjects_10.reply_sprint_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_ru} 10')
def reply_bilik_time_ru(callback):
    subjects_10.reply_bilik_time_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_ru} 10')
def reply_bilik_time_list_ru(callback):
    subjects_10.reply_bilik_time_list_ru(callback, bot)
###################################################################################################        KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 10kz')
def reply_list_ru(callback):
    subjects_10.reply_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz} 10')
def reply_sprint_ru(callback):
    subjects_10.reply_sprint_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_kz} 10')
def reply_sprint_list_ru(callback):
    subjects_10.reply_sprint_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_kz} 10')
def reply_bilik_time_ru(callback):
    subjects_10.reply_bilik_time_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_kz} 10')
def reply_bilik_time_list_ru(callback):
    subjects_10.reply_bilik_time_list_kz(callback, bot)
#######################################   10 class   #######################################
#######################################   10 class   #######################################
#######################################   10 class   #######################################

#######################################   9 class   #######################################
#######################################   9 class   #######################################
#######################################   9 class   #######################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 9')
def reply_list_ru(callback):
    subjects_9.reply_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru} 9')
def reply_sprint_ru(callback):
    subjects_9.reply_sprint_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_ru} 9')
def reply_sprint_list_ru(callback):
    subjects_9.reply_sprint_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_ru} 9')
def reply_bilik_time_ru(callback):
    subjects_9.reply_bilik_time_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_ru} 9')
def reply_bilik_time_list_ru(callback):
    subjects_9.reply_bilik_time_list_ru(callback, bot)
###################################################################################################        KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 9kz')
def reply_list_ru(callback):
    subjects_9.reply_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz} 9')
def reply_sprint_ru(callback):
    subjects_9.reply_sprint_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_kz} 9')
def reply_sprint_list_ru(callback):
    subjects_9.reply_sprint_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_kz} 9')
def reply_bilik_time_ru(callback):
    subjects_9.reply_bilik_time_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_kz} 9')
def reply_bilik_time_list_ru(callback):
    subjects_9.reply_bilik_time_list_kz(callback, bot)
#######################################   9 class   #######################################
#######################################   9 class   #######################################
#######################################   9 class   #######################################


#######################################   8 class   #######################################
#######################################   8 class   #######################################
#######################################   8 class   #######################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 8')
def reply_list_ru(callback):
    subjects_8.reply_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru} 8')
def reply_sprint_ru(callback):
    subjects_8.reply_sprint_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_ru} 8')
def reply_sprint_list_ru(callback):
    subjects_8.reply_sprint_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_ru} 8')
def reply_bilik_time_ru(callback):
    subjects_8.reply_bilik_time_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_ru} 8')
def reply_bilik_time_list_ru(callback):
    subjects_8.reply_bilik_time_list_ru(callback, bot)
###################################################################################################        KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 8kz')
def reply_list_ru(callback):
    subjects_8.reply_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz} 8')
def reply_sprint_ru(callback):
    subjects_8.reply_sprint_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_kz} 8')
def reply_sprint_list_ru(callback):
    subjects_8.reply_sprint_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_kz} 8')
def reply_bilik_time_ru(callback):
    subjects_8.reply_bilik_time_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_kz} 8')
def reply_bilik_time_list_ru(callback):
    subjects_8.reply_bilik_time_list_kz(callback, bot)
#######################################   8 class   #######################################
#######################################   8 class   #######################################
#######################################   8 class   #######################################


#######################################   7 class   #######################################
#######################################   7 class   #######################################
#######################################   7 class   #######################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 7')
def reply_list_ru(callback):
    subjects_7.reply_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru} 7')
def reply_sprint_ru(callback):
    subjects_7.reply_sprint_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_ru} 7')
def reply_sprint_list_ru(callback):
    subjects_7.reply_sprint_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_ru} 7')
def reply_bilik_time_ru(callback):
    subjects_7.reply_bilik_time_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_ru} 7')
def reply_bilik_time_list_ru(callback):
    subjects_7.reply_bilik_time_list_ru(callback, bot)
###################################################################################################        KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 7kz')
def reply_list_ru(callback):
    subjects_7.reply_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz} 7')
def reply_sprint_ru(callback):
    subjects_7.reply_sprint_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_kz} 7')
def reply_sprint_list_ru(callback):
    subjects_7.reply_sprint_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_kz} 7')
def reply_bilik_time_ru(callback):
    subjects_7.reply_bilik_time_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_kz} 7')
def reply_bilik_time_list_ru(callback):
    subjects_7.reply_bilik_time_list_kz(callback, bot)
#######################################   7 class   #######################################
#######################################   7 class   #######################################
#######################################   7 class   #######################################

#######################################   6 class   #######################################
#######################################   6 class   #######################################
#######################################   6 class   #######################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 6')
def reply_list_ru(callback):
    subjects_6.reply_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru} 6')
def reply_sprint_ru(callback):
    subjects_6.reply_sprint_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_ru} 6')
def reply_sprint_list_ru(callback):
    subjects_6.reply_sprint_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_ru} 6')
def reply_bilik_time_ru(callback):
    subjects_6.reply_bilik_time_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_ru} 6')
def reply_bilik_time_list_ru(callback):
    subjects_6.reply_bilik_time_list_ru(callback, bot)
###################################################################################################        KZ

@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 6kz')
def reply_list_ru(callback):
    subjects_6.reply_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz} 6')
def reply_sprint_ru(callback):
    subjects_6.reply_sprint_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_kz} 6')
def reply_sprint_list_ru(callback):
    subjects_6.reply_sprint_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_kz} 6')
def reply_bilik_time_ru(callback):
    subjects_6.reply_bilik_time_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_kz} 6')
def reply_bilik_time_list_ru(callback):
    subjects_6.reply_bilik_time_list_kz(callback, bot)
#######################################   6 class   #######################################
#######################################   6 class   #######################################
#######################################   6 class   #######################################


#######################################   5 class   #######################################
#######################################   5 class   #######################################
#######################################   5 class   #######################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 5')
def reply_sprint_ru(callback):
    subjects_5.reply_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru} 5')
def reply_sprint_ru(callback):
    subjects_5.reply_sprint_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_ru} 5')
def reply_sprint_list_ru(callback):
    subjects_5.reply_sprint_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_ru} 5')
def reply_bilik_time_ru(callback):
    subjects_5.reply_bilik_time_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_ru} 5')
def reply_bilik_time_list_ru(callback):
    subjects_5.reply_bilik_time_list_ru(callback, bot)

##################################################################################################          KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 5kz')
def reply_sprint_ru(callback):
    subjects_5.reply_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz} 5')
def reply_sprint_ru(callback):
    subjects_5.reply_sprint_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_kz} 5')
def reply_sprint_list_ru(callback):
    subjects_5.reply_sprint_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_kz} 5')
def reply_bilik_time_ru(callback):
    subjects_5.reply_bilik_time_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_kz} 5')
def reply_bilik_time_list_ru(callback):
    subjects_5.reply_bilik_time_list_kz(callback, bot)
#######################################   5 class   #######################################
#######################################   5 class   #######################################
#######################################   5 class   #######################################


#######################################   4 class  SUBJECTS  #######################################
#######################################   4 class  SUBJECTS  #######################################
#######################################   4 class  SUBJECTS  #######################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_ru} 4')
def mat(callback):
    subjects_4.mat(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_ru} 4')
def kaz(callback):
    subjects_4.kaz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_ru} 4')
def kazl(callback):
    subjects_4.kazl(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_ru} 4')
def reply_bilik_time_list_ru(callback):
    subjects_4.reply_bilik_time_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {doda_ru} 4')
def reply_doda_dir_kz(callback):
    subjects_4.reply_doda_dir_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_dir_lan_ru}4')
def reply_doda_lan_kz(callback):
    subjects_4.lan_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_dir_log_ru}4')
def reply_doda_log_kz(callback):
    subjects_4.log_ru(callback, bot)
#############################################################################################################    KZ

@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_kz} 4')
def mat(callback):
    subjects_4.mat_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_kz} 4')
def kaz(callback):
    subjects_4.kaz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_kz} 4')
def kazl(callback):
    subjects_4.kazl_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_kz} 4')
def reply_bilik_time_list_kz(callback):
    subjects_4.reply_bilik_time_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {doda_kz} 4')
def reply_doda_dir_kz(callback):
    subjects_4.reply_doda_dir_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_dir_lan_kz}4')
def reply_doda_lan_kz(callback):
    subjects_4.lan_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_dir_log_kz}4')
def reply_doda_log_kz(callback):
    subjects_4.log_kz(callback, bot)
#######################################   4 class  SUBJECTS  #######################################
#######################################   4 class  SUBJECTS  #######################################
#######################################   4 class  SUBJECTS  #######################################

#######################################   3 class  SUBJECTS  #######################################
#######################################   3 class  SUBJECTS  #######################################
#######################################   3 class  SUBJECTS  #######################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_ru} 3')
def mat(callback):
    subjects_3.mat(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_ru} 3')
def kaz(callback):
    subjects_3.kaz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_ru} 3')
def kazl(callback):
    subjects_3.kazl(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_ru} 3')
def reply_bilik_time_list_ru(callback):
    subjects_3.reply_bilik_time_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {doda_ru} 3')
def reply_doda_dir_kz(callback):
    subjects_3.reply_doda_dir_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_dir_lan_ru}3')
def reply_doda_lan_kz(callback):
    subjects_3.lan_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_dir_log_ru}3')
def reply_doda_log_kz(callback):
    subjects_3.log_ru(callback, bot)
###########################################################################################################     KZ

@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_kz} 3')
def mat_kz(callback):
    subjects_3.mat_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_kz} 3')
def kaz_kz(callback):
    subjects_3.kaz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_kz} 3')
def kazl_kz(callback):
    subjects_3.kazl_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_kz} 3')
def reply_bilik_time_list_kz(callback):
    subjects_3.reply_bilik_time_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {doda_kz} 3')
def reply_doda_dir_kz(callback):
    subjects_3.reply_doda_dir_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_dir_lan_kz}3')
def reply_doda_lan_kz(callback):
    subjects_3.lan_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_dir_log_kz}3')
def reply_doda_log_kz(callback):
    subjects_3.log_kz(callback, bot)
#######################################   3 class  SUBJECTS  #######################################
#######################################   3 class  SUBJECTS  #######################################
#######################################   3 class  SUBJECTS  #######################################


#######################################   2 class  SUBJECTS  #######################################
#######################################   2 class  SUBJECTS  #######################################
#######################################   2 class  SUBJECTS  #######################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_ru} 2')
def mat(callback):
    subjects_2.mat(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_ru} 2')
def kaz(callback):
    subjects_2.kaz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_ru} 2')
def kazl(callback):
    subjects_2.kazl(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_ru} 2')
def reply_bilik_time_list_ru(callback):
    subjects_2.reply_bilik_time_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {doda_ru} 2')
def reply_doda_dir_kz(callback):
    subjects_2.reply_doda_dir_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_dir_lan_ru}2')
def reply_doda_lan_kz(callback):
    subjects_2.lan_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_dir_log_ru}2')
def reply_doda_log_kz(callback):
    subjects_2.log_ru(callback, bot)
#########################################################################################################       KZ

@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_kz} 2')
def mat_kz(callback):
    subjects_2.mat_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_kz} 2')
def kaz_kz(callback):
    subjects_2.kaz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Казл {sprint_kz} 2')
def kazl_kz(callback):
    subjects_2.kazl_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_kz} 2')
def reply_bilik_time_list_kz(callback):
    subjects_2.reply_bilik_time_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_kz} 1')
def reply_bilik_time_list_kz(callback):
    subjects_1.reply_bilik_time_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {doda_kz} 2')
def reply_doda_dir_kz(callback):
    subjects_2.reply_doda_dir_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_dir_lan_kz}2')
def reply_doda_lan_kz(callback):
    subjects_2.lan_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_dir_log_kz}2')
def reply_doda_log_kz(callback):
    subjects_2.log_kz(callback, bot)
#######################################   2 class  SUBJECTS  #######################################
#######################################   2 class  SUBJECTS  #######################################
#######################################   2 class  SUBJECTS  #######################################


#######################################   1 class  SUBJECTS  #######################################
#######################################   1 class  SUBJECTS  #######################################
#######################################   1 class  SUBJECTS  #######################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_ru} 1')
def mat(callback):
    # attention_ru(callback)
    subjects_1.mat(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_ru} 1')
def kaz(callback):
    subjects_1.kaz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_ru} 1')
def reply_bilik_time_list_ru(callback):
    subjects_1.reply_bilik_time_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {doda_ru} 1')
def reply_doda_dir_kz(callback):
    subjects_1.reply_doda_dir_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_dir_lan_ru}1')
def reply_doda_lan_kz(callback):
    subjects_1.lan_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_dir_log_ru}1')
def reply_doda_log_kz(callback):
    subjects_1.log_ru(callback, bot)
############################################################################################################        KZ

@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {sprint_kz} 1')
def mat_kz(callback):
    subjects_1.mat(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {sprint_kz} 1')
def kaz_kz(callback):
    subjects_1.kaz_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {bala_time_kz} 1')
def reply_bilik_time_list_kz(callback):
    subjects_1.reply_bilik_time_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нап {doda_kz} 1')
def reply_doda_dir_kz(callback):
    subjects_1.reply_doda_dir_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_dir_lan_kz}1')
def reply_doda_lan_kz(callback):
    subjects_1.lan_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_dir_log_kz}1')
def reply_doda_log_kz(callback):
    subjects_1.log_kz(callback, bot)
#######################################   1 class  SUBJECTS  #######################################
#######################################   1 class  SUBJECTS  #######################################
#######################################   1 class  SUBJECTS  #######################################


#######################################   4 class   #######################################
#######################################   4 class   #######################################
#######################################   4 class   #######################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 4')
def reply_list_ru(callback):
    subjects_4.reply_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru} 4')
def reply_sprint_ru(callback):
    subjects_4.reply_sprint_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_ru} 4')
def reply_sprint_list_ru(callback):
    subjects_4.reply_sprint_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_ru} 4')
def reply_bilik_time_ru(callback):
    subjects_4.reply_bilik_time_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_ru} 4')
def reply_doda_ru(callback):
    subjects_4.reply_doda_ru(callback, bot)
##########################################################################################################    KZ

@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 4kz')
def reply_list_ru(callback):
    subjects_4.reply_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz} 4')
def reply_sprint_ru(callback):
    subjects_4.reply_sprint_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_kz} 4')
def reply_sprint_list_ru(callback):
    subjects_4.reply_sprint_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_kz} 4')
def reply_bilik_time_ru(callback):
    subjects_4.reply_bilik_time_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_kz} 4')
def reply_doda_kz(callback):
    subjects_4.reply_doda_kz(callback, bot)

#######################################   4 class   #######################################
#######################################   4 class   #######################################
#######################################   4 class   #######################################


#######################################   3 class   #######################################
#######################################   3 class   #######################################
#######################################   3 class   #######################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 3')
def reply_list_ru(callback):
    subjects_3.reply_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru} 3')
def reply_sprint_ru(callback):
    subjects_3.reply_sprint_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_ru} 3')
def reply_sprint_list_ru(callback):
    subjects_3.reply_sprint_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_ru} 3')
def reply_bilik_time_ru(callback):
    subjects_3.reply_bilik_time_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_ru} 3')
def reply_doda_ru(callback):
    subjects_3.reply_doda_ru(callback, bot)
####################################################################################################    KZ

@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 3kz')
def reply_list_kz(callback):
    subjects_3.reply_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz} 3')
def reply_sprint_kz(callback):
    subjects_3.reply_sprint_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_kz} 3')
def reply_sprint_list_kz(callback):
    subjects_3.reply_sprint_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_kz} 3')
def reply_bilik_time_kz(callback):
    subjects_3.reply_bilik_time_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_kz} 3')
def reply_doda_kz(callback):
    subjects_3.reply_doda_kz(callback, bot)
#######################################   3 class   #######################################
#######################################   3 class   #######################################
#######################################   3 class   #######################################


#######################################   2 class   #######################################
#######################################   2 class   #######################################
#######################################   2 class   #######################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 2')
def reply_list_ru(callback):
    subjects_2.reply_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru} 2')
def reply_sprint_ru(callback):
    subjects_2.reply_sprint_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_ru} 2')
def reply_sprint_list_ru(callback):
    subjects_2.reply_sprint_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_ru} 2')
def reply_bilik_time_ru(callback):
    subjects_2.reply_bilik_time_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_ru} 2')
def reply_doda_ru(callback):
    subjects_2.reply_doda_ru(callback, bot)
#####################################################################################################       KZ

@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 2kz')
def reply_list_kz(callback):
    subjects_2.reply_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz} 2')
def reply_sprint_kz(callback):
    subjects_2.reply_sprint_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_kz} 2')
def reply_sprint_list_kz(callback):
    subjects_2.reply_sprint_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_kz} 2')
def reply_bilik_time_kz(callback):
    subjects_2.reply_bilik_time_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_kz} 2')
def reply_doda_kz(callback):
    subjects_2.reply_doda_kz(callback, bot)
#######################################   2 class   #######################################
#######################################   2 class   #######################################
#######################################   2 class   #######################################

#######################################   1 class   #######################################
#######################################   1 class   #######################################
#######################################   1 class   #######################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 1')
def reply_list_ru(callback):
    subjects_1.reply_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_ru} 1')
def reply_sprint_ru(callback):
    subjects_1.reply_sprint_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_ru} 1')
def reply_sprint_list_ru(callback):
    subjects_1.reply_sprint_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_ru} 1')
def reply_bilik_time_ru(callback):
    subjects_1.reply_bilik_time_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_ru} 1')
def reply_doda_ru(callback):
    subjects_1.reply_doda_ru(callback, bot)
######################################################################################################      KZ
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 1kz')
def reply_list_kz(callback):
    subjects_1.reply_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{sprint_kz} 1')
def reply_sprint_kz(callback):
    subjects_1.reply_sprint_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Список {sprint_kz} 1')
def reply_sprint_list_kz(callback):
    subjects_1.reply_sprint_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{bala_time_kz} 1')
def reply_bilik_time_kz(callback):
    subjects_1.reply_bilik_time_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{doda_kz} 1')
def reply_doda_kz(callback):
    subjects_1.reply_doda_kz(callback, bot)
#######################################   1 class   #######################################
#######################################   1 class   #######################################
#######################################   1 class   #######################################

############################################    TEACHER    ##################################################
############################################    TEACHER    ##################################################
############################################    TEACHER    ##################################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 0')
def olimp_ru(callback: CallbackQuery):
    ped_olymp.olimp_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{pedagog_ru}')
def bil_ped_ru(callback: CallbackQuery):
    ped_olymp.bil_ped_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Спис {pedagog_ru}')
def ped_list_ru(callback: CallbackQuery):
    ped_olymp.ped_list_ru(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Олимпиады 0kz')
def olimp_ru(callback: CallbackQuery):
    ped_olymp.olimp_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'{pedagog_kz}')
def bil_ped_ru(callback: CallbackQuery):
    ped_olymp.bil_ped_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Спис {pedagog_kz}')
def ped_list_ru(callback: CallbackQuery):
    ped_olymp.ped_list_kz(callback, bot)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Анг {pedagog_ru}')
def t_ang(callback: CallbackQuery):
    ped_start_olymp.subj_info(callback, bot, "Английский язык")

@bot.callback_query_handler(func=lambda callback: callback.data == "pАнглийский язык_ru")
def t_ang_s(callback: CallbackQuery):
    ped_start_olymp.test_req(callback, bot, "Английский язык")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tАнглийский язык_ru')
def ang_test(callback):
    start_test(callback, 500, 1868)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нач {pedagog_ru}')
def t_nach(callback: CallbackQuery):
    ped_start_olymp.subj_info(callback, bot, "Начальные классы")

@bot.callback_query_handler(func=lambda callback: callback.data == "pНачальные классы_ru")
def t_nach_s(callback: CallbackQuery):
    ped_start_olymp.test_req(callback, bot, "Начальные классы")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tНачальные классы_ru')
def nach_test(callback):
    start_test(callback, 500, 1869)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Био {pedagog_ru}')
def t_bio(callback: CallbackQuery):
    ped_start_olymp.subj_info(callback, bot, "Биология")

@bot.callback_query_handler(func=lambda callback: callback.data == "pБиология_ru")
def t_bio_s(callback: CallbackQuery):
    ped_start_olymp.test_req(callback, bot, "Биология")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tБиология_ru')
def bio_test(callback):
    start_test(callback, 500, 1870)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Гео {pedagog_ru}')
def t_geo(callback: CallbackQuery):
    ped_start_olymp.subj_info(callback, bot, "География")

@bot.callback_query_handler(func=lambda callback: callback.data == "pГеография_ru")
def t_geo_s(callback: CallbackQuery):
    ped_start_olymp.test_req(callback, bot, "География")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tГеография_ru')
def geo_test(callback):
    start_test(callback, 500, 1871)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Инф {pedagog_ru}')
def t_inf(callback: CallbackQuery):
    ped_start_olymp.subj_info(callback, bot, "Информатика")

@bot.callback_query_handler(func=lambda callback: callback.data == "pИнформатика_ru")
def t_inf_s(callback: CallbackQuery):
    ped_start_olymp.test_req(callback, bot, "Информатика")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tИнформатика_ru')
def inf_test(callback):
    start_test(callback, 500, 1872)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Труд {pedagog_ru}')
def t_trud(callback: CallbackQuery):
    ped_start_olymp.subj_info(callback, bot, "Труд")

@bot.callback_query_handler(func=lambda callback: callback.data == "pТруд_ru")
def t_trud_s(callback: CallbackQuery):
    ped_start_olymp.test_req(callback, bot, "Труд")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tТруд_ru')
def trud_test(callback):
    start_test(callback, 500, 1873)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {pedagog_ru}')
def t_mat(callback: CallbackQuery):
    ped_start_olymp.subj_info(callback, bot, "Математика")

@bot.callback_query_handler(func=lambda callback: callback.data == "pМатематика_ru")
def t_mat_s(callback: CallbackQuery):
    ped_start_olymp.test_req(callback, bot, "Математика")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tМатематика_ru')
def mat_test(callback):
    start_test(callback, 500, 1875)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Рус {pedagog_ru}')
def t_rus(callback: CallbackQuery):
    ped_start_olymp.subj_info(callback, bot, "Русский язык")

@bot.callback_query_handler(func=lambda callback: callback.data == "pРусский язык_ru")
def t_rus_s(callback: CallbackQuery):
    ped_start_olymp.test_req(callback, bot, "Русский язык")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tРусский язык_ru')
def rus_test(callback):
    start_test(callback, 500, 1876)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Сам {pedagog_ru}')
def t_sam(callback: CallbackQuery):
    ped_start_olymp.subj_info(callback, bot, "Самопознание")

@bot.callback_query_handler(func=lambda callback: callback.data == "pСамопознание_ru")
def t_sam_s(callback: CallbackQuery):
    ped_start_olymp.test_req(callback, bot, "Самопознание")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tСамопознание_ru')
def sam_test(callback):
    start_test(callback, 500, 1883)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Ист {pedagog_ru}')
def t_hist(callback: CallbackQuery):
    ped_start_olymp.subj_info(callback, bot, "История")

@bot.callback_query_handler(func=lambda callback: callback.data == "pИстория_ru")
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.test_req(callback, bot, "История")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tИстория_ru')
def sam_test(callback):
    start_test(callback, 500, 1878)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Физ {pedagog_ru}')
def t_fiz(callback: CallbackQuery):
    ped_start_olymp.subj_info(callback, bot, "Физика")

@bot.callback_query_handler(func=lambda callback: callback.data == "pФизика_ru")
def t_fiz_s(callback: CallbackQuery):
    ped_start_olymp.test_req(callback, bot, "Физика")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tФизика_ru')
def fiz_test(callback):
    start_test(callback, 500, 1879)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Хим {pedagog_ru}')
def t_xim(callback: CallbackQuery):
    ped_start_olymp.subj_info(callback, bot, "Химия")

@bot.callback_query_handler(func=lambda callback: callback.data == "pХимия_ru")
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.test_req(callback, bot, "Химия")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tХимия_ru')
def fiz_test(callback):
    start_test(callback, 500, 1880)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Физра {pedagog_ru}')
def t_log(callback: CallbackQuery):
    ped_start_olymp.subj_info(callback, bot, "Физкультура")

@bot.callback_query_handler(func=lambda callback: callback.data == "pФизкультура_ru")
def t_log_s(callback: CallbackQuery):
    ped_start_olymp.test_req(callback, bot, "Физкультура")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tФизкультура_ru')
def log_test(callback):
    start_test(callback, 500, 1881)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {pedagog_ru}')
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.subj_info(callback, bot, "Каз. язык и литература")

@bot.callback_query_handler(func=lambda callback: callback.data == "pКаз. язык и литература_ru")
def t_kaz_s(callback: CallbackQuery):
    ped_start_olymp.test_req(callback, bot, "Каз. язык и литература")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tКаз. язык и литература_ru')
def kaz_test(callback):
    start_test(callback, 500, 1874)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Пед {pedagog_ru}')
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.subj_info(callback, bot, "Педагогика-Психология")

@bot.callback_query_handler(func=lambda callback: callback.data == "pПедагогика-Психология_ru")
def t_kaz_s(callback: CallbackQuery):
    ped_start_olymp.test_req(callback, bot, "Педагогика-Психология")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tПедагогика-Психология_ru')
def kaz_test(callback):
    start_test(callback, 500, 1882)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Анг {pedagog_kz}')
def t_ang(callback: CallbackQuery):
    ped_start_olymp.subj_info_kz(callback, bot, "Ағылшын тілі")

@bot.callback_query_handler(func=lambda callback: callback.data == "pАғылшын тілі_kz")
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.test_req_kz(callback, bot, "Ағылшын тілі")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tАғылшын тілі_kz')
def ang_test(callback):
    start_test(callback, 500, 1868)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Нач {pedagog_kz}')
def t_nach(callback: CallbackQuery):
    ped_start_olymp.subj_info_kz(callback, bot, "Бастауыш сынып")

@bot.callback_query_handler(func=lambda callback: callback.data == "pБастауыш сынып_kz")
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.test_req_kz(callback, bot, "Бастауыш сынып")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tБастауыш сынып_kz')
def nach_test(callback):
    start_test(callback, 500, 1869)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Био {pedagog_kz}')
def t_bio(callback: CallbackQuery):
    ped_start_olymp.subj_info_kz(callback, bot, "Биология")

@bot.callback_query_handler(func=lambda callback: callback.data == "pБиология_kz")
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.test_req_kz(callback, bot, "Биология")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tБиология_kz')
def bio_test(callback):
    start_test(callback, 500, 1870)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Гео {pedagog_kz}')
def t_geo(callback: CallbackQuery):
    ped_start_olymp.subj_info_kz(callback, bot, "География")

@bot.callback_query_handler(func=lambda callback: callback.data == "pГеография_kz")
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.test_req_kz(callback, bot, "География")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tГеография_kz')
def geo_test(callback):
    start_test(callback, 500, 1871)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Инф {pedagog_kz}')
def t_inf(callback: CallbackQuery):
    ped_start_olymp.subj_info_kz(callback, bot, "Информатика")

@bot.callback_query_handler(func=lambda callback: callback.data == "pИнформатика_kz")
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.test_req_kz(callback, bot, "Информатика")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tИнформатика_kz')
def inf_test(callback):
    start_test(callback, 500, 1872)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Труд {pedagog_kz}')
def t_trud(callback: CallbackQuery):
    ped_start_olymp.subj_info_kz(callback, bot, "Еңбек")

@bot.callback_query_handler(func=lambda callback: callback.data == "pЕңбек_kz")
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.test_req_kz(callback, bot, "Еңбек")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tЕңбек_kz')
def trud_test(callback):
    start_test(callback, 500, 1873)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Мат {pedagog_kz}')
def t_mat(callback: CallbackQuery):
    ped_start_olymp.subj_info_kz(callback, bot, "Математика")

@bot.callback_query_handler(func=lambda callback: callback.data == "pМатематика_kz")
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.test_req_kz(callback, bot, "Математика")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tМатематика_kz')
def mat_test(callback):
    start_test(callback, 500, 1875)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Рус {pedagog_kz}')
def t_rus(callback: CallbackQuery):
    ped_start_olymp.subj_info_kz(callback, bot, "Орыс тілі")

@bot.callback_query_handler(func=lambda callback: callback.data == "pОрыс тілі_kz")
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.test_req_kz(callback, bot, "Орыс тілі")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tОрыс тілі_kz')
def rus_test(callback):
    start_test(callback, 500, 1876)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Сам {pedagog_kz}')
def t_sam(callback: CallbackQuery):
    ped_start_olymp.subj_info_kz(callback, bot, "Өзін-өзі тану")

@bot.callback_query_handler(func=lambda callback: callback.data == "pӨзін-өзі тану_kz")
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.test_req_kz(callback, bot, "Өзін-өзі тану")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tӨзін-өзі тану_kz')
def sam_test(callback):
    start_test(callback, 500, 1877)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Ист {pedagog_kz}')
def t_hist(callback: CallbackQuery):
    ped_start_olymp.subj_info_kz(callback, bot, "Тарих")

@bot.callback_query_handler(func=lambda callback: callback.data == "pТарих_kz")
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.test_req_kz(callback, bot, "Тарих")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tТарих_kz')
def sam_test(callback):
    start_test(callback, 500, 1878)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Физ {pedagog_kz}')
def t_fiz(callback: CallbackQuery):
    ped_start_olymp.subj_info_kz(callback, bot, "Физика")

@bot.callback_query_handler(func=lambda callback: callback.data == "pФизика_kz")
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.test_req_kz(callback, bot, "Физика")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tФизика_kz')
def fiz_test(callback):
    start_test(callback, 500, 1879)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Хим {pedagog_kz}')
def t_xim(callback: CallbackQuery):
    ped_start_olymp.subj_info_kz(callback, bot, "Химия")

@bot.callback_query_handler(func=lambda callback: callback.data == "pХимия_kz")
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.test_req_kz(callback, bot, "Химия")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tХимия_kz')
def fiz_test(callback):
    start_test(callback, 500, 1880)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Физра {pedagog_kz}')
def t_log(callback: CallbackQuery):
    ped_start_olymp.subj_info_kz(callback, bot, "Дене шынықтыру")

@bot.callback_query_handler(func=lambda callback: callback.data == "pДене шынықтыру_kz")
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.test_req_kz(callback, bot, "Дене шынықтыру")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tДене шынықтыру_kz')
def log_test(callback):
    start_test(callback, 500, 1881)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Каз {pedagog_kz}')
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.subj_info_kz(callback, bot, "Қаз. тілі және әдебиеті")

@bot.callback_query_handler(func=lambda callback: callback.data == "pҚаз. тілі және әдебиеті_kz")
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.test_req_kz(callback, bot, "Қаз. тілі және әдебиеті")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tҚаз. тілі және әдебиеті_kz')
def kaz_test(callback):
    start_test(callback, 500, 1874)


@bot.callback_query_handler(func=lambda callback: callback.data == f'Пед {pedagog_kz}')
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.subj_info_kz(callback, bot, "Педагогика-Психология")

@bot.callback_query_handler(func=lambda callback: callback.data == "pПедагогика-Психология_kz")
def t_kaz(callback: CallbackQuery):
    ped_start_olymp.test_req_kz(callback, bot, "Педагогика-Психология")

@bot.callback_query_handler(func=lambda callback: callback.data == f'tПедагогика-Психология_kz')
def kaz_test(callback):
    start_test(callback, 500, 1882)
############################################    TEACHER    ##################################################
############################################    TEACHER    ##################################################
############################################    TEACHER    ##################################################

###############################  CONDITIONALS  ###############################################
@bot.callback_query_handler(func=lambda callback: callback.data == f'Положение {sprint_ru}')
def reply_condition_sprint_ru(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(bilgen_sprint_path_ru, 'rb'))
    except ConnectionError:
        pass


@bot.callback_query_handler(func=lambda callback: callback.data == f'Положение {bala_time_ru}')
def reply_condition_bilik_time_ru(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(bilik_ru_path, 'rb'))
    except ConnectionError:
        pass


@bot.callback_query_handler(func=lambda callback: callback.data == f'Положение {sprint_kz}')
def reply_condition_sprint_ru(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(bilgen_sprint_path_kz, 'rb'))
    except ConnectionError:
        pass


@bot.callback_query_handler(func=lambda callback: callback.data == f'Положение {bala_time_kz}')
def reply_condition_bilik_time_ru(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(bilik_kz_path, 'rb'))
    except ConnectionError:
        pass


@bot.callback_query_handler(func=lambda callback: callback.data == f'Положение {doda_kz}')
def reply_condition_doda_kz(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(doda_path_kz, 'rb'))
    except ConnectionError:
        pass


@bot.callback_query_handler(func=lambda callback: callback.data == f'Положение {doda_ru}')
def reply_condition_doda_ru(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(doda_path_ru, 'rb'))
    except ConnectionError:
        pass

###############################  CONDITIONALS  ###############################################

##############################################################################################
##############################################################################################


def decorator(func, arg1, arg2=None, arg3=None):
    if arg2 is None:
        return func(arg1)
    else: return func(arg1, arg2, arg3)

sql = SQL_db()
def check_password(id, password):
    username = sql.get_iin(id)
    if username is None:
        bot.send_message(id, text='Incorrect')
        return
    salt = 'te1grBi1genPa$$4eck'
    token_string = f'{username};{password};{salt}'.encode()
    token = hashlib.sha512(token_string).hexdigest()
    url = "https://bilgen.academy/intranet/login_api.php"

    payload = {'username': f'{username}',
               'password': f'{password}',
               'token': f'{token}'}

    files = []

    headers = {
        'Cookie': 'MoodleSession=k3arbdujce7dnd0spktc1um5c0'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response.text


@bot.callback_query_handler(func=lambda callback: callback.data == 'Атырауская область')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=6)


@bot.callback_query_handler(func=lambda callback: callback.data == 'ВКО')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=16)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Костанайская область')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=10)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Мангистауская область')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=12)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Кызылординская область')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=11)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Жамбылская область')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=8)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Карагандинская область')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=9)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Туркистанская область')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=13)


@bot.callback_query_handler(func=lambda callback: callback.data == 'ЗКО')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=7)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Акмолинская область')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=3)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Актюбинская область')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=4)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Павлодарская область')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=14)


@bot.callback_query_handler(func=lambda callback: callback.data == 'СКО')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=15)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Алматинская область')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=5)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Нур-Султан')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=1)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Алматы')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=2)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Шымкент')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=19)
####################################################################################################     KZ


@bot.callback_query_handler(func=lambda callback: callback.data == 'Атырау облысы')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=6)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Шығыс Қазақстан облысы')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=16)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Қостанай облысы')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=10)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Маңғыстау облысы')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=12)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Қызылорда облысы')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=11)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Жамбыл облысы')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=8)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Қарағанды облысы')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=9)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Түркістан облысы')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=13)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Батыс Қазақстан облысы')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=7)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Ақмола облысы')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=3)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Ақтөбе облысы')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=4)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Павлодар облысы')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=14)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Солтүстік Қазақстан облысы')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=15)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Алматы облысы')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=5)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Нұр-Сұлтан')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=1)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Алматы қаласы')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=2)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Шымкент қаласы')
def send_region(callback):
    select_class(callback.message.chat.id, callback.message.message_id)
    sql.send_the_region(callback, region_id=19)


def send_class_info(callback, lang='ru'):
    global class_flag
    if class_flag == 0:
        password = password_gen()
        sql.access(callback.message.chat.id)
        if lang == 'kz':
            bot.send_message(callback.message.chat.id, text=f'Кілт сөз:')
        else:
            bot.send_message(callback.message.chat.id, text=f'Ваш пароль\n\nЕсли Вы забудете пароль, введите в поиске '
                                                            f'чата: "Ваш пароль" чтобы его найти')
        bot.send_message(callback.message.chat.id, text=f'{password.decode("utf-8")}')
        send_password(id=callback.message.chat.id, password=password)
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    if lang == 'kz':
        menu(callback.message.chat.id, txt='🎛 Басты бет ⬇️', lang=lang)
    else:
        menu(callback.message.chat.id, lang=lang)
    if callback.data == 'Преподаватель' or callback.data == 'Мұғалім':
        class_num = 0
    else:
        class_num = (str(callback.data)).split()[0]

    sql.update_class(class_num, callback)

    if class_num == 0:
        sql.update_teacher(callback)


def send_fio(id, fio):
    username = sql.get_iin(id)

    fio_parts = (str(fio).split())
    lastname = fio_parts[0]
    firstname = fio_parts[1]
    patronymic = None
    if len(fio_parts) == 3:
        patronymic = fio_parts[2]
    sql.send_fio(lastname, firstname, username, patronymic)


def send_iin(id, iin):
    global iin_flag
    if sql.update_iin(iin, id) == 1:
        sql.send_iin(iin)
    else:
        iin_flag = 1
        sql.update_id(id, iin)
        sql.delete_user(iin)
        bot.send_message(chat_id=id, text='Вы уже зарегистрированы, введите пароль')



def send_password(id, password):
    dec_pass = dec_password(password)
    username = sql.get_iin(id)
    sql.insert_purse(id)
    sql.send_password(dec_pass, username)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Профиль')
def profile(callback):
    id = callback.message.chat.id
    data = sql.profile(id)
    iin = data[0][0]
    class_var = data[0][1]

    cash = sql.get_cash_value(id)

    if class_var == 0:
        text = f'Логин: {iin}\nСтатус: Преподаватель\nБаланс: {cash} ₸'
    else:
        text = f'Логин: {iin}\nКласс: {class_var}\nБаланс: {cash} ₸'

    markup = InlineKeyboardMarkup()
    button_class = InlineKeyboardButton('🔄 Сменить класс', callback_data='Сменить класс')

    button_menu = InlineKeyboardButton(text=f'🎛 Главное меню', callback_data='ru')

    markup.add(button_class).add(button_menu)
    try:
        bot.delete_message(chat_id=id, message_id=callback.message.message_id)
    except ApiTelegramException:
        pass

    bot.send_message(chat_id=id, text=text, reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Профиль kz')
def profile(callback):
    id = callback.message.chat.id
    data = sql.profile(id)
    iin = data[0][0]
    class_var = data[0][1]

    cash = sql.get_cash_value(id)

    if class_var == 0:
        text = f'Логин: {iin}\nДәреже: Мұғалім\nБаланс: {cash} ₸'
    else:
        text = f'Логин: {iin}\nСынып: {class_var}\nБаланс: {cash} ₸'

    markup = InlineKeyboardMarkup()
    button_class = InlineKeyboardButton('🔄 Сынып ауыстыру', callback_data='Сменить класс kz')

    button_menu = InlineKeyboardButton(text=f'🎛 Басты бет', callback_data='kz')

    markup.add(button_class).add(button_menu)

    bot.delete_message(chat_id=id, message_id=callback.message.message_id)

    bot.send_message(chat_id=id, text=text, reply_markup=markup)


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
polls = []


def set_question_attemps(questions, questionusageid, chat_id, timeout):
    userid = sql.get_user_id(chat_id)
    j = 1
    attempts_id = []
    for question in questions:
        questiontext = sql.get_questiontext(question) # String
        answers = sql.get_answers(question)  # List of Tuple - id, answer, fraction
        answers_str = ''
        answers_ids = []
        correct_answer = 0
        random.shuffle(answers)
        html = HTML2Text()
        for i in range(len(answers)):
            if i == 0:
                answers_str += f'{html.handle(answers[i][1]).strip()}\n'
            else:
                answers_str += f';{html.handle(answers[i][1]).strip()}\n'
            if int(answers[i][2]) == 1:
                correct_answer = i
            answers_ids.append(answers[i][0])
        questionsummary = f'{questiontext.rstrip()}\n\n:{answers_str}'
        rightanswer = f'{html.handle(answers[correct_answer][1]).strip()}\n'
        questionattempid = sql.set_question_attempts(questionusageid, j, question, questionsummary, rightanswer)
        attempts_id.append(questionattempid)
        j += 1
        sql.set_attempts_step(questionattempid, userid, answers_ids)
        redis_cache.add_question(chat_id, question, answers_ids, correct_answer, timeout)
        global polls
        op = [1, 3, 5, 7]
        poll = Poll(questiontext, op, open_period=20, poll_type='quiz', correct_option_id=1)
        polls.append(poll)
    return attempts_id


def set_quiz_attempts(quiz, userid, uniqueid):
    timestart = int(time.time())
    tasks = quiz[1]
    layout = []
    for  i in range(tasks):
        layout.append(i + 1)
    layout.append(0)
    layout = str(tuple(layout)).replace(' ', '')
    quiz_attempt_id = sql.set_quiz_attempts(quiz, userid, uniqueid, layout, timestart)
    return quiz_attempt_id

########################################################################################################################
########################################################################################################################
@bot.poll_handler(func=lambda active_quiz: active_quiz.is_closed is False)
def write_answer(active_quiz: Poll):
    cache_value = redis_cache.get_poll_id(active_quiz.id).split(', ')
    chat_id = int(cache_value[0])
    msg_id = int(cache_value[1])
    bot.delete_message(chat_id=chat_id, message_id=msg_id - 1)
    bot.delete_message(chat_id=chat_id, message_id=msg_id)
    user_custom = User_custom(chat_id)
    callback = CallbackQuery(chat_id, user_custom, 'answ', chat_instance='0000')
    rewrite_results(chat_id, active_quiz)
    send_question(callback)


def rewrite_results(chat_id, active_quiz=None):
    quest_id = int(redis_cache.get_result(chat_id))
    usage_id = int(redis_cache.get_usage(chat_id))
    if active_quiz is not None:
        for i in range(len(active_quiz.options)):
            if active_quiz.options[i].voter_count != 0:
                sql.update_question_attempts(quest_id, usage_id, active_quiz.options[i].text)
                attempt_id = sql.select_id_question_attempts(quest_id, usage_id)
                attempt_step_id = sql.get_attempt_step(attempt_id)
                sql.update_question_attempt_step_data(i, attempt_step_id)
                if i != active_quiz.correct_option_id:
                    sql.update_question_attempt_step(attempt_id)
    else:
        sql.update_question_attempts(quest_id, usage_id, None)
        attempt_id = sql.select_id_question_attempts(quest_id, usage_id)
        sql.update_question_attempt_step(attempt_id)


@bot.callback_query_handler(func=lambda callback: callback.data == 'next')
def send_question(callback: CallbackQuery):
    chat_id = callback.from_user.id
    question_num = int(redis_cache.get_question_num(chat_id)) + 1
    redis_cache.write_question_num(chat_id, question_num)
    if type(callback.from_user) is not User_custom:
        try:
            if callback.data == 'next':
                rewrite_results(chat_id)
            bot.delete_message(chat_id, callback.message.message_id - 1)
            bot.delete_message(chat_id, callback.message.message_id)
        except ApiTelegramException:
            pass
    try:
        ques_id, question = redis_cache.get_question(chat_id)
    except TypeError:
        send_result(chat_id)
        return
    question_text = sql.get_questiontext(ques_id)
    redis_cache.write_result(chat_id, ques_id)
    key = list(question['answers'].keys())[0]
    correct_answer_id = question['answers'][key]
    open_period = int(question['timeout'])
    answers_ids = key[1:-1].split(', ')
    options = []
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text='Next', callback_data='next')
    markup.add(button)
    for answer_id in answers_ids:
        options.append(sql.get_answers_text(answer_id))
    # msg_photo = bot.send_photo(chat_id=callback.message.chat.id, photo=open('./ph.png', 'rb'))

    try:
        bot.send_message(chat_id, question_text)
    except ApiTelegramException:
        print(question_text)
    msg = bot.send_poll(chat_id=chat_id, question=f'Вопрос/Сұрақ/Question №{question_num}', open_period=open_period,
                        options=options, correct_option_id=correct_answer_id, type='quiz', reply_markup=markup)
    poll = msg.poll
    poll_id = poll.id
    redis_cache.add_poll_id(poll_id, chat_id, msg.message_id)


def level(overall):
    if 80 <= overall <= 100:
        return 1
    elif 57 <= overall <= 79.9:
        return 2
    elif 33 <= overall <= 56.9:
        return 3
    elif overall <= 32.9:
        return 4



def hash_code_cert(userid, course_id):
    rand_num = random.randint(100, 1000000)
    rand_num_1 = random.randint(100, 1000000)
    rand_num_2 = random.randint(100, 1000000)
    code = f'{userid}-{course_id}-telegram-{rand_num}-{rand_num_1}-{rand_num_2}'.encode()
    hash_code = hashlib.md5(code).hexdigest()
    hash = ''
    for _ in range(8):
        hash += random.choice(hash_code)
    return hash


def send_result(chat_id):
    m = bot.send_message(chat_id, 'Считаем результат...')
    result = 0
    usage_id = int(redis_cache.get_usage(chat_id, flag=0))
    question_attempts_id = sql.select_all_question_attempts(usage_id)
    for item in question_attempts_id:
        fraction = sql.select_grade_attempt_step(item[0])
        if int(fraction) == 1:
            result += 1
    overall = result / len(question_attempts_id)
    overall *= 100
    overall = float(format(overall, '.1f'))
    level_ = level(overall)
    course_id = redis_cache.get_course_id(chat_id)
    user_id = sql.get_user_id(chat_id)
    hash_code = hash_code_cert(user_id, course_id)
    while sql.select_code_customcert(hash_code) is not None:
        hash_code = hash_code_cert(user_id, course_id)
    name = None
    try:
        customcertid = sql.select_customcertid(course_id, level_)
        sql.insert_customcert(user_id, customcertid, hash_code)
        name = sql.get_customcert_one(customcertid)
    except TypeError as e:
        logger.error("course_id is not configured")
        logger.error(e)

    quiz_attempt_id = redis_cache.get_quiz_attempt_id(chat_id)
    sql.update_quiz_attempts(format(result, '.5f'), quiz_attempt_id)
    redis_cache.rediska.delete(chat_id)
    redis_cache.rediska.delete(f'{chat_id} - question_num')

    bot.delete_message(chat_id, m.message_id)
    bot.send_message(chat_id, text=f'Тест завершен\nВы набрали:\n{overall}% правильных ответов '
                                   f'({result}/{len(question_attempts_id)})\n'
                                   f'Можете перейти в начало:\n/start')
    if name is not None:
        fullname = sql.get_olymp_name(name[0][0])
        text = f'{fullname}'
        str_telegram = f'{user_id};{customcertid};telgrBilgen'.encode()
        telegram = hashlib.sha512(str_telegram).hexdigest()
        bot.send_document(chat_id=chat_id, data=f'https://bilgen.academy/mod/customcert/'
                                                                 f'my_certificates.php?'
                                                                 f'userid={user_id}'
                                                                 f'&certificateid={customcertid}'
                                                                 f'&downloadcert=1'
                                                                 f'&telegram={telegram}')
        bot.send_message(chat_id=chat_id, text=text)
        bot.send_message(chat_id=chat_id, text='Ваш сертификат ⬆️')



########################################################################################################################
########################################################################################################################
def check_enrolments(callback, c_id):
    u_id = sql.get_user_id(callback.message.chat.id)

    e_ids = sql.get_enrol_id(u_id)

    e_ids_list = []
    for e_id in e_ids:
        e_ids_list.append(e_id[0])
    e_ids_list = tuple(e_ids_list)
    if len(e_ids_list) < 2:
        if len(e_ids_list) == 0:
            return -1
        data = sql.select_course_id(e_ids_list[0])
    else:
        data = sql.select_course_ids(e_ids_list)

    global delete_flag
    i = 0
    for course_id in data:
        if course_id[0] == c_id:
            accept_for_clear_row(callback)
            time.sleep(10)
            if delete_flag == 1:
                quiz_id = sql.get_quiz(c_id)[0]
                customcerts = sql.select_customcertid_all(c_id)
                for item in customcerts:
                    cust_id = sql.select_customcertid_userid_to_delete(u_id, item[0])
                    if len(cust_id) > 0:
                        break
                try:
                    sql.delete_customcert(cust_id[0][0])
                except IndexError:
                    pass
                sql.delete_quiz_attempt(quiz_id, u_id)
                sql.delete_enrol_id(e_ids_list[i])
                delete_flag = 0
                return 1
            else: return 0
        i += 1
    if i == len(e_ids_list):
        return -1
    return 0

delete_flag = 0

def accept_for_clear_row(callback):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text='Продолжить', callback_data='delete_course')
    markup.add(button)
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    txt = 'Ваши результаты пройденной олимпиады по данному предмету обнулятся. Нажмите "Продолжить" если Вы согласны.\n\n' \
          'В противном случае, введите команду /start'

    bot.send_message(chat_id=callback.message.chat.id, text=txt, reply_markup=markup)


fuckin_dictionary = {
    1850: 2504,
    1825: 2493,
    1800: 2494,
    1822: 2495,
    1823: 2496,
    1824: 2497,
    1843: 2498,
    1845: 2500,
    1829: 2500,
    1844: 2501,
    1826: 2502,
    1827: 2468,
    1838: 2469,
    1839: 2470,
    1840: 2473,
    1846: 2471,
    1847: 2524,
    1848: 2525,
    1793: 2526,
    1853: 2499,
    1854: 2527,
    1855: 2528,
    1858: 2529,
    1864: 2530,
    1856: 2505,
    1857: 2506,
    1861: 2509,
    1860: 2508,
    1859: 2507,
    1862: 2510,
    1863: 2511,
    1865: 2503,
    1866: 2468,
    1867: 2472,
    1784: 43825,
}

doda_time = [
    2521,
    2520,
    2519,
    2518,
    2517,
    2516,
    2515,
    2514,
]


ustaz = [
    2566,
    2565,
    2564,
    2563,
    2562,
    2561,
    2560,
    2559,
    2558,
    2557,
    2556,
    2555,
    2554,
    2553,
    2552,
    2551
]


@bot.callback_query_handler(func=lambda callback: callback.data == 'delete_course')
def delete_course(callback):
    global delete_flag
    delete_flag = 1
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    m = bot.send_message(callback.message.chat.id, text="Идет обработка запроса...")
    time.sleep(5)
    bot.delete_message(callback.message.chat.id, m.message_id)


def check_quiz_attempt(quiz, uid):
    res = sql.check_quiz_aatem(uid, quiz)
    if res is None:
        return 1
    return 0


def start_test(callback, cost, course_id):
    cash = sql.get_cash_value(callback.message.chat.id)
    uid = sql.get_user_id(callback.message.chat.id)
    quiz = sql.get_quiz(course_id)
    if int(cash) >= cost:
        if check_enrolments(callback, course_id) == 0:
            menu(callback.message.chat.id)
            return
        try:
            bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        except ApiTelegramException:
            pass
        enrol_id = sql.get_enrol(course_id)
        sql.set_user_enrolments(callback.message.chat.id, enrol_id)
        if check_quiz_attempt(quiz[0], uid) == 0:
            if check_enrolments(callback, course_id) == 0:
                menu(callback.message.chat.id)
                return
        instance_id = sql.get_instance(course_id)
        flag = 0
        try:
            category_id = fuckin_dictionary[course_id]
            context_id = 49
            flag = 1
        except KeyError:
            context_id = sql.get_context(instance_id)
        if course_id == 1827:
            flag = 2
        elif course_id == 1779:
            flag = 3
        if quiz[0] in doda_time:
            timeout = 240
        elif quiz[0] in ustaz:
            timeout = 180
        else:
            timeout = quiz[2] // quiz[1]
        unique_id = sql.set_question_usages(context_id)
        redis_cache.write_usage(callback.message.chat.id, unique_id)
        quiz_attemp_id = set_quiz_attempts(quiz, uid,unique_id)
        if quiz_attemp_id is None:
            quiz_attemp_id = set_quiz_attempts(quiz, uid,unique_id)
        redis_cache.write_quiz_attempts(callback.message.chat.id, quiz_attemp_id)
        if flag == 0:
            context_for_category = sql.get_context_category(course_id)
            category_id = sql.get_category(context_for_category)
            questions = sql.get_questions(category_id)
        elif flag == 2:
            questions = [52100, 52112, 52125, 52127, 52128, 52129, 52130, 59029, 59030, 59033, 59035, 59038, 59039,
                         59040, 59042, 59052, 59060, 59061, 59048, 59077, 59078, 59087, 59094, 59095, 61557, 61568,
                         61582, 62143, 62144, 62167]
        elif flag == 3:
            questions = [625096, 625108, 625114, 625109, 625116, 625105, 626469, 625106, 625100, 625112, 625115, 626466,
                         625124, 625117, 626467, 625118, 625107, 626465, 625123, 626470, 625113, 625120, 625099, 625094,
                         625119, 625098, 625097, 625111, 625110, 625122]
        else:
            questions = sql.get_fucking_questions(category_id)
        attempts_id = set_question_attemps(questions, unique_id, callback.message.chat.id, timeout)
        redis_cache.write_course_id(callback.message.chat.id, course_id)

        m = bot.send_message(callback.message.chat.id, '3')
        time.sleep(1)
        bot.delete_message(callback.message.chat.id, m.message_id)
        m = bot.send_message(callback.message.chat.id, '2')
        time.sleep(1)
        bot.delete_message(callback.message.chat.id, m.message_id)
        m = bot.send_message(callback.message.chat.id, '1')
        time.sleep(1)
        bot.delete_message(callback.message.chat.id, m.message_id)
        redis_cache.write_question_num(callback.message.chat.id, 0)
        sql.sub_cash(callback.message.chat.id, cost)
        send_question(callback)
    else:
        bot.send_message(chat_id=callback.message.chat.id, text='Не хватает средств для оплаты курса')



@bot.callback_query_handler(func=lambda callback: callback.data == 'M')
def update_genre(callback):
    sql.update_genre_(callback)
    select_region(id=callback.message.chat.id, message_id=callback.message.message_id)


@bot.callback_query_handler(func=lambda callback: callback.data == 'W')
def update_genre(callback):
    sql.update_genre_(callback, 0)
    select_region(id=callback.message.chat.id, message_id=callback.message.message_id)


def select_genre(id):
    markup = InlineKeyboardMarkup()

    button_m = InlineKeyboardButton('M', callback_data='M')
    button_w = InlineKeyboardButton('Ж', callback_data='W')

    markup.add(button_m, button_w)

    bot.send_message(chat_id=id, text="Жынысы\n\nПол", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: 'cert_' in callback.data)
def send_certs(callback):
    u_id = sql.get_user_id(callback.message.chat.id)
    course_fullname = redis_cache.get_course_name(callback.data)
    course_id = int(callback.data[5:])
    certs = sql.select_customcertid_all(course_id)
    cust_ids_list = []
    for item in certs:
        cust_id = sql.select_customcertid_userid_to_delete(u_id, item[0])
        if len(cust_id) > 0:
            cust_ids_list.append(item[0])
    cust_ids_list = tuple(cust_ids_list)
    if len(cust_ids_list) < 2:
        if len(cust_ids_list) == 0:
            return -1
        data_cert = sql.get_customcert_one(cust_ids_list[0])
    else:
        data_cert = sql.get_customcert_list(cust_ids_list)

    for name in data_cert:
        text = f'{course_fullname}\n{name[1]}'
        str_telegram = f'{u_id};{name[2]};telgrBilgen'.encode()
        telegram = hashlib.sha512(str_telegram).hexdigest()
        bot.send_document(chat_id=callback.message.chat.id, data=f'https://bilgen.academy/mod/customcert/'
                                                                 f'my_certificates.php?'
                                                                 f'userid={u_id}'
                                                                 f'&certificateid={name[2]}'
                                                                 f'&downloadcert=1'
                                                                 f'&telegram={telegram}')
        bot.send_message(chat_id=callback.message.chat.id, text=text)


def get_certificate(callback: CallbackQuery, txt1, txt2, txt3):
    u_id = sql.get_user_id(callback.message.chat.id)
    data = sql.get_certificate(u_id, 1609437600)

    cust_ids_list = []
    for cust_id in data:
        cust_ids_list.append(cust_id[0])

    cust_ids_list = tuple(cust_ids_list)
    if len(cust_ids_list) < 2:
        if len(cust_ids_list) == 0:
            bot.answer_callback_query(callback.id, text=txt3, show_alert=True)
            return -1
        data_cert = sql.get_customcert_one(cust_ids_list[0])
    else:
        data_cert = sql.get_customcert_list(cust_ids_list)

    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    msg = bot.send_message(callback.message.chat.id, txt1)
    course_ids = set()
    for course in data_cert:
        course_ids.add(course[0])
    markup = InlineKeyboardMarkup()
    i = 0
    for course in course_ids:
        fullname = sql.get_olymp_name(course)
        redis_cache.write_course_name(course, fullname)
        markup.add(InlineKeyboardButton(fullname, callback_data=f'cert_{course}'))

    bot.delete_message(callback.message.chat.id, msg.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=txt2, reply_markup=markup)



@bot.callback_query_handler(func=lambda callback: callback.data=='Сертификаты')
def get_certificate_ru(callback):
    get_certificate(callback, 'Список загружается...', 'Выберите', 'У Вас еще нет сертификатов')


@bot.callback_query_handler(func=lambda callback: callback.data == 'Сертификаты kz')
def get_certificate_kz(callback):
    get_certificate(callback, 'Тізім жүктелуде...', 'Таңдаңыз', 'Сізде қолжетімді сертификат жоқ')


class User_custom(object):
    def __init__(self, id):
        self.id = id


@bot.callback_query_handler(func=lambda callback: callback.data == 'ru')
def intro_ru(callback: CallbackQuery):
    uid = callback.message.chat.id
    u_info = sql.check_user(uid=uid)

    user_now[uid] = callback.data

    bot.delete_message(uid, callback.message.message_id)
    if u_info != -1 and u_info[2] == 1:
        profile_buttons(u_info=u_info, id=uid)
    else:
        sign_up_in_ru(id=uid)


@bot.callback_query_handler(func=lambda callback: callback.data == 'kz')
def intro_kz(callback: CallbackQuery):
    uid = callback.message.chat.id
    u_info = sql.check_user(uid=uid)

    user_now[uid] = callback.data

    bot.delete_message(uid, callback.message.message_id)

    if u_info != -1 and u_info[2] == 1:
        profile_buttons(u_info=u_info, id=uid, lang='kz')
    else:
        sign_up_in_kz(id=uid)


def menu(id, txt='🎛 На главную ⬇️', lang='ru'):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    if lang == 'ru':
        button_menu = KeyboardButton('Меню')
    else:
        button_menu = KeyboardButton('Мeню')
    markup.add(button_menu)
    bot.send_message(chat_id=id, text=txt, reply_markup=markup)


def profile_buttons(u_info, id, lang='ru'):
    markups = InlineKeyboardMarkup()
    if lang == 'kz':
        button_courses = InlineKeyboardButton('🎓 Курстар', callback_data=f'Курс {u_info[0]}kz')
        button_olympiads = InlineKeyboardButton('📚 Олимпиадалар', callback_data=f'Олимпиады {u_info[0]}kz')
        button_balance = InlineKeyboardButton('💲 Төлем жүйесі', callback_data='Пополнение kz')
        button_achievements = InlineKeyboardButton('🏆 Нәтижелерім', callback_data='Сертификаты kz')
        button_profile = InlineKeyboardButton('🧑🏻‍💻 Жеке кабинет', callback_data=f'Профиль kz')
    else:
        button_courses = InlineKeyboardButton('🎓 Курсы', callback_data=f'Курс {u_info[0]}')
        button_olympiads = InlineKeyboardButton('📚 Олимпиады', callback_data=f'Олимпиады {u_info[0]}')
        button_balance = InlineKeyboardButton('💲 Способ оплаты', url='https://bilgen.academy/api/gateway/')
        button_achievements = InlineKeyboardButton('🏆 Мои сертификаты', callback_data='Сертификаты')
        button_profile = InlineKeyboardButton('🧑🏻‍💻 Профиль', callback_data=f'Профиль')

    if int(u_info[0]) == 0:
        markups.add(button_courses, button_olympiads)
    else:
        markups.add(button_olympiads)

    markups.add(button_achievements, button_profile)
    markups.add(button_balance)
    if lang == 'kz':
        bot.send_message(chat_id=id, text='🎛 Басты бет', reply_markup=markups)
    else:
        bot.send_message(chat_id=id, text='🎛 Главное меню', reply_markup=markups)


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    markup = InlineKeyboardMarkup()
    uid = message.chat.id
    if message.message_id > 1:
        try:
            bot.delete_message(uid, message.message_id - 1)
        except ApiTelegramException:
            pass
    bot.delete_message(uid, message.message_id)
    print(uid, '<<<<<<<<<<<<  Новое сообщение!!!!!')
    button_ru = InlineKeyboardButton('🇷🇺 Русский', callback_data='ru')
    button_kz = InlineKeyboardButton('🇰🇿 Қазақша', callback_data='kz')
    markup.add(button_kz).add(button_ru)
    bot.send_message(chat_id=message.chat.id, text=say_hello, reply_markup=markup)


@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        global iin_flag
        iin_flag = 0
        iin(message.chat.id)
        sql.send_number(chat_id=message.chat.id, number=message.contact.phone_number)


@bot.message_handler(func=lambda message: True)
def buttons_tree(message: Message):

    global iin_flag
    global name_flag
    id_ = message.chat.id
    # buttons = {
    #     '🇰🇿 Қазақша': status_kz(id=id_),
    #     '🇷🇺 Русский': status_ru(id=id_),
    #     #######################################################################################
    #     'Мұғалім': info_1(id=id_),
    #     'Оқушы': student_kz(id=id_),
    #     #######################################################################################
    #     'Курстар': info_2(id=id_),
    #     'Олимпиадалар': info_3(id=id_),
    #     #######################################################################################
    #     'Преподаватель': info_4(id=id_),
    #     'Ученик': student_ru(id=id_),
    #     #######################################################################################
    #     'Курсы': info_5(id=id_),
    #     'Олимпиады': info_6(id=id_),
    #     #######################################################################################
    #     'Tanymger Expert': send_info(id=id_, text=choose_kz, lng='kz'),
    #     'Bilgen Tech': send_info(id=id_, text=choose_kz, lng='kz'),
    #     'Oysana': send_info(id=id_, text=choose_kz, lng='kz'),
    #     'Тоғызқұмалақ': send_info(id=id_, text=choose_kz, lng='kz'),
    #     'Білікті педагог': send_info(id=id_, text=choose_kz, lng='kz'),
    #     #######################################################################################
    #     'Tanymger  Expert': send_info(id=id_, text=choose_ru, lng='ru'),
    #     'Bilgen  Tech': send_info(id=id_, text=choose_ru, lng='ru'),
    #     'Оуsana': send_info(id=id_, text=choose_ru, lng='ru'),
    #     'Toғызқұмалақ': send_info(id=id_, text=choose_ru, lng='ru'),
    #     'Квалифицированный педагог': send_info(id=id_, text=choose_ru, lng='ru'),
    #     #######################################################################################
    #     'Bilgen UBT': send_info(id=id_, text=choose_kz, lng='kz'),
    #     # 'Bilgen Tech': send_info(id=id_, text=choose_kz, lng='kz'),  # TODO: Fix this shit
    #     #######################################################################################
    #     'Bilgen Baige/Alaman': send_info(id=id_, text=choose_kz, lng='kz'),
    #     'Bala/Bilik Time': send_info(id=id_, text=choose_kz, lng='kz'),
    #     #######################################################################################
    #     'Bilgen  UBT': send_info(id=id_, text=choose_ru, lng='ru'),
    #     # 'Bilgen  Tech': send_info(id=id_, text=choose_ru, lng='ru'),  # TODO: Fix this shit
    #     #######################################################################################
    #     'Bilgen  Baige/Alaman': send_info(id=id_, text=choose_ru, lng='ru'),
    #     'Bala/Bilik  Time': send_info(id=id_, text=choose_ru, lng='ru'),
    # }
    # buttons['🇷🇺 Русский'] = status_ru, id_
    # buttons['Bala/Bilik  Time'] = send_info, id_, choose_ru, 'ru'
    # button = buttons.get(message.text)
    # try:
    #     decorator(button[0], button[1], button[2], button[3])
    # except IndexError:
    #     decorator(button[0], button[1])

    # print(message)
    ###############################################

    ###############################################
    ###############################################
    if message.text == 'Меню': ######################### RU
        u_info = sql.check_user(id_)
        bot.delete_message(id_, message.message_id - 1)
        bot.delete_message(id_, message.message_id)
        profile_buttons(u_info, id_)

    elif message.text == 'Мeню': ######################### KZ
        u_info = sql.check_user(id_)
        bot.delete_message(id_, message.message_id - 1)
        bot.delete_message(id_, message.message_id)
        profile_buttons(u_info, id_, 'kz')

    elif message.text == 'Регистрация' or message.text == 'Тіркеу':
        iin_flag = 0
        sign_up_ru(id=id_)
    elif message.text == 'Кілт сөзді ұмыттыңыз ба?' or message.text == 'Восстановить пароль':
        pass_forget(message)
    elif message.text == 'Кіру' or message.text == 'Авторизация':
        iin_flag = 1
        iin(id=id_)
    elif re.fullmatch(pattern=iin_pattern, string=message.text):
        if iin_flag == 1:
            sign_in_ru(id=id_)
            sql.update_id(chat_id=id_, iin=message.text)
        else:
            fio(id=id_)
            send_iin(id=id_, iin=message.text)
    elif re.fullmatch(pattern=fio_pattern, string=message.text):
        send_fio(id=id_, fio=message.text)
        select_genre(id_)
    elif re.fullmatch(pattern=phone_number_pattern, string=message.text):
        iin(message.chat.id)
        sql.send_number(chat_id=id_, number=message.text)
    elif re.fullmatch(pattern=r'.+', string=message.text):
        if iin_flag == 1:
            response_text = check_password(id=id_, password=message.text) # [data] => error
            error_mes = '[data] => error'
            if response_text is None:
                return
            if kmp(response_text, error_mes) != -1:
                bot.send_message(chat_id=id_, text='Дұрыс емес кілт сөз\n\nНеправильный пароль\n\n/start')
            else:
                sql.access(id_)
                bot.send_message(chat_id=id_, text='Қош келдіңіз!\n\nДобро пожаловать!')
                try:
                    _lang = user_now[id_]
                except KeyError:
                    _lang = 'ru'
                menu(id_, txt='🎛 Басты бет\n🎛 На главную ⬇️', lang=_lang)
        else:
            bot.send_message(chat_id=id_, text='Invalid')
    else:
        bot.send_message(chat_id=id_, text=mistake)


if __name__ == '__main__':
    main()

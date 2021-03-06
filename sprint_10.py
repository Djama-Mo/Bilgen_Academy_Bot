from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
from sprint_11 import olymp_text_kz, olymp_text_ru


sprint_ru = 'Bilgen  Sprint'
sprint_kz = 'Bilgen Sprint'

start_the_test_ru = 'Оплатить и приступить к тесту'
start_the_test_kz = 'Төлеу және тестті бастау'


def sprint_subject_10_ru(callback, bot, subj):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data=f'spr_{subj}_10_ru')
    button_back = InlineKeyboardButton(text='К списку олимпиад', callback_data=f'Олимпиады 10')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('2'), reply_markup=markup, parse_mode='html')


def sprint_subject_10_kz(callback, bot, subj):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data=f'spr_{subj}_10_kz')
    button_back = InlineKeyboardButton(text='Олимпиадалар тізімі', callback_data=f'Олимпиады 10kz')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('2'), reply_markup=markup, parse_mode='html')

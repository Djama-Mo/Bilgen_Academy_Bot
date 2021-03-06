from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
from sprint_11 import olymp_text_kz, olymp_text_ru


start_the_test_ru = 'Оплатить и приступить к тесту'
start_the_test_kz = 'Төлеу және тестті бастау'


def doda_subject_ru(callback, bot, class_, subj):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data=f'doda_{subj}_{class_}_ru')
    button_back = InlineKeyboardButton(text='К списку олимпиад', callback_data=f'Олимпиады {class_}')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('4'), reply_markup=markup, parse_mode='html')


def doda_subject_kz(callback, bot, class_, subj):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data=f'doda_{subj}_{class_}_kz')
    button_back = InlineKeyboardButton(text='Олимпиадалар тізімі', callback_data=f'Олимпиады {class_}kz')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('4'), reply_markup=markup, parse_mode='html')

from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton

from subjects_11 import text, text_kz

sprint_ru = 'Bilgen  Sprint'
sprint_kz = 'Bilgen Sprint'

bala_time_ru = 'Bala/Bilik  Time'
bilik_ru = 'Bala/Bilik Time – Республиканские онлайн-олимпиады для учеников 1-11 классов.'
bilgen_sprint_txt_ru = 'Bilgen Sprint - Республиканская дистанционная предметная олимпиада'

bala_time_kz = 'Bala/Bilik Time'
bilgen_sprint_txt_kz = 'Bilgen Sprint - Республикалық қашықтықтан өткізілетін пәндік олимпиада'
bilik_kz = 'Bala/Bilik Time – Бастауыш пен жоғарғы сыныптар арасында республикалық көлемде өтетін онлайн олимпиадалар.'

doda_dir_lan_kz = 'Тіл білімі'
doda_dir_log_kz = 'Логика'

doda_dir_lan_ru = 'Лингвистика'
doda_dir_log_ru = 'Логикa' # 'a' - eng

doda_ru = 'Doda'
doda_kz = 'Dodа'

doda_inf_kz = 'Doda - Бастауыш сынып оқушыларына арналған Республикалық "Doda" шығармашылық байқауы'
doda_inf_ru = 'Doda - Республиканский дистанционный творческий конкурс для учащихся начальных классов'


def reply_list_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text=f'{sprint_ru}', callback_data=f'{sprint_ru} 4')
    button_2 = InlineKeyboardButton(text=f'{bala_time_ru}', callback_data=f'{bala_time_ru} 4')
    button_3 = InlineKeyboardButton(text=f'{doda_ru}', callback_data=f'{doda_ru} 4')

    button_menu = InlineKeyboardButton(text=f'Главное меню', callback_data='ru')

    markup_url.add(button_1).add(button_3).add(button_menu)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text='Выберите', reply_markup=markup_url)


def reply_sprint_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Список предметов', callback_data=f'Список {sprint_ru} 4')
    button_2 = InlineKeyboardButton(text='Положение', callback_data=f'Положение {sprint_ru}')

    button_menu = InlineKeyboardButton(text=f'Главное меню', callback_data='ru')

    markup_url.add(button_1, button_2).add(button_menu)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=bilgen_sprint_txt_ru, reply_markup=markup_url)


def reply_sprint_list_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Математика', callback_data=f'Мат {sprint_ru} 4')
    button_2 = InlineKeyboardButton(text='Казахский язык', callback_data=f'Каз {sprint_ru} 4')
    button_3 = InlineKeyboardButton(text='Казахская литература', callback_data=f'Казл {sprint_ru} 4')

    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Олимпиады 4')

    markup_url.add(button_1).add(button_2).add(button_3).add(button_back)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text='\n\nСписок предметов\n\n', reply_markup=markup_url)


def reply_bilik_time_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Информация', callback_data=f'Нап {bala_time_ru} 4')
    button_2 = InlineKeyboardButton(text='Положение', callback_data=f'Положение {bala_time_ru}')

    button_menu = InlineKeyboardButton(text=f'Главное меню', callback_data='ru')

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    markup_url.add(button_1, button_2).add(button_menu)
    bot.send_message(chat_id=callback.message.chat.id, text=bilik_ru, reply_markup=markup_url)


def reply_doda_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Направления', callback_data=f'Нап {doda_ru} 4')
    button_2 = InlineKeyboardButton(text='Положение', callback_data=f'Положение {doda_ru}')
    button_menu = InlineKeyboardButton(text=f'Главное меню', callback_data='ru')

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    markup_url.add(button_1, button_2).add(button_menu)
    bot.send_message(chat_id=callback.message.chat.id, text=doda_inf_ru, reply_markup=markup_url)

####################################################################################################      KZ
def reply_list_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text=f'{sprint_kz}', callback_data=f'{sprint_kz} 4')
    button_2 = InlineKeyboardButton(text=f'{bala_time_kz}', callback_data=f'{bala_time_kz} 4')
    button_3 = InlineKeyboardButton(text=f'{doda_kz}', callback_data=f'{doda_kz} 1')

    button_menu = InlineKeyboardButton(text=f'Басты бет', callback_data='kz')

    markup_url.add(button_1).add(button_3).add(button_menu)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text='Таңдаңыз', reply_markup=markup_url)


def reply_sprint_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Пәндер тізімі', callback_data=f'Список {sprint_kz} 4')
    button_2 = InlineKeyboardButton(text='Ереже', callback_data=f'Положение {sprint_kz}')

    button_menu = InlineKeyboardButton(text=f'Басты бет', callback_data='kz')

    markup_url.add(button_1, button_2).add(button_menu)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=bilgen_sprint_txt_kz, reply_markup=markup_url)


def reply_sprint_list_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Математика', callback_data=f'Мат {sprint_kz} 4')
    button_2 = InlineKeyboardButton(text='Қазақ тілі', callback_data=f'Каз {sprint_kz} 4')
    button_3 = InlineKeyboardButton(text='Қазақ әдебиеті', callback_data=f'Казл {sprint_kz} 4')

    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Олимпиады 4kz')

    markup_url.add(button_1).add(button_2).add(button_3).add(button_back)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text='\n\nСписок предметов\n\n', reply_markup=markup_url)


def reply_bilik_time_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Пәндер тізімі', callback_data=f'Нап {bala_time_kz} 4')
    button_2 = InlineKeyboardButton(text='Ақпарат', callback_data=f'Положение {bala_time_kz}')

    button_menu = InlineKeyboardButton(text=f'Басты бет', callback_data='kz')

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    markup_url.add(button_1, button_2).add(button_menu)
    bot.send_message(chat_id=callback.message.chat.id, text=bilik_kz, reply_markup=markup_url)


def reply_doda_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Бағыттары', callback_data=f'Нап {doda_kz} 4')
    button_2 = InlineKeyboardButton(text='Ереже', callback_data=f'Положение {doda_kz}')
    button_menu = InlineKeyboardButton(text=f'Басты бет', callback_data='kz')

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    markup_url.add(button_1, button_2).add(button_menu)
    bot.send_message(chat_id=callback.message.chat.id, text=doda_inf_kz, reply_markup=markup_url)
#############################################################################################################

def mat(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}mat 4')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 4')

    markup_url.add(button).add(button_back)
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("Математика", 4, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def kaz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}kaz 4')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 4')

    markup_url.add(button).add(button_back)
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("Казахский язык", 4, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def kazl(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}kazl 4')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 4')

    markup_url.add(button).add(button_back)
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("Казахская литература", 4, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def reply_bilik_time_list_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Учавствовать', callback_data=f'{bala_time_ru}4')
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Олимпиады 4')

    markup_url.add(button_1).add(button_back)
    bot.send_message(chat_id=callback.message.chat.id, text=text(bala_time_ru, 4, 40, 60, 1000),
                     reply_markup=markup_url, parse_mode='html')


def reply_doda_dir_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text=f'{doda_dir_lan_ru}', callback_data=f'{doda_dir_lan_ru}4')
    button_2 = InlineKeyboardButton(text=f'{doda_dir_log_ru}', callback_data=f'{doda_dir_log_ru}4')
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Олимпиады 4')
    markup_url.add(button_1).add(button_back)
    bot.send_message(chat_id=callback.message.chat.id, text='Направления',
                     reply_markup=markup_url, parse_mode='html')


def lan_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text=f'Учавствовать', callback_data=f'ling_4_ru')
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Нап {doda_ru} 4')

    markup_url.add(button_1).add(button_back)
    bot.send_message(chat_id=callback.message.chat.id, text=text(f'{doda_ru} ({doda_dir_lan_ru})', 4, 15, 60, 1500),
                     reply_markup=markup_url, parse_mode='html')


def log_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text=f'Учавствовать', callback_data=f'log_4_ru')
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Нап {doda_ru} 4')

    markup_url.add(button_1).add(button_back)
    bot.send_message(chat_id=callback.message.chat.id, text=text(f'{doda_ru} ({doda_dir_log_ru})', 4, 15, 60, 1500),
                     reply_markup=markup_url, parse_mode='html')


##########################################################################################################      KZ
def mat_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}mat 4')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 4')

    markup_url.add(button).add(button_back)
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Математика", 4, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def kaz_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}kaz 4')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 4')

    markup_url.add(button).add(button_back)
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Қазақ тілі", 4, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def kazl_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}kazl 4')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 4')

    markup_url.add(button).add(button_back)
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Қазақ әдебиеті", 4, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def reply_bilik_time_list_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Қатысу', callback_data=f'{bala_time_kz}4')
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Олимпиады 4kz')

    markup_url.add(button_1).add(button_back)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz(bala_time_kz, 4, 40, 60, 1000),
                     reply_markup=markup_url, parse_mode='html')


def reply_doda_dir_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text=f'{doda_dir_lan_kz}', callback_data=f'{doda_dir_lan_kz}4')
    button_2 = InlineKeyboardButton(text=f'{doda_dir_log_kz}', callback_data=f'{doda_dir_log_kz}4')
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Олимпиады 4kz')
    markup_url.add(button_1).add(button_back)
    bot.send_message(chat_id=callback.message.chat.id, text='Бағыттары',
                     reply_markup=markup_url, parse_mode='html')


def lan_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text=f'Қатысу', callback_data=f'ling_4_kz')
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Нап {doda_kz} 4')

    markup_url.add(button_1).add(button_back)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz(f'{doda_kz} ({doda_dir_lan_kz})', 4, 15, 60, 1500),
                     reply_markup=markup_url, parse_mode='html')


def log_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text=f'Қатысу', callback_data=f'log_4_kz')
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Нап {doda_kz} 4')

    markup_url.add(button_1).add(button_back)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz(f'{doda_kz} ({doda_dir_log_kz})', 4, 15, 60, 1500),
                     reply_markup=markup_url, parse_mode='html')

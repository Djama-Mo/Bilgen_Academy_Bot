from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from subjects_11 import text, text_kz

sprint_ru = 'Bilgen  Sprint'

sprint_kz = 'Bilgen Sprint'
mat_kz = 'Жаратылыстану-математикалық'
gum_kz = 'Қоғамдық-гуманитарлық'

mat = 'Естественно-математическое'
gum = 'Общественно-гуманитарное'

bala_time_ru = 'Bala/Bilik  Time'
bilik_ru = 'Bala/Bilik Time – Республиканские онлайн-олимпиады для учеников 1-11 классов.'
bilgen_sprint_txt_ru = 'Bilgen Sprint - Республиканская дистанционная предметная олимпиада'

bala_time_kz = 'Bala/Bilik Time'
bilgen_sprint_txt_kz = 'Bilgen Sprint - Республикалық қашықтықтан өткізілетін пәндік олимпиада'
bilik_kz = 'Bala/Bilik Time – Бастауыш пен жоғарғы сыныптар арасында республикалық көлемде өтетін онлайн олимпиадалар.'


def reply_list_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text=f'{sprint_ru}', callback_data=f'{sprint_ru} 5')
    button_2 = InlineKeyboardButton(text=f'{bala_time_ru}', callback_data=f'{bala_time_ru} 5')

    button_menu = InlineKeyboardButton(text=f'Главное меню', callback_data='ru')

    markup_url.add(button_1).add(button_menu)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text='Выберите', reply_markup=markup_url)


def reply_sprint_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Список предметов', callback_data=f'Список {sprint_ru} 5')
    button_2 = InlineKeyboardButton(text='Положение', callback_data=f'Положение {sprint_ru}')

    button_menu = InlineKeyboardButton(text=f'Главное меню', callback_data='ru')

    markup_url.add(button_1, button_2).add(button_menu)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=bilgen_sprint_txt_ru, reply_markup=markup_url)


def reply_sprint_list_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Информатика', callback_data=f'Информатика {sprint_ru}5')
    button_2 = InlineKeyboardButton(text='Математика', callback_data=f'Мат {sprint_ru} 5')
    button_3 = InlineKeyboardButton(text='Казахский язык', callback_data=f'Каз {sprint_ru} 5')
    button_4 = InlineKeyboardButton(text='Казахская литература', callback_data=f'Казл {sprint_ru} 5')
    button_6 = InlineKeyboardButton(text='Естествознание', callback_data=f'Ест {sprint_ru} 5')
    button_7 = InlineKeyboardButton(text='История Казахстана', callback_data=f'Иск {sprint_ru} 5')
    button_8 = InlineKeyboardButton(text='История Мира', callback_data=f'Мира {sprint_ru} 5')
    button_9 = InlineKeyboardButton(text='География', callback_data=f'Гео {sprint_ru} 5')
    button_10 = InlineKeyboardButton(text='Английский язык', callback_data=f'Анг {sprint_ru} 5')

    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Олимпиады 5')

    markup_url.add(button_2, button_3).add(button_4).add(button_7).add(button_8, button_6).add(button_10).add(button_back)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text='\n\nСписок предметов\n\n', reply_markup=markup_url)


def reply_bilik_time_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Направления', callback_data=f'Нап {bala_time_ru} 5')
    button_2 = InlineKeyboardButton(text='Положение', callback_data=f'Положение {bala_time_ru}')
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    button_menu = InlineKeyboardButton(text=f'Главное меню', callback_data='ru')

    markup_url.add(button_1, button_2).add(button_menu)
    bot.send_message(chat_id=callback.message.chat.id, text=bilik_ru, reply_markup=markup_url)


def reply_bilik_time_list_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text=mat, callback_data=f'{mat} 5')
    button_2 = InlineKeyboardButton(text=gum, callback_data=f'{gum} 5')
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Олимпиады 5')

    markup_url.add(button_1).add(button_2).add(button_back)
    bot.send_message(chat_id=callback.message.chat.id, text='Выберите направление', reply_markup=markup_url)

######################################################################################               KZ
def reply_list_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text=f'{sprint_kz}', callback_data=f'{sprint_kz} 5')
    button_2 = InlineKeyboardButton(text=f'{bala_time_kz}', callback_data=f'{bala_time_kz} 5')

    button_menu = InlineKeyboardButton(text=f'Басты бет', callback_data='kz')

    markup_url.add(button_1).add(button_menu)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text='Таңдаңыз', reply_markup=markup_url)


def reply_sprint_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Пәндер тізімі', callback_data=f'Список {sprint_kz} 5')
    button_2 = InlineKeyboardButton(text='Ереже', callback_data=f'Положение {sprint_kz}')

    button_menu = InlineKeyboardButton(text=f'Басты бет', callback_data='kz')

    markup_url.add(button_1, button_2).add(button_menu)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=bilgen_sprint_txt_kz, reply_markup=markup_url)


def reply_sprint_list_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Информатика', callback_data=f'Информатика {sprint_kz}5')
    button_2 = InlineKeyboardButton(text='Математика', callback_data=f'Мат {sprint_kz} 5')
    button_3 = InlineKeyboardButton(text='Қазақ тілі', callback_data=f'Каз {sprint_kz} 5')
    button_4 = InlineKeyboardButton(text='Қазақ әдебиеті', callback_data=f'Казл {sprint_kz} 5')
    button_6 = InlineKeyboardButton(text='Жаратылыстану', callback_data=f'Ест {sprint_kz} 5')
    button_7 = InlineKeyboardButton(text='Қазақстан тарихы', callback_data=f'Иск {sprint_kz} 5')
    button_8 = InlineKeyboardButton(text='Әлем тарихы', callback_data=f'Мира {sprint_kz} 5')
    button_9 = InlineKeyboardButton(text='География', callback_data=f'Гео {sprint_kz} 5')
    button_10 = InlineKeyboardButton(text='Ағылшын тілі', callback_data=f'Анг {sprint_kz} 5')

    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Олимпиады 5kz')

    markup_url.add(button_2, button_3).add(button_4).add(button_7).add(button_8, button_6).add(button_10).add(button_back)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text='\n\nПәндер тізімі\n\n', reply_markup=markup_url)


def reply_bilik_time_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Бағыттары', callback_data=f'Нап {bala_time_kz} 5')
    button_2 = InlineKeyboardButton(text='Ереже', callback_data=f'Положение {bala_time_kz}')

    button_menu = InlineKeyboardButton(text=f'Басты бет', callback_data='kz')

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    markup_url.add(button_1, button_2).add(button_menu)
    bot.send_message(chat_id=callback.message.chat.id, text=bilik_kz, reply_markup=markup_url)


def reply_bilik_time_list_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text=mat_kz, callback_data=f'{mat_kz} 5')
    button_2 = InlineKeyboardButton(text=gum_kz, callback_data=f'{gum_kz} 5')
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Олимпиады 5kz')

    markup_url.add(button_1).add(button_2).add(button_back)

    bot.send_message(chat_id=callback.message.chat.id, text='Бағыттары таңдаңыз', reply_markup=markup_url)



def informatika(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}informatika 5')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("Информатика", 5, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def matematika(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}mat 5')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("Математика", 5, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')



def kaz_yaz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}kaz 5')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("Казахский язык", 5, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def kaz_lit(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}kazl 5')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("Казахская литература", 5, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')



def est(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}est 5')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("Естествознание", 5, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')



def hkz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}hkz 5')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("История Казахстана", 5, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def hm(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}hm 5')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("История Мира", 5, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def geo(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}geo 5')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("География", 5, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def ang(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}ang 5')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("Английский язык", 5, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def mat_bil(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{mat}5')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Нап {bala_time_ru} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text(mat, 5, 40, 60, 1000),
                     reply_markup=markup_url, parse_mode='html')


def gum_bil(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{gum}5')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Нап {bala_time_ru} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text(gum, 5, 40, 60, 1000),
                     reply_markup=markup_url, parse_mode='html')


def informatika_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}informatika 5')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Информатика", 5, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def matematika_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}mat 5')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Математика", 5, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')



def kaz_yaz_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}kaz 5')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Қазақ тілі", 5, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def kaz_lit_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}kazl 5')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Қазақ әдебиеті", 5, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')



def est_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}est 5')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Естествознание", 5, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')



def hkz_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}hkz 5')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Қазақстан тарихы", 5, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def hm_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}hm 5')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Әлем тарихы", 5, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def geo_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}geo 5')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("География", 5, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def ang_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}ang 5')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Ағылшын тілі", 5, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def mat_bil_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{mat_kz}5')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Нап {bala_time_kz} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz(mat_kz, 5, 40, 60, 1000),
                     reply_markup=markup_url, parse_mode='html')


def gum_bil_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{gum_kz}5')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Нап {bala_time_kz} 5')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz(gum_kz, 5, 40, 60, 1000),
                     reply_markup=markup_url, parse_mode='html')

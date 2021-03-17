from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


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

    button_1 = InlineKeyboardButton(text=f'{sprint_ru}', callback_data=f'{sprint_ru} 11')
    button_2 = InlineKeyboardButton(text=f'{bala_time_ru}', callback_data=f'{bala_time_ru} 11')

    button_menu = InlineKeyboardButton(text=f'Главное меню', callback_data='ru')

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    markup_url.add(button_1).add(button_menu)
    bot.send_message(chat_id=callback.message.chat.id, text='Выберите', reply_markup=markup_url)


def reply_sprint_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Список предметов', callback_data=f'Список {sprint_ru} 11')
    button_2 = InlineKeyboardButton(text='Положение', callback_data=f'Положение {sprint_ru}')
    button_menu = InlineKeyboardButton(text=f'Главное меню', callback_data='ru')

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    markup_url.add(button_1, button_2).add(button_menu)
    bot.send_message(chat_id=callback.message.chat.id, text=bilgen_sprint_txt_ru, reply_markup=markup_url)


def reply_sprint_list_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Информатика', callback_data=f'Информатика {sprint_ru}11')
    button_2 = InlineKeyboardButton(text='Математика', callback_data=f'Мат {sprint_ru} 11')
    button_3 = InlineKeyboardButton(text='Казахский язык', callback_data=f'Каз {sprint_ru} 11')
    button_4 = InlineKeyboardButton(text='Казахская литература', callback_data=f'Казл {sprint_ru} 11')
    button_5 = InlineKeyboardButton(text='Биология', callback_data=f'Био {sprint_ru} 11')
    button_6 = InlineKeyboardButton(text='Химия', callback_data=f'Хим {sprint_ru} 11')
    button_7 = InlineKeyboardButton(text='Физика', callback_data=f'Физ {sprint_ru} 11')
    button_8 = InlineKeyboardButton(text='История Казахстана', callback_data=f'Иск {sprint_ru} 11')
    button_9 = InlineKeyboardButton(text='История Мира', callback_data=f'Мира {sprint_ru} 11')
    button_10 = InlineKeyboardButton(text='География', callback_data=f'Гео {sprint_ru} 11')
    button_11 = InlineKeyboardButton(text='Английский язык', callback_data=f'Анг {sprint_ru} 11')

    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Олимпиады 11')

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    markup_url.add(button_2, button_3).add(button_7).add(button_10, button_5).add(button_back)
    bot.send_message(chat_id=callback.message.chat.id, text='\n\nСписок предметов\n\n', reply_markup=markup_url)


def reply_bilik_time_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Направления', callback_data=f'Нап {bala_time_ru} 11')
    button_2 = InlineKeyboardButton(text='Положение', callback_data=f'Положение {bala_time_ru}')

    button_menu = InlineKeyboardButton(text=f'Главное меню', callback_data='ru')

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    markup_url.add(button_1, button_2).add(button_menu)
    bot.send_message(chat_id=callback.message.chat.id, text=bilik_ru, reply_markup=markup_url)


def reply_bilik_time_list_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text=mat, callback_data=f'{mat} 11')
    button_2 = InlineKeyboardButton(text=gum, callback_data=f'{gum} 11')

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Олимпиады 11')

    markup_url.add(button_1).add(button_2).add(button_back)
    bot.send_message(chat_id=callback.message.chat.id, text='Выберите направление', reply_markup=markup_url)

##############################################################################################################      KZ
def reply_list_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text=f'{sprint_kz}', callback_data=f'{sprint_kz} 11')
    button_2 = InlineKeyboardButton(text=f'{bala_time_kz}', callback_data=f'{bala_time_kz} 11')

    button_menu = InlineKeyboardButton(text=f'Басты бет', callback_data='kz')

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    markup_url.add(button_1).add(button_menu)
    bot.send_message(chat_id=callback.message.chat.id, text='Таңдаңыз', reply_markup=markup_url)


def reply_sprint_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Пәндер тізімі', callback_data=f'Список {sprint_kz} 11')
    button_2 = InlineKeyboardButton(text='Ереже', callback_data=f'Положение {sprint_kz}')

    button_menu = InlineKeyboardButton(text=f'Басты бет', callback_data='kz')

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    markup_url.add(button_1, button_2).add(button_menu)
    bot.send_message(chat_id=callback.message.chat.id, text=bilgen_sprint_txt_kz, reply_markup=markup_url)


def reply_sprint_list_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Информатика', callback_data=f'Информатика {sprint_kz}11')
    button_2 = InlineKeyboardButton(text='Математика', callback_data=f'Мат {sprint_kz} 11')
    button_3 = InlineKeyboardButton(text='Қазақ тілі', callback_data=f'Каз {sprint_kz} 11')
    button_4 = InlineKeyboardButton(text='Қазақ әдебиеті', callback_data=f'Казл {sprint_kz} 11')
    button_5 = InlineKeyboardButton(text='Биология', callback_data=f'Био {sprint_kz} 11')
    button_6 = InlineKeyboardButton(text='Химия', callback_data=f'Хим {sprint_kz} 11')
    button_7 = InlineKeyboardButton(text='Физика', callback_data=f'Физ {sprint_kz} 11')
    button_8 = InlineKeyboardButton(text='Қазақстан тарихы', callback_data=f'Иск {sprint_kz} 11')
    button_9 = InlineKeyboardButton(text='Әлем тарихы', callback_data=f'Мира {sprint_kz} 11')
    button_10 = InlineKeyboardButton(text='География', callback_data=f'Гео {sprint_kz} 11')
    button_11 = InlineKeyboardButton(text='Ағылшын тілі', callback_data=f'Анг {sprint_kz} 11')

    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Олимпиады 11kz')

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    markup_url.add(button_2, button_3).add(button_7).add(button_10, button_5).add(button_back)
    bot.send_message(chat_id=callback.message.chat.id, text='\n\nПәндер тізімі\n\n', reply_markup=markup_url)


def reply_bilik_time_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Бағыттары', callback_data=f'Нап {bala_time_kz} 11')
    button_2 = InlineKeyboardButton(text='Ереже', callback_data=f'Положение {bala_time_kz}')

    button_menu = InlineKeyboardButton(text=f'Басты бет', callback_data='kz')

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    markup_url.add(button_1, button_2).add(button_menu)
    bot.send_message(chat_id=callback.message.chat.id, text=bilik_kz, reply_markup=markup_url)


def reply_bilik_time_list_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text=mat_kz, callback_data=f'{mat_kz} 11')
    button_2 = InlineKeyboardButton(text=gum_kz, callback_data=f'{gum_kz} 11')

    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Олимпиады 11kz')

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    markup_url.add(button_1).add(button_2).add(button_back)
    bot.send_message(chat_id=callback.message.chat.id, text='Бағыттары таңдаңыз', reply_markup=markup_url)

##############################################################################################################      KZ
def text(subject, class_, num_of_tasks, time, cost):
    return f"<b>{subject} - {class_} класс </b>\n\nКоличество задач - <i><b>{num_of_tasks}</b></i>\n" \
           f"Время выполнения - <i><b>{time}</b></i> минут\n" \
           f"Цена - <i><b>{cost}</b></i> ₸"


def text_kz(subject, class_, num_of_tasks, time, cost):
    return f"<b>{subject} - {class_} сынып </b>\n\nТапсырма саны - <i><b>{num_of_tasks}</b></i>\n" \
           f"Орындау уақыты - <i><b>{time}</b></i> минут\n" \
           f"Бағасы - <i><b>{cost}</b></i> ₸"


def informatika(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}informatika 11')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("Информатика", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def matematika(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}mat 11')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("Математика", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def kaz_yaz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}kaz 11')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("Казахский язык", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def kaz_lit(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}kazl 11')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("Казахская литература", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def bio(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}bio 11')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("Биология", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def xim(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}xim 11')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("Химия", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def fiz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}fiz 11')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("Физика", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def hkz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}hkz 11')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("История Казахстана", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def hm(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}hm 11')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("История Мира", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def geo(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}geo 11')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("География", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def ang(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{sprint_ru}ang 11')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Список {sprint_ru} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text("Английский язык", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def mat_bil(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{mat}11')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Нап {bala_time_ru} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text(mat, 11, 40, 60, 1000),
                     reply_markup=markup_url, parse_mode='html')


def gum_bil(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'{gum}11')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Нап {bala_time_ru} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text(gum, 11, 40, 60, 1000),
                     reply_markup=markup_url, parse_mode='html')

#############################################################################################       KZ
def informatika_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}informatika 11')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Информатика", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def matematika_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}mat 11')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Математика", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def kaz_yaz_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}kaz 11')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Қазақ тілі", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def kaz_lit_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}kazl 11')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Қазақ әдебиеті", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def bio_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}bio 11')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Биология", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def xim_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}xim 11')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Химия", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def fiz_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}fiz 11')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Физика", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def hkz_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}hkz 11')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Қазақстан тарихы", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def hm_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}hm 11')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Әлем тарихы", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def geo_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}geo 11')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("География", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def ang_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{sprint_kz}ang 11')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Список {sprint_kz} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz("Ағылшын тілі", 11, 30, 60, 350),
                     reply_markup=markup_url, parse_mode='html')


def mat_bil_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{mat_kz}11')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Нап {bala_time_kz} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz(mat_kz, 11, 40, 60, 1000),
                     reply_markup=markup_url, parse_mode='html')


def gum_bil_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'{gum_kz}11')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Нап {bala_time_kz} 11')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz(gum_kz, 11, 40, 60, 1000),
                     reply_markup=markup_url, parse_mode='html')

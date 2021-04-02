from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


techr_kz = 'Білікті педагог – мұғалімдердің біліктілігін арттыру олимпиадасы.'
techr_ru = 'Квалифицированный педагог – олимпиада для повышения квалификации учителей.'

pedagog_kz = 'Білікті педагог'
pedagog_ru = 'Квалифицированный педагог'

sorry = '<u>Приносим свои извинения, олимпиада пока недоступна для прохождения в Telegram.\n' \
        'Скоро все исправим.</u>'
sorry_kz = '<u>Telegram қосымшасы арқылы олимпиада өту уақытша мүмкін емес.\n' \
           'Келеңсіздіктер үшін кешірім сұраймыз.</u>'


def olimp_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text=f'🧑🏻‍🏫 {pedagog_ru}', callback_data=f'{pedagog_ru}')

    button_menu = InlineKeyboardButton(text=f'🎛 Главное меню', callback_data='ru')

    markup_url.add(button_1).add(button_menu)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text='Выберите', reply_markup=markup_url)

def bil_ped_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='📝 Список предметов', callback_data=f'Спис {pedagog_ru}')
    button_2 = InlineKeyboardButton(text='📃 Положение', callback_data=f'Пол{pedagog_ru}')

    button_menu = InlineKeyboardButton(text=f'🎛 Главное меню', callback_data='ru')

    markup_url.add(button_1, button_2).add(button_menu)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=f'{techr_ru}', reply_markup=markup_url,
                     parse_mode='html')


def ped_list_ru(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Английский язык', callback_data=f'Анг {pedagog_ru}')
    button_2 = InlineKeyboardButton(text='Начальные классы', callback_data=f'Нач {pedagog_ru}')
    button_3 = InlineKeyboardButton(text='Биология', callback_data=f'Био {pedagog_ru}')
    button_4 = InlineKeyboardButton(text='География', callback_data=f'Гео {pedagog_ru}')
    button_5 = InlineKeyboardButton(text='Информатика', callback_data=f'Инф {pedagog_ru}')
    button_6 = InlineKeyboardButton(text='Труд', callback_data=f'Труд {pedagog_ru}')
    button_7 = InlineKeyboardButton(text='Математика', callback_data=f'Мат {pedagog_ru}')
    button_8 = InlineKeyboardButton(text='Русский язык', callback_data=f'Рус {pedagog_ru}')
    button_9 = InlineKeyboardButton(text='Самопознание', callback_data=f'Сам {pedagog_ru}')
    button_10 = InlineKeyboardButton(text='История', callback_data=f'Ист {pedagog_ru}')
    button_11 = InlineKeyboardButton(text='Физика', callback_data=f'Физ {pedagog_ru}')
    button_12 = InlineKeyboardButton(text='Химия', callback_data=f'Хим {pedagog_ru}')
    button_13 = InlineKeyboardButton(text='Физкультура', callback_data=f'Физра {pedagog_ru}')
    button_14 = InlineKeyboardButton(text='Каз. язык и литература', callback_data=f'Каз {pedagog_ru}')
    button_15 = InlineKeyboardButton(text='Педагогика-Психология', callback_data=f'Пед {pedagog_ru}')

    button_back = InlineKeyboardButton(text='🔙 Назад', callback_data=f'Олимпиады 0')

    markup_url.add(button_1).add(button_2).add(button_3, button_4, button_6).add(button_5, button_7).\
        add(button_8, button_9).add(button_10, button_11, button_12).add(button_13, button_14).\
        add(button_15).add(button_back)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text='\n\nСписок предметов\n\n', reply_markup=markup_url)

###################################################################################################################  KZ

def olimp_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text=f'🧑🏻‍🏫 {pedagog_kz}', callback_data=f'{pedagog_kz}')
    button_menu = InlineKeyboardButton(text=f'🎛 Басты бет', callback_data='kz')

    markup_url.add(button_1).add(button_menu)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text='Таңдаңыз', reply_markup=markup_url)

def bil_ped_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='📝 Пәндер тізімі', callback_data=f'Спис {pedagog_kz}')
    button_2 = InlineKeyboardButton(text='📃 Ереже', callback_data=f'Пол{pedagog_kz}')

    button_menu = InlineKeyboardButton(text=f'🎛 Басты бет', callback_data='kz')

    markup_url.add(button_1, button_2).add(button_menu)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=f'{techr_kz}', reply_markup=markup_url,
                     parse_mode='html')


def ped_list_kz(callback, bot):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Ағылшын тілі', callback_data=f'Анг {pedagog_kz}')
    button_2 = InlineKeyboardButton(text='Бастауыш сынып', callback_data=f'Нач {pedagog_kz}')
    button_3 = InlineKeyboardButton(text='Биология', callback_data=f'Био {pedagog_kz}')
    button_4 = InlineKeyboardButton(text='География', callback_data=f'Гео {pedagog_kz}')
    button_5 = InlineKeyboardButton(text='Информатика', callback_data=f'Инф {pedagog_kz}')
    button_6 = InlineKeyboardButton(text='Еңбек', callback_data=f'Труд {pedagog_kz}')
    button_7 = InlineKeyboardButton(text='Математика', callback_data=f'Мат {pedagog_kz}')
    button_8 = InlineKeyboardButton(text='Орыс тілі', callback_data=f'Рус {pedagog_kz}')
    button_9 = InlineKeyboardButton(text='Өзін-өзі тану', callback_data=f'Сам {pedagog_kz}')
    button_10 = InlineKeyboardButton(text='Тарих', callback_data=f'Ист {pedagog_kz}')
    button_11 = InlineKeyboardButton(text='Физика', callback_data=f'Физ {pedagog_kz}')
    button_12 = InlineKeyboardButton(text='Химия', callback_data=f'Хим {pedagog_kz}')
    button_13 = InlineKeyboardButton(text='Дене шынықтыру', callback_data=f'Физра {pedagog_kz}')
    button_14 = InlineKeyboardButton(text='Қазақ тілі және әдебиеті', callback_data=f'Каз {pedagog_kz}')
    button_15 = InlineKeyboardButton(text='Педагогика-Психология', callback_data=f'Пед {pedagog_kz}')

    button_back = InlineKeyboardButton(text='🔙 Кері оралу', callback_data=f'Олимпиады 0kz')

    markup_url.add(button_1).add(button_2).add(button_3, button_4).add(button_5, button_7).\
        add(button_8, button_9).add(button_10, button_11, button_12).add(button_14).add(button_6, button_13).\
        add(button_15).\
        add(button_back)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text='\n\nПәндер тізімі\n\n', reply_markup=markup_url)

from telebot import TeleBot
from telebot.types import KeyboardButton
from telebot.types import Message
from telebot.types import ReplyKeyboardMarkup
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


def main():
    bot.polling()


TOKEN = '1444931205:AAFd87IYZON5mVbfxi9-zVGf45mkLYXvPLY'

bot = TeleBot(token=TOKEN)


buttons = dict()


def status_kz(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_teacher = KeyboardButton('Мұғалім')
    button_student = KeyboardButton('Оқушы')
    button_alippe = KeyboardButton('Bilgen Әліппе')
    markup.add(button_teacher).add(button_student).add(button_alippe)
    bot.send_message(chat_id=id, text='Дәрежеңіз', reply_markup=markup)


def status_ru(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_teacher = KeyboardButton('Преподаватель')
    button_student = KeyboardButton('Ученик')
    markup.add(button_teacher).add(button_student)
    bot.send_message(chat_id=id, text='Ваш статус', reply_markup=markup)


def alippe(id):
    markup = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Сатып алу', url='wa.me/77783873039')
    button_2 = InlineKeyboardButton(text='Видео нұсқаулық', callback_data='Видео нұсқаулық')

    markup.add(button_1).add(button_2)

    bot.send_message(chat_id=id, text=alippe_txt, reply_markup=markup)


def info_1(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button_1 = KeyboardButton('Tanymger Expert')
    button_2 = KeyboardButton('Bilgen Tech')
    button_3 = KeyboardButton('Oysana')
    button_4 = KeyboardButton('Тоғызқұмалақ')
    button_5 = KeyboardButton('Білікті педагог')

    button_back = KeyboardButton('Кері оралу 🔙')

    markup.add(button_1).add(button_2).add(button_3).add(button_4).add(button_5).add(button_back)
    bot.send_message(chat_id=id, text=info_1_str, reply_markup=markup)


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

    button_back = KeyboardButton('Кері  оралу 🔙')

    markup.add(button_1).add(button_2).add(button_back)
    bot.send_message(chat_id=id, text=info_3_str, reply_markup=markup)


def info_4(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button_1 = KeyboardButton('Tanymger  Expert')
    button_2 = KeyboardButton('Bilgen  Tech')
    button_3 = KeyboardButton('Оуsana')
    button_4 = KeyboardButton('Toғызқұмалақ')
    button_5 = KeyboardButton('Квалифицированный педагог')

    button_back = KeyboardButton('Назад 🔙')

    markup.add(button_1).add(button_2).add(button_3).add(button_4).add(button_5).add(button_back)
    bot.send_message(chat_id=id, text=info_4_str, reply_markup=markup)


def student_ru(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button_1 = KeyboardButton('Курсы')
    button_2 = KeyboardButton('Олимпиады')

    button_back = KeyboardButton('Назад 🔙')

    markup.add(button_1).add(button_2).add(button_back)
    bot.send_message(chat_id=id, text='Выберите', reply_markup=markup)


def info_5(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button_1 = KeyboardButton('Bilgen  UBT')
    button_2 = KeyboardButton('Bilgen  Tech')

    button_back = KeyboardButton('Назaд 🔙')

    markup.add(button_1).add(button_2).add(button_back)
    bot.send_message(chat_id=id, text=info_5_str, reply_markup=markup)


def info_6(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button_1 = KeyboardButton('Bilgen  Baige/Alaman')
    button_2 = KeyboardButton('Bala/Bilik  Time')

    button_back = KeyboardButton('Назaд 🔙')

    markup.add(button_1).add(button_2).add(button_back)
    bot.send_message(chat_id=id, text=info_6_str, reply_markup=markup)


def send_info(id, text, lng, condition):
    markup_url = InlineKeyboardMarkup()

    button_1 = InlineKeyboardButton(text='Тіркелу', url='https://bilgen.academy/intranet/custom_signup_new.php')
    button_2 = InlineKeyboardButton(text='Төлем жүйесі', callback_data='Төлем жүйесі')
    button_3 = InlineKeyboardButton(text='Регистрация', url='https://bilgen.academy/intranet/custom_signup_new.php')
    button_4 = InlineKeyboardButton(text='Способ оплаты', callback_data='Способ оплаты')

    button_5 = InlineKeyboardButton(text=text, callback_data=condition)

    if lng == 'kz':
        markup_url.add(button_1).add(button_2).add(button_5)
        bot.send_message(chat_id=id, text='Таңдаңыз...', reply_markup=markup_url)
    else:
        markup_url.add(button_3).add(button_4).add(button_5)
        bot.send_message(chat_id=id, text='Выберите...', reply_markup=markup_url)


@bot.callback_query_handler(func=lambda callback: callback.data == 'Способ оплаты' or callback.data == 'Төлем жүйесі')
def reply_video(callback):
    try:
        bot.send_video(chat_id=callback.message.chat.id, data=open('./Pay_method/KASPI.mp4', 'rb'))
    except ConnectionError:
        pass


@bot.callback_query_handler(func=lambda callback: callback.data == 'Видео нұсқаулық')
def reply_video(callback):
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
@bot.callback_query_handler(func=lambda callback: callback.data == 'Bilgen Tech')
def reply_condition_bilgen_tech_kz(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(tech_kz_path, 'rb'))
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
@bot.callback_query_handler(func=lambda callback: callback.data == 'Білікті педагог')
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
@bot.callback_query_handler(func=lambda callback: callback.data == 'Bilgen  Tech')
def reply_condition_bilgen_tech_ru(callback):
    try:
        bot.send_message(chat_id=callback.message.chat.id, text='Sorry, this file is not ready to demonstrate it yet')
        # bot.send_document(chat_id=callback.message.chat.id, data=open(tech_ru_path, 'rb'))
    except ConnectionError:
        pass

##############################################################################################
@bot.callback_query_handler(func=lambda callback: callback.data == 'Оуsana')
def reply_condition_oysana_ru(callback):
    try:
        bot.send_message(chat_id=callback.message.chat.id, text='Sorry, this file is not ready to demonstrate it yet')
        # bot.send_document(chat_id=callback.message.chat.id, data=open(oys_ru_path, 'rb'))
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
@bot.callback_query_handler(func=lambda callback: callback.data == 'Квалифицированный педагог')
def reply_condition_teacher_ru(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(techr_ru_path, 'rb'))
    except ConnectionError:
        pass

##############################################################################################  RU
##############################################################################################  STUDENT
@bot.callback_query_handler(func=lambda callback: callback.data == 'Bilgen  UBT')
def reply_condition_ubt_ru(callback):
    try:
        bot.send_message(chat_id=callback.message.chat.id, text='Sorry, this file is not ready to demonstrate it yet')
        # bot.send_document(chat_id=callback.message.chat.id, data=open(ubt_ru_path, 'rb'))
    except ConnectionError:
        pass

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
##############################################################################################
##############################################################################################
##############################################################################################


def decorator(func, arg1, arg2=None, arg3=None):
    if arg2 is None:
        return func(arg1)
    else: return func(arg1, arg2, arg3)


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_kz = KeyboardButton('🇰🇿 Қазақша')
    button_ru = KeyboardButton('🇷🇺 Русский')
    markup.add(button_kz).add(button_ru)
    bot.send_message(chat_id=message.chat.id, text=say_hello, reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def buttons_tree(message: Message):
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



    ###############################################
    if message.text == '🇰🇿 Қазақша' or message.text == 'Кері оралу 🔙':
        status_kz(id=id_)
    elif message.text == '🇷🇺 Русский' or message.text == 'Назад 🔙':
        status_ru(id=id_)
    ###############################################
    elif message.text == 'Мұғалім':
        info_1(id=id_)
    elif message.text == 'Оқушы' or message.text == 'Кері  оралу 🔙':
        student_kz(id=id_)
    elif message.text == 'Bilgen Әліппе':
        alippe(id=id_)
    ###############################################
    elif message.text == 'Курстар':
        info_2(id=id_)
    elif message.text == 'Олимпиадалар':
        info_3(id=id_)
    ###############################################
    elif message.text == 'Преподаватель':
        info_4(id=id_)
    elif message.text == 'Ученик' or message.text == 'Назaд 🔙':
        student_ru(id=id_)
    ###############################################
    elif message.text == 'Курсы':
        info_5(id=id_)
    elif message.text == 'Олимпиады':
        info_6(id=id_)
    ###############################################
    elif message.text == 'Tanymger Expert':
        send_info(id=id_, text=choose_kz, lng='kz', condition='Tanymger Expert')
    elif message.text == 'Bilgen Tech':
        send_info(id=id_, text=choose_kz, lng='kz', condition='Bilgen Tech')
    elif message.text == 'Oysana':
        send_info(id=id_, text=choose_kz, lng='kz', condition='Oysana')
    elif message.text == 'Тоғызқұмалақ':
        send_info(id=id_, text=choose_kz, lng='kz', condition='Тоғызқұмалақ')
    elif message.text == 'Білікті педагог':
        send_info(id=id_, text=choose_kz, lng='kz', condition='Білікті педагог')
    ###############################################
    elif message.text == 'Tanymger  Expert':
        send_info(id=id_, text=choose_ru, lng='ru', condition='Tanymger  Expert')
    elif message.text == 'Bilgen  Tech':
        send_info(id=id_, text=choose_ru, lng='ru', condition='Bilgen  Tech')
    elif message.text == 'Оуsana':
        send_info(id=id_, text=choose_ru, lng='ru', condition='Оуsana')
    elif message.text == 'Toғызқұмалақ':
        send_info(id=id_, text=choose_ru, lng='ru', condition='Toғызқұмалақ')
    elif message.text == 'Квалифицированный педагог':
        send_info(id=id_, text=choose_ru, lng='ru', condition='Квалифицированный педагог')
    ###############################################
    elif message.text == 'Bilgen UBT':
        send_info(id=id_, text=choose_kz, lng='kz', condition='Bilgen UBT')
    ###############################################
    elif message.text == 'Bilgen Baige/Alaman':
        send_info(id=id_, text=choose_kz, lng='kz', condition='Bilgen Baige/Alaman')
    elif message.text == 'Bala/Bilik Time':
        send_info(id=id_, text=choose_kz, lng='kz', condition='Bala/Bilik Time')
    ###############################################
    elif message.text == 'Bilgen  UBT':
        send_info(id=id_, text=choose_ru, lng='ru', condition='Bilgen  UBT')
    ###############################################
    elif message.text == 'Bilgen  Baige/Alaman':
        send_info(id=id_, text=choose_ru, lng='ru', condition='Bilgen  Baige/Alaman')
    elif message.text == 'Bala/Bilik  Time':
        send_info(id=id_, text=choose_ru, lng='ru', condition='Bala/Bilik  Time')
    ###############################################
    # elif message.data == 'Төлем жүйесі' or message.data == 'Способ оплаты':
    #     bot.send_video(chat_id=id_, data=open('./Pay_method/KASPI.mp4', 'rb'))


say_hello = 'Тілді таңдаңыз\nВыберите язык'

choose_kz = 'Ережені жүктеу'

choose_ru = 'Скачать положение'

alippe_txt = f'Bilgen Әліппе әлемін бірге саяхаттауға шақырамыз❗️\n' \
             f'Bilgen Әліппе оқулығы оқылым, жазылым, айтылым және тыңдалым — 4 дағды бойынша жүргізіледі.\n' \
             f'Танымдық әрі қызықты бұл оқулық өз оқырманын бірден баурап алатыны сөзсіз💯✔️ ' \
             f'Себебі оқулықтың мобильді нұсқасы бар. ' \
             f'Ал саяхаттың мазмұнды да әсерлі өтуіне Bilge Bala мен Айкерім көмектеседі. \n\n' \
             f'Әліппе әлемін бірге тамашалағыңыз келсе, тапсырыс беріңіз.\n\n' \
             f'Бағасы: 3 500 kzt'

#######################################################################################################################
tanymger_kz = 'Tanymger Expert – заманауи электронды оқулық жасау бойынша авторлар мен баспа қызметкерлерінің ' \
              'біліктілігін арттыру курсы.'

tech_kz = 'Bilgen Tech – IT саласы бойынша бағдарламалау курсы.'

oys_kz = 'Oysana – менталды арифметика курсы.'

tog_kz = 'Тоғызқұмалақ – дене шынықтыру мамандарына "Тоғызқұмалақ" ұлттық ойынын үйрету.'

techr_kz = 'Білікті педагог – мұғалімдердің біліктілігін арттыру олимпиадасы.'


tanymger_kz_path = './condition_kz/teacher/Tanymger Expert.docx'

tech_kz_path = './condition_kz/teacher/BilGenTech.pdf'

oys_kz_path = './condition_kz/teacher/BilGen Oysana.pdf'

tog_kz_path = './condition_kz/teacher/Тогызкумалак.docx'

techr_kz_path = './condition_kz/teacher/Білікті Педагог.docx'


info_1_str = f'{tanymger_kz}\n\n{tech_kz}\n\n{oys_kz}\n\n{tog_kz}\n\n{techr_kz}'
#######################################################################################################################


#######################################################################################################################
tanymger_ru = 'Tanymger  Expert – курс повышения квалификации для авторов и сотрудников издании ' \
              'по разработке электронного учебника.'

tech_ru = 'Bilgen Tech – курс программирования.'

oys_ru = 'Oysana – курс ментальной арифметики.'

tog_ru = 'Тоғызқұмалақ – обучение учителей физкультуры национальной игре «Тогызкумалак».'

techr_ru = 'Квалифицированный педагог – олимпиада для повышения квалификации учителей.'

info_4_str = f'{tanymger_ru}\n\n{tech_ru}\n\n{oys_ru}\n\n{tog_ru}\n\n{techr_ru}'


tanymger_ru_path = 'condition_ru/teacher/Tanymger Expert.docx'

tech_ru_path = ''

oys_ru_path = ''

tog_ru_path = './condition_ru/teacher/Тогызкумалак.docx'

techr_ru_path = './condition_ru/teacher/Кваливицированный Педагог.docx'

#######################################################################################################################


#######################################################################################################################
ubt_kz = 'Bilgen UBT – 10-11 сынып оқушыларын таңдау пәні бойынша ҰБТ-ға дайындау курсы.'

baige_kz = '«Bilgen Baige» бастауыш сынып оқушыларына, «Bilgen Alaman» жоғарғы сынып оқушыларына арналған ' \
           'пәндік олимпиадалар.'

bilik_kz = 'Bala/Bilik Time – Бастауыш пен жоғарғы сыныптар арасында республикалық көлемде өтетін онлайн олимпиадалар.'


ubt_kz_path = './condition_kz/student/BilGen UBT.pdf'

baige_kz_path = './condition_kz/student/BilGen Baige, BilGen Alaman.pdf'

bilik_kz_path = './condition_kz/student/BilGen Bala, Bilik TIME.docx'


info_2_str = f'{ubt_kz}\n\n{tech_kz}'

info_3_str = f'{baige_kz}\n\n{bilik_kz}'
#######################################################################################################################


#######################################################################################################################
ubt_ru = 'Bilgen UBT – курс подготовки к ЕНТ для учеников 10-11 классов.'

baige_ru = 'Предметные олимпиады для учеников младших классов «Bilgen Baige» и старшеклассников «Bilgen Alaman».'

bilik_ru = 'Bala/Bilik Time – Республиканские онлайн-олимпиады для учеников 1-11 классов.'


ubt_ru_path = ''

baige_ru_path = 'condition_ru/student/BilGen  Baige, BilGen Alaman.docx'

bilik_ru_path = './condition_ru/student/BilGen Bala, Bilik TIME.pdf'


info_5_str = f'{ubt_ru}\n\n{tech_ru}'

info_6_str = f'{baige_ru}\n\n{bilik_ru}'
#######################################################################################################################


if __name__ == '__main__':
    main()

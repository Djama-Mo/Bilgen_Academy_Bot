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
    markup.add(button_teacher).add(button_student)
    bot.send_message(chat_id=id, text='Дәрежеңіз', reply_markup=markup)


def status_ru(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_teacher = KeyboardButton('Преподаватель')
    button_student = KeyboardButton('Ученик')
    markup.add(button_teacher).add(button_student)
    bot.send_message(chat_id=id, text='Ваш статус', reply_markup=markup)


def info_1(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton('Tanymger Expert')
    button_2 = KeyboardButton('Bilgen Tech')
    button_3 = KeyboardButton('Oysana')
    button_4 = KeyboardButton('Тоғызқұмалақ')
    button_5 = KeyboardButton('Білікті педагог')
    markup.add(button_1).add(button_2).add(button_3).add(button_4).add(button_5)
    bot.send_message(chat_id=id, text=info_1_str, reply_markup=markup)


def student_kz(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton('Курстар')
    button_2 = KeyboardButton('Олимпиадалар')
    markup.add(button_1).add(button_2)
    bot.send_message(chat_id=id, text='Tаңдаңыз', reply_markup=markup)


def info_2(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton('Bilgen UBT')
    button_2 = KeyboardButton('Bilgen Tech')
    markup.add(button_1).add(button_2)
    bot.send_message(chat_id=id, text=info_2_str, reply_markup=markup)


def info_3(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton('Bilgen Baige/Alaman')
    button_2 = KeyboardButton('Bala/Bilik Time')
    markup.add(button_1).add(button_2)
    bot.send_message(chat_id=id, text=info_3_str, reply_markup=markup)


def info_4(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton('Tanymger  Expert')
    button_2 = KeyboardButton('Bilgen  Tech')
    button_3 = KeyboardButton('Оуsana')
    button_4 = KeyboardButton('Toғызқұмалақ')
    button_5 = KeyboardButton('Квалифицированный педагог')
    markup.add(button_1).add(button_2).add(button_3).add(button_4).add(button_5)
    bot.send_message(chat_id=id, text=info_4_str, reply_markup=markup)


def student_ru(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton('Курсы')
    button_2 = KeyboardButton('Олимпиады')
    markup.add(button_1).add(button_2)
    bot.send_message(chat_id=id, text='Выберите', reply_markup=markup)


def info_5(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton('Bilgen  UBT')
    button_2 = KeyboardButton('Bilgen  Tech')
    markup.add(button_1).add(button_2)
    bot.send_message(chat_id=id, text=info_5_str, reply_markup=markup)


def info_6(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton('Bilgen  Baige/Alaman')
    button_2 = KeyboardButton('Bala/Bilik  Time')
    markup.add(button_1).add(button_2)
    bot.send_message(chat_id=id, text=info_6_str, reply_markup=markup)


def send_info(id, text, lng):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton('Тіркелу')
    button_2 = KeyboardButton('Төлем жүйесі')
    button_3 = KeyboardButton('Регистрация')
    button_4 = KeyboardButton('Способ оплаты')
    if lng == 'kz':
        markup.add(button_1).add(button_2)
    elif lng == 'ru':
        markup.add(button_3).add(button_4)
    bot.send_message(chat_id=id, text=text, reply_markup=markup)


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
    ###############################################
    if message.text == '🇰🇿 Қазақша':
        status_kz(id=id_)
    elif message.text == '🇷🇺 Русский':
        status_ru(id=id_)
    ###############################################
    elif message.text == 'Мұғалім':
        info_1(id=id_)
    elif message.text == 'Оқушы':
        student_kz(id=id_)
    ###############################################
    elif message.text == 'Курстар':
        info_2(id=id_)
    elif message.text == 'Олимпиадалар':
        info_3(id=id_)
    ###############################################
    elif message.text == 'Преподаватель':
        info_4(id=id_)
    elif message.text == 'Ученик':
        student_ru(id=id_)
    ###############################################
    elif message.text == 'Курсы':
        info_5(id=id_)
    elif message.text == 'Олимпиады':
        info_6(id=id_)
    ###############################################
    elif message.text == 'Tanymger Expert':
        send_info(id=id_, text=choose_kz, lng='kz')
    elif message.text == 'Bilgen Tech':
        send_info(id=id_, text=choose_kz, lng='kz')
    elif message.text == 'Oysana':
        send_info(id=id_, text=choose_kz, lng='kz')
    elif message.text == 'Тоғызқұмалақ':
        send_info(id=id_, text=choose_kz, lng='kz')
    elif message.text == 'Білікті педагог':
        send_info(id=id_, text=choose_kz, lng='kz')
    ###############################################
    elif message.text == 'Tanymger  Expert':
        send_info(id=id_, text=choose_ru, lng='ru')
    elif message.text == 'Bilgen  Tech':
        send_info(id=id_, text=choose_ru, lng='ru')
    elif message.text == 'Оуsana':
        send_info(id=id_, text=choose_ru, lng='ru')
    elif message.text == 'Toғызқұмалақ':
        send_info(id=id_, text=choose_ru, lng='ru')
    elif message.text == 'Квалифицированный педагог':
        send_info(id=id_, text=choose_ru, lng='ru')
    ###############################################
    elif message.text == 'Bilgen UBT':
        send_info(id=id_, text=choose_kz, lng='kz')
    elif message.text == 'Bilgen Tech':
        send_info(id=id_, text=choose_kz, lng='kz')
    ###############################################
    elif message.text == 'Bilgen Baige/Alaman':
        send_info(id=id_, text=choose_kz, lng='kz')
    elif message.text == 'Bala/Bilik Time':
        send_info(id=id_, text=choose_kz, lng='kz')
    ###############################################
    elif message.text == 'Bilgen  UBT':
        send_info(id=id_, text=choose_ru, lng='ru')
    elif message.text == 'Bilgen  Tech':
        send_info(id=id_, text=choose_ru, lng='ru')
    ###############################################
    elif message.text == 'Bilgen  Baige/Alaman':
        send_info(id=id_, text=choose_ru, lng='ru')
    elif message.text == 'Bala/Bilik  Time':
        send_info(id=id_, text=choose_ru, lng='ru')


say_hello = 'Тілді таңдаңыз\nВыберите язык'

choose_kz = 'Ережені жүктеу'

choose_ru = 'Скачать положение'


#######################################################################################################################
tanymger_kz = 'Tanymger Expert – заманауи электронды оқулық жасау бойынша авторлар мен баспа қызметкерлерінің ' \
              'біліктілігін арттыру курсы.'

tech_kz = 'Bilgen Tech – IT саласы бойынша бағдарламалау курсы.'

oys_kz = 'Oysana – менталды арифметика курсы.'

tog_kz = 'Тоғызқұмалақ – дене шынықтыру мамандарына "Тоғызқұмалақ" ұлттық ойынын үйрету.'

techr_kz = 'Білікті педагог – мұғалімдердің біліктілігін арттыру олимпиадасы.'

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
#######################################################################################################################


#######################################################################################################################
ubt_kz = 'Bilgen UBT – 10-11 сынып оқушыларын таңдау пәні бойынша ҰБТ-ға дайындау курсы.'

baige_kz = '«Bilgen Baige» бастауыш сынып оқушыларына, «Bilgen Alaman» жоғарғы сынып оқушыларына арналған ' \
           'пәндік олимпиадалар.'

bilik_kz = 'Bala/Bilik Time – Бастауыш пен жоғарғы сыныптар арасында республикалық көлемде өтетін онлайн олимпиадалар.'

info_2_str = f'{ubt_kz}\n\n{tech_kz}'

info_3_str = f'{baige_kz}\n\n{bilik_kz}'
#######################################################################################################################


#######################################################################################################################
ubt_ru = 'Bilgen UBT – курс подготовки к ЕНТ для учеников 10-11 классов.'

baige_ru = 'Предметные олимпиады для учеников младших классов «Bilgen Baige» и старшеклассников «Bilgen Alaman».'

bilik_ru = 'Bala/Bilik Time – Республиканские онлайн-олимпиады для учеников 1-11 классов.'

info_5_str = f'{ubt_ru}\n\n{tech_ru}'

info_6_str = f'{baige_ru}\n\n{bilik_ru}'
#######################################################################################################################


if __name__ == '__main__':
    main()

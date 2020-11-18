from telebot import TeleBot
from telebot.types import KeyboardButton
from telebot.types import Message
from telebot.types import ReplyKeyboardMarkup
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


def main():
    bot.polling(none_stop=True)


TOKEN = '1444931205:AAFd87IYZON5mVbfxi9-zVGf45mkLYXvPLY'

bot = TeleBot(token=TOKEN)


buttons = dict()

users = set()


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


def info_4(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button_1 = KeyboardButton('Tanymger  Expert')
    button_2 = KeyboardButton('Tanymger  Tech')
    button_3 = KeyboardButton('Toғызқұмалақ')

    button_back = KeyboardButton('Назaд 🔙')  # a''

    markup.add(button_1).add(button_2).add(button_3).add(button_back)
    bot.send_message(chat_id=id, text=info_4_str, reply_markup=markup)


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


def info_5(id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button_1 = KeyboardButton('Bilgen  Tech')

    button_back = KeyboardButton('Haзaд 🔙')  # Ha

    markup.add(button_1).add(button_back)
    bot.send_message(chat_id=id, text=info_5_str, reply_markup=markup)


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
    button_2 = InlineKeyboardButton(text='Төлем жүйесі', callback_data='Төлем жүйесі')
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


@bot.callback_query_handler(func=lambda callback: callback.data == 'Төлем жүйесі')
def reply_video(callback):
    try:
        bot.send_video(chat_id=callback.message.chat.id, data=open('./Pay_method/KASPI.mp4', 'rb'))
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
@bot.callback_query_handler(func=lambda callback: callback.data == 'Квалифицированный педагог')
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
##############################################################################################
@bot.callback_query_handler(func=lambda callback: callback.data == 'Bilgen  Sprint')
def reply_condition_sprint_ru(callback):
    try:
        bot.send_document(chat_id=callback.message.chat.id, data=open(bilgen_sprint_path_ru, 'rb'))
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
    users.add(message.chat.id)
    write_file(message.chat.id)
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
    elif message.text == 'Мұғалім' or message.text == 'Кері оралy 🔙':
        teacher_kz(id=id_)
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
    elif message.text == 'Преподаватель' or message.text == 'Назaд 🔙':
        teacher_ru(id=id_)
    elif message.text == 'Ученик' or message.text == 'Haзaд 🔙':
        student_ru(id=id_)
    ###############################################
    elif message.text == 'Курсы':
        info_5(id=id_)
    elif message.text == 'Олимпиады':
        info_6(id=id_)
    ###############################################
    elif message.text == 'Tanymger Expert':
        send_info(id=id_, text=choose_kz, lng='kz', condition='Tanymger Expert', flag=1)
    elif message.text == 'Tanymger Tech':
        send_info(id=id_, text=choose_kz, lng='kz', condition='Tanymger Tech', flag=1)
    elif message.text == 'Oysana':
        send_info(id=id_, text=choose_kz, lng='kz', condition='Oysana', flag=1)
    elif message.text == 'Тоғызқұмалақ':
        send_info(id=id_, text=choose_kz, lng='kz', condition='Тоғызқұмалақ', flag=1)
    elif message.text == 'Білікті педагог':
        send_info(id=id_, text=choose_kz, lng='kz', condition='Білікті педагог', flag=1)
    ###############################################
    elif message.text == 'Tanymger  Expert':
        send_info(id=id_, text=choose_ru, lng='ru', condition='Tanymger  Expert', flag=1)
    elif message.text == 'Tanymger  Tech':
        send_info(id=id_, text=choose_ru, lng='ru', condition='Tanymger  Tech', flag=1)
    elif message.text == 'Toғызқұмалақ':
        send_info(id=id_, text=choose_ru, lng='ru', condition='Toғызқұмалақ', flag=1)
    elif message.text == 'Квалифицированный педагог':
        send_info(id=id_, text=choose_ru, lng='ru', condition='Квалифицированный педагог', flag=1)
    ###############################################
    elif message.text == 'Bilgen Tech':
        send_info(id=id_, text=choose_kz, lng='kz', condition='Bilgen Tech')
    elif message.text == 'Bilgen UBT':
        send_info(id=id_, text=choose_kz, lng='kz', condition='Bilgen UBT')
    ###############################################
    elif message.text == 'Bilgen Baige/Alaman':
        send_info(id=id_, text=choose_kz, lng='kz', condition='Bilgen Baige/Alaman')
    elif message.text == 'Bala/Bilik Time':
        send_info(id=id_, text=choose_kz, lng='kz', condition='Bala/Bilik Time')
    elif message.text == 'Bilgen Sprint':
        send_info(id=id_, text=choose_kz, lng='kz', condition='Bilgen Sprint')
    ###############################################
    elif message.text == 'Bilgen  Tech':
        send_info(id=id_, text=choose_ru, lng='ru', condition='Bilgen  Tech')
    ###############################################
    elif message.text == 'Bilgen  Baige/Alaman':
        send_info(id=id_, text=choose_ru, lng='ru', condition='Bilgen  Baige/Alaman')
    elif message.text == 'Bala/Bilik  Time':
        send_info(id=id_, text=choose_ru, lng='ru', condition='Bala/Bilik  Time')
    elif message.text == 'Bilgen  Sprint':
        send_info(id=id_, text=choose_ru, lng='ru', condition='Bilgen  Sprint')
    ###############################################
    elif message.text == 'Kypсы':
        info_4(id=id_)
    elif message.text == 'Oлимпиады':
        info_4_2(id=id_)
    ###############################################
    elif message.text == 'Кyрстар':
        info_1(id=id_)
    elif message.text == 'Олимпиадалаp':
        info_1_2(id=id_)
    elif message.text == 'Выведи количество пользователей':
        with open('./users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                users.add(int(line))
        bot.send_message(chat_id=id_, text=f'{len(users)}')
    else:
        bot.send_message(chat_id=id_, text=mistake)


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

mistake = 'Введен не корректный запрос, нажмите на кнопку из нижеперечисленных\n\n' \
          'Дұрыс емес сұрау енгізілді, төменде көрсетілгендерден батырмасын басыңыз'
#######################################################################################################################
tanymger_kz = 'Tanymger Expert – заманауи электронды оқулық жасау бойынша авторлар мен баспа қызметкерлерінің ' \
              'біліктілігін арттыру курсы.'

tech_teach_kz = 'Tanymger Tech – IT саласы бойынша бағдарламалау курсы.'

oys_kz = 'Oysana – менталды арифметика курсы.'

tog_kz = 'Тоғызқұмалақ – дене шынықтыру мамандарына "Тоғызқұмалақ" ұлттық ойынын үйрету.'

techr_kz = 'Білікті педагог – мұғалімдердің біліктілігін арттыру олимпиадасы.'


tanymger_kz_path = './condition_kz/teacher/Tanymger Expert.docx'

tech_kz_path = 'condition_kz/teacher/Tanymger Tech.pdf'

oys_kz_path = './condition_kz/teacher/BilGen Oysana.pdf'

tog_kz_path = './condition_kz/teacher/Тогызкумалак.pdf'

techr_kz_path = './condition_kz/teacher/Білікті педагог.pdf'


info_1_str = f'{tanymger_kz}\n\n{tech_teach_kz}\n\n{oys_kz}\n\n{tog_kz}'

info_1_2_str = f'{tech_teach_kz}\n\n{techr_kz}'
#######################################################################################################################


#######################################################################################################################
tanymger_ru = 'Tanymger  Expert – курс повышения квалификации для авторов и сотрудников издании ' \
              'по разработке электронного учебника.'

tech_teach_ru = 'Tanymger Tech – курс программирования.'

tog_ru = 'Тоғызқұмалақ – обучение учителей физкультуры национальной игре «Тогызкумалак».'

techr_ru = 'Квалифицированный педагог – олимпиада для повышения квалификации учителей.'

info_4_str = f'{tanymger_ru}\n\n{tech_teach_ru}\n\n{tog_ru}'

info_4_2_str = f'{tech_teach_ru}\n\n{techr_ru}'

tanymger_ru_path = 'condition_ru/teacher/Tanymger Expert.docx'

tech_ru_path = './condition_ru/teacher/Tanymger Tech.pdf'

tog_ru_path = './condition_ru/teacher/Тогызкумалак.pdf'

techr_ru_path = 'condition_ru/teacher/Квалифицированный педагог.pdf'

#######################################################################################################################


#######################################################################################################################
ubt_kz = 'Bilgen UBT – 10-11 сынып оқушыларын таңдау пәні бойынша ҰБТ-ға дайындау курсы.'

baige_kz = '«Bilgen Baige» бастауыш сынып оқушыларына, «Bilgen Alaman» жоғарғы сынып оқушыларына арналған ' \
           'пәндік олимпиадалар.'

bilik_kz = 'Bala/Bilik Time – Бастауыш пен жоғарғы сыныптар арасында республикалық көлемде өтетін онлайн олимпиадалар.'

tech_kz = 'Tanymger Tech – IT саласы бойынша бағдарламалау курсы.'

bilgen_sprint_txt_kz = 'Bilgen Sprint - Республикалық қашықтықтан өткізілетін пәндік олимпиада'

ubt_kz_path = './condition_kz/student/BilGen UBT.pdf'

baige_kz_path = './condition_kz/student/BilGen Baige, BilGen Alaman.pdf'

bilik_kz_path = './condition_kz/student/BilGen Bala, Bilik TIME.pdf'

bilgen_sprint_path_kz = './condition_kz/student/BilGen Sprint.pdf'

bilgen_tech_path = './condition_kz/student/BilGenTech.pdf'

info_2_str = f'{ubt_kz}\n\n{tech_kz}'

info_3_str = f'{baige_kz}\n\n{bilik_kz}\n\n{bilgen_sprint_txt_kz}'
#######################################################################################################################


#######################################################################################################################
baige_ru = 'Предметные олимпиады для учеников младших классов «Bilgen Baige» и старшеклассников «Bilgen Alaman».'

bilik_ru = 'Bala/Bilik Time – Республиканские онлайн-олимпиады для учеников 1-11 классов.'

tech_ru = 'Bilgen Tech – курс программирования.'

bilgen_sprint_txt_ru = 'Bilgen Sprint - Республиканская дистанционная предметная олимпиада'

baige_ru_path = 'condition_ru/student/BilGen Baige, BilGen Alaman.pdf'

bilik_ru_path = './condition_ru/student/BilGen Bala, Bilik TIME.pdf'

bilgen_sprint_path_ru = './condition_ru/student/BilGen Sprint.pdf'

info_5_str = f'{tech_ru}'

info_6_str = f'{baige_ru}\n\n{bilik_ru}\n\n{bilgen_sprint_txt_ru}'
#######################################################################################################################

#######################################################################################################################
tanymger_expert_kz = 'Tanymger Expert'
tanymger_tech_kz = 'Tanymger Tech'
oysana_kz = 'Oysana'
togyzqumalaq_kz = 'Тоғызқұмалақ'
pedagog_kz = 'Білікті педагог'

tanymger_expert_ru = 'Tanymger  Expert'
tanymger_tech_ru = 'Tanymger  Tech'
togyzqumalaq_ru = 'Toғызқұмалақ'
pedagog_ru = 'Квалифицированный педагог'

bilgen_tech_kz = 'Bilgen Tech'
bilgen_ubt_kz = 'Bilgen UBT'
bilgen_baige_kz = 'Bilgen Baige/Alaman'
bala_time_kz = 'Bala/Bilik Time'
sprint_kz = 'Bilgen Sprint'

bilgen_tech_ru = 'Bilgen  Tech'
bilgen_baige_ru = 'Bilgen  Baige/Alaman'
bala_time_ru = 'Bala/Bilik  Time'
sprint_ru = 'Bilgen  Sprint'
#######################################################################################################################

def write_file(text):
    with open('./users.txt', 'a') as file:
        file.write(str(text) + '\n')


if __name__ == '__main__':
    main()

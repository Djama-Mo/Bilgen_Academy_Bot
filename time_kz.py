from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


mat_kz = 'Жаратылыстану-математикалық'
gum_kz = 'Қоғамдық-гуманитарлық'

bala_time_kz = 'Bala/Bilik Time'

bilik_kz = 'Bala/Bilik Time – Бастауыш пен жоғарғы сыныптар арасында республикалық көлемде өтетін онлайн олимпиадалар.'

start_the_test_kz = 'Төлеу және тестті бастау'


def olymp_text_kz(time):
    return f'Әр сұраққа жауап беруге {time} минут.\n' \
           f'Егер сіз жауап беріп үлгермесеңіз немесе жауабын білмесеңіз "Келесі сұраққа көшу" батырмасын басыңыз.\n' \
           f'Сіз алдыңғы сұрақтарға кері орала алмайсыз'


def b_mat_11(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data='b_mat_11_kz')
    button_back = InlineKeyboardButton(text='Бағыттар', callback_data=f'Нап {bala_time_kz} 11')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'), reply_markup=markup)


def b_gum_11(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data='b_gum_11_kz')
    button_back = InlineKeyboardButton(text='Бағыттар', callback_data=f'Нап {bala_time_kz} 11')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'), reply_markup=markup)


def b_mat_10(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data='b_mat_10_kz')
    button_back = InlineKeyboardButton(text='Бағыттар', callback_data=f'Нап {bala_time_kz} 10')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'), reply_markup=markup)


def b_gum_10(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data='b_gum_10_kz')
    button_back = InlineKeyboardButton(text='Бағыттар', callback_data=f'Нап {bala_time_kz} 10')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'), reply_markup=markup)


def b_mat_9(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data='b_mat_9_kz')
    button_back = InlineKeyboardButton(text='Бағыттар', callback_data=f'Нап {bala_time_kz} 9')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'), reply_markup=markup)


def b_gum_9(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data='b_gum_9_kz')
    button_back = InlineKeyboardButton(text='Бағыттар', callback_data=f'Нап {bala_time_kz} 9')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'), reply_markup=markup)


def b_mat_8(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data='b_mat_8_kz')
    button_back = InlineKeyboardButton(text='Бағыттар', callback_data=f'Нап {bala_time_kz} 8')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'), reply_markup=markup)


def b_gum_8(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data='b_gum_8_kz')
    button_back = InlineKeyboardButton(text='Бағыттар', callback_data=f'Нап {bala_time_kz} 8')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'), reply_markup=markup)


def b_mat_7(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data='b_mat_7_kz')
    button_back = InlineKeyboardButton(text='Бағыттар', callback_data=f'Нап {bala_time_kz} 7')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'), reply_markup=markup)


def b_gum_7(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data='b_gum_7_kz')
    button_back = InlineKeyboardButton(text='Бағыттар', callback_data=f'Нап {bala_time_kz} 7')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'), reply_markup=markup)


def b_mat_6(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data='b_mat_6_kz')
    button_back = InlineKeyboardButton(text='Бағыттар', callback_data=f'Нап {bala_time_kz} 6')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'), reply_markup=markup)


def b_gum_6(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data='b_gum_6_kz')
    button_back = InlineKeyboardButton(text='Бағыттар', callback_data=f'Нап {bala_time_kz} 6')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'), reply_markup=markup)


def b_mat_5(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data='b_mat_5_kz')
    button_back = InlineKeyboardButton(text='Бағыттар', callback_data=f'Нап {bala_time_kz} 5')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'), reply_markup=markup)


def b_gum_5(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data='b_gum_5_kz')
    button_back = InlineKeyboardButton(text='Бағыттар', callback_data=f'Нап {bala_time_kz} 5')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'), reply_markup=markup)


def b_time_4(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data='b_time_4_kz')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Нап {bala_time_kz} 4')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'), reply_markup=markup)


def b_time_3(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data='b_time_3_kz')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Нап {bala_time_kz} 3')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'), reply_markup=markup)


def b_time_2(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data='b_time_2_kz')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Нап {bala_time_kz} 2')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'), reply_markup=markup)


def b_time_1(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data='b_time_1_kz')
    button_back = InlineKeyboardButton(text='Кері оралу', callback_data=f'Нап {bala_time_kz} 1')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'), reply_markup=markup)

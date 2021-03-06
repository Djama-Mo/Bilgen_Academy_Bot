from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


mat = 'Естественно-математическое'
gum = 'Общественно-гуманитарное'

bala_time_ru = 'Bala/Bilik  Time'

bilik_ru = 'Bala/Bilik Time – Республиканские онлайн-олимпиады для учеников 1-11 классов.'

start_the_test_ru = 'Оплатить и приступить к тесту'


def olymp_text_ru(time):
    return f'На каждый вопрос отведено {time} минуты.\n' \
           f'Если Вы не успели отвеить или не знаете ответа на поставленный вопрос, нажмите на кнопку "Далее".\n' \
           f'Вы не сможете вернуться к предыдущим вопросам'


def b_mat_11(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data='b_mat_11_ru')
    button_back = InlineKeyboardButton(text='К направлениям', callback_data=f'Нап {bala_time_ru} 11')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'), reply_markup=markup)


def b_gum_11(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data='b_gum_11_ru')
    button_back = InlineKeyboardButton(text='К направлениям', callback_data=f'Нап {bala_time_ru} 11')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'), reply_markup=markup)


def b_mat_10(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data='b_mat_10_ru')
    button_back = InlineKeyboardButton(text='К направлениям', callback_data=f'Нап {bala_time_ru} 10')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'), reply_markup=markup)


def b_gum_10(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data='b_gum_10_ru')
    button_back = InlineKeyboardButton(text='К направлениям', callback_data=f'Нап {bala_time_ru} 10')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'), reply_markup=markup)


def b_mat_9(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data='b_mat_9_ru')
    button_back = InlineKeyboardButton(text='К направлениям', callback_data=f'Нап {bala_time_ru} 9')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'), reply_markup=markup)


def b_gum_9(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data='b_gum_9_ru')
    button_back = InlineKeyboardButton(text='К направлениям', callback_data=f'Нап {bala_time_ru} 9')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'), reply_markup=markup)


def b_mat_8(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data='b_mat_8_ru')
    button_back = InlineKeyboardButton(text='К направлениям', callback_data=f'Нап {bala_time_ru} 8')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'), reply_markup=markup)


def b_gum_8(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data='b_gum_8_ru')
    button_back = InlineKeyboardButton(text='К направлениям', callback_data=f'Нап {bala_time_ru} 8')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'), reply_markup=markup)


def b_mat_7(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data='b_mat_7_ru')
    button_back = InlineKeyboardButton(text='К направлениям', callback_data=f'Нап {bala_time_ru} 7')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'), reply_markup=markup)


def b_gum_7(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data='b_gum_7_ru')
    button_back = InlineKeyboardButton(text='К направлениям', callback_data=f'Нап {bala_time_ru} 7')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'), reply_markup=markup)


def b_mat_6(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data='b_mat_6_ru')
    button_back = InlineKeyboardButton(text='К направлениям', callback_data=f'Нап {bala_time_ru} 6')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'), reply_markup=markup)


def b_gum_6(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data='b_gum_6_ru')
    button_back = InlineKeyboardButton(text='К направлениям', callback_data=f'Нап {bala_time_ru} 6')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'), reply_markup=markup)


def b_mat_5(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data='b_mat_5_ru')
    button_back = InlineKeyboardButton(text='К направлениям', callback_data=f'Нап {bala_time_ru} 5')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'), reply_markup=markup)


def b_gum_5(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data='b_gum_5_ru')
    button_back = InlineKeyboardButton(text='К направлениям', callback_data=f'Нап {bala_time_ru} 5')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'), reply_markup=markup)


def b_time_4(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data='b_time_4_ru')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Нап {bala_time_ru} 4')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'), reply_markup=markup)


def b_time_3(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data='b_time_3_ru')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Нап {bala_time_ru} 3')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'), reply_markup=markup)


def b_time_2(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data='b_time_2_ru')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Нап {bala_time_ru} 2')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'), reply_markup=markup)


def b_time_1(callback, bot):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data='b_time_1_ru')
    button_back = InlineKeyboardButton(text='Назад', callback_data=f'Нап {bala_time_ru} 1')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'), reply_markup=markup)

from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


pedagog_kz = 'Білікті педагог'
pedagog_ru = 'Квалифицированный педагог'


def text(subject, num_of_tasks, time, cost):
    return f"<b>{subject}</b>\n\nКоличество задач - <i><b>{num_of_tasks}</b></i>\n" \
           f"Время выполнения - <i><b>{time}</b></i> минут\n" \
           f"Цена - <i><b>{cost}</b></i> ₸"


def text_kz(subject, num_of_tasks, time, cost):
    return f"<b>{subject}</b>\n\nТапсырма саны - <i><b>{num_of_tasks}</b></i>\n" \
           f"Орындау уақыты - <i><b>{time}</b></i> минут\n" \
           f"Бағасы - <i><b>{cost}</b></i> ₸"


start_the_test_ru = 'Оплатить и приступить к тесту'
start_the_test_kz = 'Төлеу және тестті бастау'


def olymp_text_ru(time):
    return f'На каждый вопрос отведено {time} минуты.\n\n' \
           f'Если Вы не успели ответить или не знаете ответа на поставленный вопрос, нажмите на кнопку "Далее".\n\n' \
           f'<b>Вы не сможете вернуться к предыдущим вопросам</b>'


def olymp_text_kz(time):
    return f'Әр сұраққа жауап беруге {time} минут.\n\n' \
           f'Егер сіз жауап беріп үлгермесеңіз немесе жауабын білмесеңіз "Келесі сұраққа көшу" батырмасын басыңыз.\n\n'\
           f'<b>Сіз алдыңғы сұрақтарға кері орала алмайсыз</b>'


def subj_info(callback, bot, subject):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Учавствовать', callback_data=f'p{subject}_ru')
    button_back = InlineKeyboardButton(text='К списку предметов', callback_data=f'Спис {pedagog_ru}')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text(subject, 40, 60, 500),
                     reply_markup=markup_url, parse_mode='html')


def subj_info_kz(callback, bot, subject):
    markup_url = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text='Қатысу', callback_data=f'p{subject}_kz')
    button_back = InlineKeyboardButton(text='Пәндер тізімі', callback_data=f'Спис {pedagog_kz}')

    markup_url.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=text_kz(subject, 40, 60, 500),
                     reply_markup=markup_url, parse_mode='html')


def test_req(callback, bot, subject):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data=f't{subject}_ru')
    button_back = InlineKeyboardButton(text='К списку предметов', callback_data=f'Спис {pedagog_ru}')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('1.5'),
                     reply_markup=markup, parse_mode='html')


def test_req_kz(callback, bot, subject):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data=f't{subject}_kz')
    button_back = InlineKeyboardButton(text='Пәндер тізімі', callback_data=f'Спис {pedagog_kz}')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('1.5'),
                     reply_markup=markup, parse_mode='html')

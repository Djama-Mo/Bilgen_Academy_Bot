from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


sprint_ru = 'Bilgen  Sprint'
sprint_kz = 'Bilgen Sprint'

start_the_test_ru = 'Оплатить и приступить к тесту'
start_the_test_kz = 'Төлеу және тестті бастау'


def olymp_text_ru(time):
    return f'На каждый вопрос отведено {time} минуты.\n\n' \
           f'Если Вы не успели ответить или не знаете ответа на поставленный вопрос, нажмите на кнопку "Далее".\n\n' \
           f'<b>Вы не сможете вернуться к предыдущим вопросам</b>'


def olymp_text_kz(time):
    return f'Әр сұраққа жауап беруге {time} минут.\n\n' \
           f'Егер сіз жауап беріп үлгермесеңіз немесе жауабын білмесеңіз "Келесі сұраққа көшу" батырмасын басыңыз.\n\n' \
           f'<b>Сіз алдыңғы сұрақтарға кері орала алмайсыз</b>'


def sprint_subject_11_ru(callback, bot, subj):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_ru, callback_data=f'spr_{subj}_11_ru')
    button_back = InlineKeyboardButton(text='К списку олимпиад', callback_data=f'Олимпиады 11')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_ru('2'), reply_markup=markup, parse_mode='html')


def sprint_subject_11_kz(callback, bot, subj):
    markup = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text=start_the_test_kz, callback_data=f'spr_{subj}_11_kz')
    button_back = InlineKeyboardButton(text='Олимпиадалар тізімі', callback_data=f'Олимпиады 11kz')

    markup.add(button).add(button_back)

    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    bot.send_message(chat_id=callback.message.chat.id, text=olymp_text_kz('2'), reply_markup=markup, parse_mode='html')

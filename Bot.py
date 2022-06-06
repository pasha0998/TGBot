import telebot;
from telebot import types
bot = telebot.TeleBot('5057614275:AAEInrfAHLHFHMRbK3cWNb2Sow9xIB78pEQ');

name = ""
surname = ""

@bot.message_handler(content_types=['text'])
def start(message):
     if message.text == '/reg':
         bot.send_message(message.from_user.id, "Как тебя зовут?")
         bot.register_next_step_handler(message, reg_name)
     else:
         bot.send_message(message.from_user.id, 'Напиши /reg');

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
    global surname
    surname = message.text

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Тебя зовут: ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text = question, reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Приятно познакомиться, будем дружить!")


def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Приятно познакомиться!")

    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Попробуем еще раз!")
        bot.send_message(call.message.chat.id, "Привет! Давай познакомимся! Как тебя зовут?")
        bot.register_next_step_handler(call.message, reg_name)
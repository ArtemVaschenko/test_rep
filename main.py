import telebot
import config
import random
from telebot import types
q = 0
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welkome(message):
    sti = open(config.stiker, 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Добавить один день")
    item2 = types.KeyboardButton("Отнять один день")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Добро пожаловать мой маленький Уайтбой'.format(message.from_user, bot. get_me()),parse_mode='html', reply_markup=markup)





@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.chat.type == "Добавить один день":
            q += 1
            bot.send_message(message.chat.id, str(q))
        elif message.chat.type == "Отнять один день":
            q -= 1
            bot.send_message(message.chat.id, str(q))
        else:
            bot.send_message(message.chat.id, 'Я не знаю как ответить')

# RUN
bot.polling(none_stop=True)
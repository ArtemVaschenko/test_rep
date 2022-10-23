import telebot
import config


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welkome(message):
    sti = open('/Users/apple/Desktop/astma.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, 'Добро пожаловать мой маленький Уайтбой'.format(message.from_user, bot. get_me()))
    parse_mode='html'
@bot.message_handler(content_types=['text'])

def lalala(message):
    bot.send_message(message.chat.id, message.text)

# RUN
bot.polling(none_stop=True)
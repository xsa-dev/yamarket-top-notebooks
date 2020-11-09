import telebot
import config


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, ты написал мне /start')

    
bot.polling()

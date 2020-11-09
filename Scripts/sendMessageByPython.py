import telebot
import config

tid = config.tid
bot = telebot.TeleBot(config.token)
try:
    bot.send_message(tid, "Ничего не найдено!")
except Exception as e:
    raise e



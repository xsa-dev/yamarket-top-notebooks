import telebot
import config

tid = config.tid
bot = telebot.TeleBot(config.token)

try:
    doc = open('..\Data\yareport.xlsx', 'rb')
    bot.send_document(tid, doc)
except Exception as e:
    raise e

# -*- coding: utf
import telebot # pip install pyTelegramBotAPI

TOKEN = 'ТОКЕН'  # заменить на настоящий токен от BotFather
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть.'.format(name=message.chat.id))

bot.polling()

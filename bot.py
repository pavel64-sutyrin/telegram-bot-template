# -*- coding: utf
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import telebot # pip install pyTelegramBotAPI

TOKEN = '-- INSERT TOKEN HERE --'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    print('< [{0}] "{1}"'.format(message.chat.username, message.text))
    
    msg = 'Привет, {0}, рад тебя видеть!'.format(message.chat.username)
    
    print('> [{0}] "{1}"'.format(message.chat.username, msg))
    bot.send_message(message.chat.id, msg)

print('bot started')
bot.polling()

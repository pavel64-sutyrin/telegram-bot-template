import telebot # pip install pyTelegramBotAPI


TOKEN = '276789777:AAG_-qnSGFRCY2w3zZJByE4zIbo0qDyGrck'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.chat.id))



bot.polling()
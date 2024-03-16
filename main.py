import telebot as tb

token = '7055015230:AAG81S6EgQkZVQaWls2Y3utZrQYYms6Ze7w'

bot = tb.TeleBot(token)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    if message.text == '/start':
        bot.send_message(chat_id=message.chat.id,text='hello world')


if __name__ == '__main__':
    bot.infinity_polling()


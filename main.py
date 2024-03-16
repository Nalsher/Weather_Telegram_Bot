<<<<<<< HEAD
import telebot as tb

token = '7055015230:AAG81S6EgQkZVQaWls2Y3utZrQYYms6Ze7w'

bot = tb.TeleBot(token)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    if message.text == '/start':
        bot.send_message(chat_id=message.chat.id,text='hello world')


if __name__ == '__main__':
    bot.infinity_polling()

=======
import telebot
import requests
def getz():
    r = requests.get('https://www.google.ru/search?q=погода+в+волчихе&newwindow=1&sxsrf=AB5stBi49s--I4dIyE7-nNFdUBtwNcXabQ%3A1688578513817&ei=0amlZJXKMYjMrgSJoY3QDQ&ved=0ahUKEwjV9vaTjfj_AhUIposKHYlQA9oQ4dUDCA4&uact=5&oq=погода+в+волчихе&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzoKCAAQRxDWBBCwA0oECEEYAFBDWENg7wJoAXACeACAAQCIAQCSAQCYAQCgAQHAAQHIAQg&sclient=gws-wiz-serp')
    s = r.text
    temp = ''
    for i in range(len(s)-3):
        if s[i+2] == '°' and s[i+3] == 'C':
            temp = str(s[i] + s[i+1] + s[i+2] + s[i+3])
            break
    return temp
bot = telebot.TeleBot('6374040587:AAGwT2tqqnAsNsfsuEdQjQQss5ehIHrmc2Y')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'<b>Погода в Волчихе</b>',parse_mode='html')
    bot.send_message(message.chat.id,getz(),parse_mode='html')
bot.polling(none_stop=True)
>>>>>>> 58b53dbc20a9fcfc49fa300f118dea4b878315de

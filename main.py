import telebot as tb
from telebot import types
from requestApi import Get_W_Api,Parse_data
from extentionfile import *



token = 'Telegrambottokenexample'

bot = tb.TeleBot(token)

button_for_city = types.InlineKeyboardButton('Указать город',callback_data=None)
button_for_check = types.InlineKeyboardButton('Выбрать последний указанный город',callback_data=None)
button_for_favor = types.InlineKeyboardButton('Выбрать избранный город',callback_data=None)


keyboard = types.ReplyKeyboardMarkup()
keyboard.add(button_for_favor,button_for_city,button_for_check)

@bot.message_handler(content_types = ['text'],commands=['start'])

def start(message):
    bot.send_message(chat_id=message.chat.id, text='Выберите действие', reply_markup=keyboard)
    @bot.message_handler(content_types=['text'])
    def send_welcome(message):
        if message.text == 'Указать город':
            bot.send_message(chat_id=message.chat.id,text="Введите название города")

            @bot.message_handler(func=lambda message: True, content_types=['text'])
            def returnweather(message):
                city = message.text
                weather = Get_W_Api(city)
                weath = Parse_data(weather)
                chek = weath.check()
                if chek == True:
                    redis_work(message.from_user.username, city)
                    temper = weath.Get_Weather_temperature()
                    descrip = weath.Get_Weather_descrip()
                    bot.send_message(chat_id=message.chat.id, text=f'Город : {city}\nПогода : {descrip}\nТемпература : {temper}')
                else:
                    bot.send_message(chat_id=message.chat.id, text='Город не найден')
            bot.register_next_step_handler(message,returnweather)
        if message.text == 'Выбрать последний указанный город':
            rdget = redis_get(message.from_user.username)
            weather = Parse_data(Get_W_Api(rdget))
            chek = weather.check()
            if chek == True:
                temper = weather.Get_Weather_temperature()
                descrip = weather.Get_Weather_descrip()
                bot.send_message(chat_id=message.chat.id,
                                 text=f'Город : {rdget}\nПогода : {descrip}\nТемпература : {temper}')
        if message.text == 'Выбрать избранный город':
            rdget = redis_get('Favour'+message.from_user.username)
            if rdget == 'None':
                raise KeyError
            weather = Parse_data(Get_W_Api(rdget))
            chek = weather.check()
            if chek == True:
                temper = weather.Get_Weather_temperature()
                descrip = weather.Get_Weather_descrip()
                bot.send_message(chat_id=message.chat.id,
                                 text=f'Город : {rdget}\nПогода : {descrip}\nТемпература : {temper}')
    bot.register_next_step_handler(message,send_welcome)

@bot.message_handler(func=lambda message: True,commands=['save'])
def save(message):
    bot.send_message(chat_id=message.chat.id,text = 'Введите название вашего города')
    # print(message.from_user.username)
    @bot.message_handler(func=lambda message: True,content_types=['text'])
    def save_city(message):
        city = message.text
        redis_work('Favour'+message.from_user.username,value=message.text)


if __name__ == '__main__':
    bot.infinity_polling()


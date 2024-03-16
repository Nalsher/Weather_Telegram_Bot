import telebot as tb
from telebot import types
from requestApi import Get_W_Api,Parse_data
from extentionfile import redis_work



token = '7055015230:AAG81S6EgQkZVQaWls2Y3utZrQYYms6Ze7w'

bot = tb.TeleBot(token)

button_for_city = types.InlineKeyboardButton('Указать город',callback_data=None)

keyboard = types.ReplyKeyboardMarkup()
keyboard.add(button_for_city)

@bot.message_handler(commands=['start'])

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
                    temper = weath.Get_Weather_temperature()
                    descrip = weath.Get_Weather_descrip()
                    bot.send_message(chat_id=message.chat.id, text=f'Погода : {descrip}\nТемпература : {temper}')
                    bot.send_message(chat_id=message.chat.id, text=chek)
                else:
                    bot.send_message(chat_id=message.chat.id, text='Город не найден')
            bot.register_next_step_handler(message,returnweather)

@bot.message_handler(func=lambda message: True,commands=['save'])
def save(message):
    bot.send_message(chat_id=message.chat.id,text = 'Введите название вашего города')
    # print(message.from_user.username)
    @bot.message_handler(func=lambda message: True,content_types=['text'])
    def save_city(message):
        city = message.text
        redis_work(message.from_user.username,city)
    bot.register_next_step_handler(message,save_city)
    

if __name__ == '__main__':
    bot.infinity_polling()

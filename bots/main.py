import telebot
from telebot import types

bot = telebot.TeleBot('5922283398:AAEcy9RMJRfJ7iwXZSz_TZYq_sRh2wwxZ-Y')

@bot.message_handler(commands = ['start'])
def start(message):
    mess = f'Лол чел ты = <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode = 'html')


@bot.message_handler(commands =['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить вебсайт", url = "https://youtube.com"))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

@bot.message_handler(commands =['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
    website = types.KeyboardButton('/website')
    start = types.KeyboardButton('/start')
    help1 = types.KeyboardButton('/help')
    markup.add(website, start, help1)
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if (message.text=='Hello' or message.text=='Привет' or message.text=='Hi')   :
        mess = f'Дарова, {message.from_user.username}'
        bot.send_message(message.chat.id, mess, parse_mode = 'html')
    elif (message.text=='id')   :
        mess = f'Your id is, {message.from_user.id}'
        bot.send_message(message.chat.id, mess, parse_mode = 'html')
    elif (message.text=='photo') :
        photic = open('the-rock-sus.gif', 'rb')
        bot.send_photo(message.chat.id, photic)
    else: 
        bot.send_message(message.chat.id, 'Не пон', parse_mode = 'html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Very cool photo')



bot.polling(none_stop=True)
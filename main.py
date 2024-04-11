import telebot
from telebot import types
from Bot_token import token
import json

bot = telebot.TeleBot(token)
# Processing Data from a Database

a = "  "
Bachelor = list()
Master = list()
Postgraduate = list()
with open('base.json') as f:
    templates = json.load(f)

# a = templates[0]["question"][0]["На какой уровень образваония вы планируете поступать?"]["Бакалавриат"]

Bachelor.append(templates[0]["question"][0]["На какой уровень образваония вы планируете поступать?"]["Бакалавриат"])
Master.append(templates[0]["question"][0]["На какой уровень образваония вы планируете поступать?"]["Магистратура"])
Postgraduate.append(templates[0]["question"][0]["На какой уровень образваония вы планируете поступать?"]["Аспирантура"])
print(Bachelor[0], Master[0], Postgraduate[0])
for i in templates[0]["question"][0]["Бакалавриат"]:
    Bachelor.append(i)

for i in templates[0]["question"][0]["Магистратура"]:
    Master.append(i)

for i in templates[0]["question"][0]["Аспирантура"]:
    Postgraduate.append(i)


# TEGRAM BOT
@bot.message_handler(commands=['help', 'start'])
def greet(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Бакалавриат", callback_data="Бакалавриат"))
    markup.add(types.InlineKeyboardButton("Магистратура", callback_data="Магистратура"))
    markup.add(types.InlineKeyboardButton("Аспирантура", callback_data="Аспирантура"))
    bot.reply_to(message, """Здравствуйте! Вы попали на бота поддержки СурГПУ.
В этом боте вы сможете узнать основную информацию для поступления. 
На какой уровень образования вы хотите поступить?""", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback_data: True)
def education_lvl(callback):
    markup = types.InlineKeyboardMarkup()
    if callback.data == "Бакалавриат":
        markup.add(types.InlineKeyboardButton(Bachelor[1], callback_data="Математика и Информатика"))
        markup.add(types.InlineKeyboardButton(Bachelor[2], callback_data="Математика и Физика"))
        bot.edit_message_text(f"""Прекрасный выбор! {Bachelor[0]}. 
Выберите направление: """, callback.message.chat.id, callback.message.message_id, reply_markup=markup)
    if callback.data == "Магистратура":
        markup.add(types.InlineKeyboardButton(Master[1],
                                              callback_data="Цифровизация"))
        bot.edit_message_text(f"""Прекрасный выбор! {Master[0]} 
Выберите направление: """, callback.message.chat.id, callback.message.message_id, reply_markup=markup)
    if callback.data == "Аспирантура":
        markup.add(types.InlineKeyboardButton(Postgraduate[1],
                                              callback_data="Проф. обр"))
        markup.add(types.InlineKeyboardButton(Postgraduate[2],
                                              callback_data="Педагогика"))
        bot.edit_message_text(f"""Прекрасный выбор! {Postgraduate[0]} 
Выберите направление: """, callback.message.chat.id, callback.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda callback_data: True)
def programm(callback):
    if callback.data == "Педагогика":
        bot.edit_message_text("Hi", callback.message.chat.id, callback.message.message_id)


def hi():
    pass


bot.infinity_polling()

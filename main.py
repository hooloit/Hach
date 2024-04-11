import telebot
from telebot import types
from Bot_token import token

bot = telebot.TeleBot(token)


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
        markup.add(types.InlineKeyboardButton("Математика и Информатика", callback_data="Математика и Информатика"))
        markup.add(types.InlineKeyboardButton("Математика и Физика", callback_data="Математика и Физика"))
        bot.edit_message_text("""Прекрасный выбор! Подача документов будет возможна до 7 июля. 
Выберите направление: """, callback.message.chat.id, callback.message.message_id, reply_markup=markup)
    if callback.data == "Магистратура":
        markup.add(types.InlineKeyboardButton("Цифровизация образования: проектирование, сопровождение, экспертиза",
                                              callback_data="Цифровизация"))
        bot.edit_message_text("""Прекрасный выбор! Подача документов будет возможна до 22 августа. 
Выберите направление: """, callback.message.chat.id, callback.message.message_id, reply_markup=markup)
    if callback.data == "Аспирантура":
        markup.add(types.InlineKeyboardButton("Методология и технология профессионального образования",
                                              callback_data="Проф. обр"))
        markup.add(types.InlineKeyboardButton("Общая педагогика, история педагогики и образования",
                                              callback_data="Педагогика"))
        bot.edit_message_text("""Прекрасный выбор! Подача документов будет возможна до 20 августа. 
Выберите направление: """, callback.message.chat.id, callback.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda callback_data: True)
def programm(callback):
    if callback.data == "Педагогика":
        bot.edit_message_text("Hi", callback.message.chat.id, callback.message.message_id)


def hi():
    pass


bot.infinity_polling()

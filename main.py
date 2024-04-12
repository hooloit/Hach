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
with open('base.json', encoding="utf-8") as f:
    templates = json.load(f)

last_callback = ""

# a = templates[0]["question"][0]["На какой уровень образования вы планируете поступать?"]["Бакалавриат"]

Bachelor.append(templates[0]["question"][0]["На какой уровень образования вы планируете поступать?"]["Бакалавриат"])
Master.append(templates[0]["question"][0]["На какой уровень образования вы планируете поступать?"]["Магистратура"])
Postgraduate.append(templates[0]["question"][0]["На какой уровень образования вы планируете поступать?"]["Аспирантура"])
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
    Bachelor = types.InlineKeyboardButton("Бакалавриат", callback_data="Бакалавриат")
    Master = types.InlineKeyboardButton("Магистратура", callback_data="Магистратура")
    Postgraduate = types.InlineKeyboardButton("Аспирантура", callback_data="Аспирантура")
    markup.add(Bachelor, Master, Postgraduate)
    bot.send_message(message.chat.id, """Здравствуйте! Вы попали на бота поддержки СурГПУ.
В этом боте вы сможете узнать основную информацию для поступления. 
На какой уровень образования вы хотите поступить?""", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback_data: True)
def education_lvl(callback):
    markup = types.InlineKeyboardMarkup()
    back = types.InlineKeyboardButton("Назад", callback_data="back")
    back_to_lvl = types.InlineKeyboardButton("Назад", callback_data="back_to_lvl")
    if callback.data == "Бакалавриат":
<<<<<<< HEAD
        markup.add(types.InlineKeyboardButton(Bachelor[1], callback_data="Математика и Информатика"))
        markup.add(types.InlineKeyboardButton(Bachelor[2], callback_data="Математика и Физика"))
        bot.edit_message_text(f"""Прекрасный выбор! {Bachelor[0]}. 
=======
        MI = types.InlineKeyboardButton(Bachelor[1], callback_data="Математика и Информатика")
        MP = types.InlineKeyboardButton(Bachelor[2], callback_data="Математика и Физика")
        markup.add(MI, MP)
        markup.add(back)
        bot.edit_message_text(f"""Вы выбрали уровень: бакалавриат. {Bachelor[0]}. 
>>>>>>> b88cdea85fdd6eb0040a4ca3fe4159a4a7ce4657
Выберите направление: """, callback.from_user.id, callback.message.message_id, reply_markup=markup)
    if callback.data == "Магистратура":
        back_to_lvl = types.InlineKeyboardButton("Назад", callback_data="Магистратура")
        markup.add(types.InlineKeyboardButton(Master[1],
                                              callback_data="Цифровизация"))
        bot.edit_message_text(f"""Прекрасный выбор! {Master[0]} 
Выберите направление: """, callback.from_user.id, callback.message.message_id, reply_markup=markup)
    if callback.data == "Аспирантура":
        back_to_lvl = types.InlineKeyboardButton("Назад", callback_data="Аспирантура")
        markup.add(types.InlineKeyboardButton(Postgraduate[1],
                                              callback_data="Проф. обр"))
        markup.add(types.InlineKeyboardButton(Postgraduate[2],
                                              callback_data="Педагогика"))
        bot.edit_message_text(f"""Прекрасный выбор! {Postgraduate[0]} 
Выберите направление: """, callback.from_user.id, callback.message.message_id, reply_markup=markup)
        bot.register_next_step_handler(callback, program)

    if callback.data == "Математика и Физика":
        markup.add(back_to_lvl)
        bot.edit_message_text("""Вступительные испытания:
– Русский язык (ЕГЭ, не менее 40 баллов)
– Математика (ЕГЭ, не менее 39 баллов)
– Физика
Более подробная информация:
https://www.surgpu.ru/Abitur/bachelor/""", callback.from_user.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Цифровизация":
        markup.add(back_to_lvl)
        bot.edit_message_text("""Вступительное испытание – Профильный
междисциплинарный экзамен (устно)
Более подробная информация:
https://www.surgpu.ru/Abitur/magistratura/""", callback.from_user.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Проф. обр":
        markup.add(back_to_lvl)
        bot.edit_message_text("""– Специальная дисциплина, соответствующая
направленности (профилю) программы
подготовки научно-педагогических кадров в
аспирантуре
– Философия
– Иностранный язык
Более подробная информация:
https://www.surgpu.ru/Abitur/aspirantura/""", callback.from_user.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Педагогика":
        bot.edit_message_text("Hi", callback.from_user.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "back":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        greet(callback.message)

def aaaa():
    pass
bot.infinity_polling()

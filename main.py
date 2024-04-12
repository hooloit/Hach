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

Faculty_Bachelor = [['a'] * 4 for i in range(2)]

Faculty_Master = [['a'] * 2 for i in range(2)]

Faculty_Postgraduate = [['a'] * 6 for i in range(2)]

for i in range(2):
    for j in range(4): 
        Faculty_Bachelor[i][j] = templates[0]["question"][0]["Бакалавриат"][Bachelor[i + 1]][j]

for i in range(2):
    for j in range(2): 
        Faculty_Master[i][j] = templates[0]["question"][0]["Магистратура"][Master[1]][j]

for i in range(2):
    for j in range(6): 
        Faculty_Postgraduate[i][j] = templates[0]["question"][0]["Аспирантура"][Postgraduate[i + 1]][j]



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
    global save
    markup = types.InlineKeyboardMarkup()
    back = types.InlineKeyboardButton("Назад", callback_data="back")
    back_to_lvl = types.InlineKeyboardButton("Назад", callback_data="back_to_lvl")
    if callback.data == "Бакалавриат":
        save = "Бакалавриат"
        MI = types.InlineKeyboardButton(Bachelor[1], callback_data="Математика и Информатика")
        MP = types.InlineKeyboardButton(Bachelor[2], callback_data="Математика и Физика")
        markup.add(MI, MP)
        markup.add(back)
        bot.edit_message_text(f"""Вы выбрали уровень: бакалавриат. {Bachelor[0]}
Выберите направление: """, callback.from_user.id, callback.message.message_id, reply_markup=markup)
    if callback.data == "Магистратура":
        save = "Магистратура"
        DIG = types.InlineKeyboardButton(Master[1],
                                         callback_data="Цифровизация")
        markup.add(DIG)
        markup.add(back)
        bot.edit_message_text(f"""Вы выбрали уровень: магистратура {Master[0]} 
Выберите направление: """, callback.from_user.id, callback.message.message_id, reply_markup=markup)
    if callback.data == "Аспирантура":
        save = "Аспирантура"
        PE = types.InlineKeyboardButton(Postgraduate[1],
                                              callback_data="Проф. обр")
        Pedag = types.InlineKeyboardButton(Postgraduate[2],
                                              callback_data="Педагогика")
        markup.add(PE)
        markup.add(Pedag)
        markup.add(back)
        bot.edit_message_text(f"""Вы выбрали уровень: аспирантура {Postgraduate[0]} 
Выберите направление: """, callback.from_user.id, callback.message.message_id, reply_markup=markup)
        bot.register_next_step_handler(callback)

    if callback.data == "Математика и Информатика":
        bot.edit_message_text(f"""{Faculty_Bachelor[0][0]}
{Faculty_Bachelor[0][1]}
{Faculty_Bachelor[0][2]}
{Faculty_Bachelor[0][3]}
Более подробная информация:
https://www.surgpu.ru/Abitur/bachelor/""", callback.from_user.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Математика и Физика":
        markup.add(back_to_lvl)
        bot.edit_message_text(f"""{Faculty_Bachelor[1][0]}
{Faculty_Bachelor[1][1]}
{Faculty_Bachelor[1][2]}
{Faculty_Bachelor[1][3]}
Более подробная информация:
https://www.surgpu.ru/Abitur/bachelor/""", callback.from_user.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Цифровизация":
        markup.add(back_to_lvl)
        bot.edit_message_text(f"""{Faculty_Master[0][0]}
{Faculty_Master[0][1]}
Более подробная информация:
https://www.surgpu.ru/Abitur/magistratura/""", callback.from_user.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Проф. обр":
        markup.add(back_to_lvl)
        bot.edit_message_text(f"""{Faculty_Postgraduate[0][0]}
{Faculty_Postgraduate[0][1]}
{Faculty_Postgraduate[0][2]}
{Faculty_Postgraduate[0][3]}
{Faculty_Postgraduate[0][4]}
{Faculty_Postgraduate[0][5]}
Более подробная информация:
https://www.surgpu.ru/Abitur/aspirantura/""", callback.from_user.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Педагогика":
        bot.edit_message_text(f"""{Faculty_Postgraduate[1][0]}
{Faculty_Postgraduate[1][1]}
{Faculty_Postgraduate[1][2]}
{Faculty_Postgraduate[1][3]}
{Faculty_Postgraduate[1][4]}
{Faculty_Postgraduate[1][5]}
Более подробная информация
https://www.surgpu.ru/Abitur/aspirantura/""", callback.from_user.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "back":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        greet(callback.message)

    if callback.data == "back_to_lvl":
        callback.data = save
        education_lvl(callback)
bot.infinity_polling()

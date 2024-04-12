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
    site = types.InlineKeyboardButton("Наш сайт", url="https://www.surgpu.ru/")
    nonresident = types.InlineKeyboardButton("Информация для иногородних", callback_data="Иногородний")
    Bachelor = types.InlineKeyboardButton("Бакалавриат", callback_data="Бакалавриат")
    Master = types.InlineKeyboardButton("Магистратура", callback_data="Магистратура")
    Postgraduate = types.InlineKeyboardButton("Аспирантура", callback_data="Аспирантура")
    markup.add(Bachelor, Master, Postgraduate)
    markup.add(nonresident)
    markup.add(site)

    bot.send_message(message.chat.id, """Здравствуйте! Вы попали на бота поддержки СурГПУ. В этом боте вы сможете узнать основную информацию для поступления. 
На какой уровень образования вы хотите поступить?""", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback_data: True)
def education_lvl(callback):
    global save
    global save_to_vector
    markup = types.InlineKeyboardMarkup()
    back = types.InlineKeyboardButton("Назад", callback_data="back")
    back_to_lvl = types.InlineKeyboardButton("Назад", callback_data="back_to_lvl")
    back_to_vector = types.InlineKeyboardButton("Назад", callback_data="back_to_vector")
    # УРОВНИ ОБРАЗОВАНИЯ
    if callback.data == "Бакалавриат":
        save = callback.data
        FK = types.InlineKeyboardButton("Факультет физ. культуры и спорта", callback_data="Физра")
        PED = types.InlineKeyboardButton("Факультет социально-педагогический", callback_data="Педагог")
        markup.add(FK)
        markup.add(PED)
        markup.add(back)
        bot.edit_message_text(f"""Вы выбрали уровень: бакалавриат. {Bachelor[0]}
Выберите факультет: """, callback.from_user.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Магистратура":
        save = callback.data
        PP = types.InlineKeyboardButton("Педагогика и психология", callback_data="Психол-пед")
        SOC = types.InlineKeyboardButton("Социально-педагог", callback_data="Соц-пед")
        markup.add(PP, SOC)
        markup.add(back)
        bot.edit_message_text(f"""Вы выбрали уровень: магистратура {Master[0]} 
Выберите факультет: """, callback.from_user.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Аспирантура":
        save = callback.data
        PSIX = types.InlineKeyboardButton("Педагогическая психология, психодиагностика цифровых образовательных сред",
                                          callback_data="Педаг-псих")
        SOC = types.InlineKeyboardButton("Социальная структура, социальные институты и процессы",
                                         callback_data="Соц. стр")
        FKP = types.InlineKeyboardButton("Физическая культура и профессиональная физическая подготовк",
                                         callback_data="Физ.под")
        GEN = types.InlineKeyboardButton("Общая педагогика, история педагогики и образования",
                                         callback_data="Общ. пед")
        markup.add(PSIX)
        markup.add(SOC)
        markup.add(FKP)
        markup.add(GEN)
        markup.add(back)
        bot.edit_message_text(f"""Вы выбрали уровень: аспирантура {Postgraduate[0]} 
Выберите направление: """, callback.from_user.id, callback.message.message_id, reply_markup=markup)

    # НАПРАВЛЕННОСТИ
    if callback.data == "Физра":  # БАКАЛАВРИАТ
        save_to_vector=callback.data
        OBJ = types.InlineKeyboardButton("ОБЖ и физ. культура",
                                         callback_data="Обж")
        AF = types.InlineKeyboardButton("Адаптивная физ.культура",
                                        callback_data="Адап. физ")
        BIO = types.InlineKeyboardButton("Биология и география",
                                         callback_data="Биология")
        FK = types.InlineKeyboardButton("Физкультурно-оздоровительная деятельность",
                                        callback_data="Оздар.")
        markup.add(OBJ)
        markup.add(AF)
        markup.add(BIO)
        markup.add(FK)
        markup.add(back_to_lvl)
        bot.edit_message_text("""Выберите направление:
- Основы безопасности жизнедеятельности и физ. культура
- Адаптивная физическая культура
- Биология и география
- Физкультурно-оздоровительная деятельность""", callback.from_user.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Педагог":  # БАКАЛАВРИАТ
        save_to_vector=callback.data

        MF = types.InlineKeyboardButton("МатФиз",
                                        callback_data="МатФиз")
        MI = types.InlineKeyboardButton("МатИнф",
                                        callback_data="МатИнф")
        SOCW = types.InlineKeyboardButton("Соц. работа",
                                          callback_data="соцраб")
        MANAG = types.InlineKeyboardButton("Менеджмент",
                                           callback_data="Менеджмент")
        markup.add(SOCW)
        markup.add(MI)
        markup.add(MF)
        markup.add(MANAG)
        markup.add(back_to_lvl)
        bot.edit_message_text("""Выберите направление:
"- Технологии социальной работы в различных сферах жизнедеятельности",
"- Математика и информатика",
"- Математика и физика",
"- Менеджмент социально-культурной деятельности"
    """, callback.from_user.id, callback.message.message_id,
                              reply_markup=markup)

    if callback.data == "Соц-пед":  # МАГИСТРАТУРА
        save_to_vector=callback.data
        FK = types.InlineKeyboardButton("Физра",
                                        callback_data="Физ. педагог")
        QUALT = types.InlineKeyboardButton("Качество",
                                           callback_data="Качеств")
        MAL = types.InlineKeyboardButton("Дошкольное",
                                         callback_data="Дошкольное")
        MANAG = types.InlineKeyboardButton("Управление",
                                           callback_data="Управ")
        markup.add(FK, QUALT)
        markup.add(MAL, MANAG)
        markup.add(back_to_lvl)
        bot.edit_message_text("""Выберите направление: 
    "Образование в области физической культуры и спорта",
    "Управление качеством образовательного процесса в начальной школе",
    "Менеджмент в дошкольном образовании",
    "Управление воспитательными системами в образовательных организациях""", callback.from_user.id,
                              callback.message.message_id,
                              reply_markup=markup)

    if callback.data == "Психол-пед":  # МАГИСТРАТУРА
        save_to_vector = callback.data
        DEV = types.InlineKeyboardButton("Развитие",
                                         callback_data="Развитие")
        DIG = types.InlineKeyboardButton("Цифровизация",
                                         callback_data="Цифра")
        markup.add(DEV)
        markup.add(DIG)
        markup.add(back_to_lvl)
        bot.edit_message_text("""
"- Развитие личностного потенциала в образовании: персонализация и цифровизация",
"- Цифровизация образования: проектирование, сопровождение, экспертиза"
""", callback.from_user.id,
                              callback.message.message_id,
                              reply_markup=markup)

    if callback.data == "Иногородний":
        markup.add(back)
        bot.edit_message_text(
            """В распоряжении Сургутского государственного педагогического Университета имеются два благоустроенных студенческих общежития квартирного типа. Количество мест для иногородних поступающих - 100.""",
            callback.message.chat.id,
            callback.message.message_id, reply_markup=markup)

    if callback.data == "back":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        greet(callback.message)

    if callback.data == "back_to_lvl":
        callback.data = save
        education_lvl(callback)

    if callback.data == "back_to_vector":
        callback.data = save_to_vector
        education_lvl(callback)

    # ------------------------------------------------------------------------------- Бакалавриат(1)
    if callback.data == "Обж":
        markup.add(back_to_vector)
        bot.edit_message_text("""На базе среднего общего образования:
- Русский язык (ЕГЭ)- 40
- Обществознание (ЕГЭ) - 42
- Профессиональное испытание - 50
https://www.surgpu.ru/Abitur/bachelor/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Адап. физ":
        markup.add(back_to_vector)
        bot.edit_message_text("""На базе среднего общего образования:
Русский язык (ЕГЭ) - 40
Обществознание (ЕГЭ) – 42 / Математика (ЕГЭ) - 39
Профессиональное испытание - 50
https://www.surgpu.ru/Abitur/bachelor/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Биология":
        markup.add(back_to_vector)
        bot.edit_message_text("""На базе среднего общего образования:
Русский язык (ЕГЭ) - 40
Обществознание (ЕГЭ) - 42
Биология и география - 40
https://www.surgpu.ru/Abitur/bachelor/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Оздар.":
        markup.add(back_to_vector)
        bot.edit_message_text("""На базе среднего общего образования:
Русский язык (ЕГЭ)- 40
Обществознание (ЕГЭ) - 42 / Математика (ЕГЭ) - 39
Профессиональное испытание - 50
https://www.surgpu.ru/Abitur/bachelor/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)
# ---------------------------------------------------------------------------------------------- Бакалавриат(2)
    if callback.data == "МатФиз":
        markup.add(back_to_vector)
        bot.edit_message_text("""На базе среднего общего образования:
Математика (ЕГЭ) - 39
Русский язык (ЕГЭ) - 40
Профессиональное испытание - 40
https://www.surgpu.ru/Abitur/bachelor/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "МатИнф":
        markup.add(back_to_vector)
        bot.edit_message_text("""На базе среднего общего образования:
Математика (ЕГЭ) - 39
Русский язык (ЕГЭ) - 40
Профессиональное испытание - 42
https://www.surgpu.ru/Abitur/bachelor/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "соцраб":
        markup.add(back_to_vector)
        bot.edit_message_text("""На базе среднего общего образования:
Русский язык (ЕГЭ) - 40
История (ЕГЭ) - 35
Обществознание (ЕГЭ) - 42 / Литература (ЕГЭ) - 40
https://www.surgpu.ru/Abitur/bachelor/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Менеджмент":
        markup.add(back_to_vector)
        bot.edit_message_text("""На базе среднего общего образования:
Русский язык (ЕГЭ) - 40
Литература (ЕГЭ) - 40
Обществознание (ЕГЭ) - 42 / История (ЕГЭ)- 35
https://www.surgpu.ru/Abitur/bachelor/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)
#-------------------------------------------------------------------------------------------------------- Магистратура(1)
    if callback.data == "Физ. педагог":
        markup.add(back_to_vector)
        bot.edit_message_text("""Вступительное испытание – Профильный
междисциплинарный экзамен (устно)
Более подробная информация:
https://www.surgpu.ru/Abitur/magistratura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Качеств":
        markup.add(back_to_vector)
        bot.edit_message_text("""Вступительное испытание – Профильный
междисциплинарный экзамен (устно)
Более подробная информация:
https://www.surgpu.ru/Abitur/magistratura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Дошкольное":
        markup.add(back_to_vector)
        bot.edit_message_text("""Вступительное испытание – Профильный
междисциплинарный экзамен (устно)
Более подробная информация:
https://www.surgpu.ru/Abitur/magistratura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Управ":
        markup.add(back_to_vector)
        bot.edit_message_text("""Вступительное испытание – Профильный
междисциплинарный экзамен (устно)
Более подробная информация:
https://www.surgpu.ru/Abitur/magistratura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)
#----------------------------------------------------------------------------------------------------Магистратура(2)
    if callback.data == "Развитие":
        markup.add(back_to_vector)
        bot.edit_message_text("""Вступительное испытание – Профильный
междисциплинарный экзамен (устно)
Более подробная информация:
https://www.surgpu.ru/Abitur/magistratura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Цифра":
        markup.add(back_to_vector)
        bot.edit_message_text("""Вступительное испытание – Профильный
междисциплинарный экзамен (устно)
Более подробная информация:
https://www.surgpu.ru/Abitur/magistratura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)
#-----------------------------------------------------------------------------------------------------Аспирантура
    if callback.data == "Педаг-псих":
        markup.add(back_to_vector)
        bot.edit_message_text("""– Специальная дисциплина, соответствующая
направленности (профилю) программы
подготовки научно-педагогических кадров в
аспирантуре
– Философия
– Иностранный язык
Более подробная информация:
https://www.surgpu.ru/Abitur/aspirantura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Соц.стр":
        markup.add(back_to_vector)
        bot.edit_message_text("""– Специальная дисциплина, соответствующая
направленности (профилю) программы
подготовки научно-педагогических кадров в
аспирантуре
– Философия
– Иностранный язык
Более подробная информация:
https://www.surgpu.ru/Abitur/aspirantura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Физ.под":
        markup.add(back_to_vector)
        bot.edit_message_text("""– Специальная дисциплина, соответствующая
направленности (профилю) программы
подготовки научно-педагогических кадров в
аспирантуре
– Философия
– Иностранный язык
Более подробная информация:
https://www.surgpu.ru/Abitur/aspirantura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Общ.пед":
        markup.add(back_to_vector)
        bot.edit_message_text("""– Специальная дисциплина, соответствующая
направленности (профилю) программы
подготовки научно-педагогических кадров в
аспирантуре
– Философия
– Иностранный язык
Более подробная информация:
https://www.surgpu.ru/Abitur/aspirantura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    # ------------------------------------------------------------------------------- Бакалавриат(1)
    if callback.data == "Обж":
        markup.add(back_to_vector)
        bot.edit_message_text("""На базе среднего общего образования:
- Русский язык (ЕГЭ)- 40
- Обществознание (ЕГЭ) - 42
- Профессиональное испытание - 50
https://www.surgpu.ru/Abitur/bachelor/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Адап. физ":
        markup.add(back_to_vector)
        bot.edit_message_text("""На базе среднего общего образования:
Русский язык (ЕГЭ) - 40
Обществознание (ЕГЭ) – 42 / Математика (ЕГЭ) - 39
Профессиональное испытание - 50
https://www.surgpu.ru/Abitur/bachelor/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Биология":
        markup.add(back_to_vector)
        bot.edit_message_text("""На базе среднего общего образования:
Русский язык (ЕГЭ) - 40
Обществознание (ЕГЭ) - 42
Биология и география - 40
https://www.surgpu.ru/Abitur/bachelor/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Оздар.":
        markup.add(back_to_vector)
        bot.edit_message_text("""На базе среднего общего образования:
Русский язык (ЕГЭ)- 40
Обществознание (ЕГЭ) - 42 / Математика (ЕГЭ) - 39
Профессиональное испытание - 50
https://www.surgpu.ru/Abitur/bachelor/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)
# ---------------------------------------------------------------------------------------------- Бакалавриат(2)
    if callback.data == "МатФиз":
        markup.add(back_to_vector)
        bot.edit_message_text("""На базе среднего общего образования:
Математика (ЕГЭ) - 39
Русский язык (ЕГЭ) - 40
Профессиональное испытание - 40
https://www.surgpu.ru/Abitur/bachelor/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "МатИнф":
        markup.add(back_to_vector)
        bot.edit_message_text("""На базе среднего общего образования:
Математика (ЕГЭ) - 39
Русский язык (ЕГЭ) - 40
Профессиональное испытание - 42
https://www.surgpu.ru/Abitur/bachelor/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "соцраб":
        markup.add(back_to_vector)
        bot.edit_message_text("""На базе среднего общего образования:
Русский язык (ЕГЭ) - 40
История (ЕГЭ) - 35
Обществознание (ЕГЭ) - 42 / Литература (ЕГЭ) - 40
https://www.surgpu.ru/Abitur/bachelor/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Менеджмент":
        markup.add(back_to_vector)
        bot.edit_message_text("""На базе среднего общего образования:
Русский язык (ЕГЭ) - 40
Литература (ЕГЭ) - 40
Обществознание (ЕГЭ) - 42 / История (ЕГЭ)- 35
https://www.surgpu.ru/Abitur/bachelor/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)
#-------------------------------------------------------------------------------------------------------- Магистратура(1)
    if callback.data == "Физ. педагог":
        markup.add(back_to_vector)
        bot.edit_message_text("""Вступительное испытание – Профильный
междисциплинарный экзамен (устно)
Более подробная информация:
https://www.surgpu.ru/Abitur/magistratura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Качеств":
        markup.add(back_to_vector)
        bot.edit_message_text("""Вступительное испытание – Профильный
междисциплинарный экзамен (устно)
Более подробная информация:
https://www.surgpu.ru/Abitur/magistratura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Дошкольное":
        markup.add(back_to_vector)
        bot.edit_message_text("""Вступительное испытание – Профильный
междисциплинарный экзамен (устно)
Более подробная информация:
https://www.surgpu.ru/Abitur/magistratura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Управ":
        markup.add(back_to_vector)
        bot.edit_message_text("""Вступительное испытание – Профильный
междисциплинарный экзамен (устно)
Более подробная информация:
https://www.surgpu.ru/Abitur/magistratura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)
#----------------------------------------------------------------------------------------------------Магистратура(2)
    if callback.data == "Развитие":
        markup.add(back_to_vector)
        bot.edit_message_text("""Вступительное испытание – Профильный
междисциплинарный экзамен (устно)
Более подробная информация:
https://www.surgpu.ru/Abitur/magistratura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Цифра":
        markup.add(back_to_vector)
        bot.edit_message_text("""Вступительное испытание – Профильный
междисциплинарный экзамен (устно)
Более подробная информация:
https://www.surgpu.ru/Abitur/magistratura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)
#-----------------------------------------------------------------------------------------------------Аспирантура
    if callback.data == "Педаг-псих":
        markup.add(back_to_vector)
        bot.edit_message_text("""– Специальная дисциплина, соответствующая
направленности (профилю) программы
подготовки научно-педагогических кадров в
аспирантуре
– Философия
– Иностранный язык
Более подробная информация:
https://www.surgpu.ru/Abitur/aspirantura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Соц.стр":
        markup.add(back_to_vector)
        bot.edit_message_text("""– Специальная дисциплина, соответствующая
направленности (профилю) программы
подготовки научно-педагогических кадров в
аспирантуре
– Философия
– Иностранный язык
Более подробная информация:
https://www.surgpu.ru/Abitur/aspirantura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Физ.под":
        markup.add(back_to_vector)
        bot.edit_message_text("""– Специальная дисциплина, соответствующая
направленности (профилю) программы
подготовки научно-педагогических кадров в
аспирантуре
– Философия
– Иностранный язык
Более подробная информация:
https://www.surgpu.ru/Abitur/aspirantura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "Общ.пед":
        markup.add(back_to_vector)
        bot.edit_message_text("""– Специальная дисциплина, соответствующая
направленности (профилю) программы
подготовки научно-педагогических кадров в
аспирантуре
– Философия
– Иностранный язык
Более подробная информация:
https://www.surgpu.ru/Abitur/aspirantura/""", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

bot.infinity_polling()
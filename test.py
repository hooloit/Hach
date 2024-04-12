import json
a = "  "
count = 0
count2 = 4
Bachelor = list()
Master = list()
Postgraduate = list()
with open('base.json') as f:
    templates = json.load(f)

Bachelor.append(templates[0]["question"][0]["На какой уровень образования вы планируете поступать?"]["Бакалавриат"])
Master.append(templates[0]["question"][0]["На какой уровень образования вы планируете поступать?"]["Магистратура"])
Postgraduate.append(templates[0]["question"][0]["На какой уровень образования вы планируете поступать?"]["Аспирантура"])
for i in templates[0]["question"][0]["Бакалавриат"]:
    Bachelor.append(i)

for i in templates[0]["question"][0]["Магистратура"]:
    Master.append(i)

for i in templates[0]["question"][0]["Аспирантура"]:
    Postgraduate.append(i)

a = templates[0]["question"][0]["Бакалавриат"][Bachelor[1]][0]
print(a)


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


for i in range(6):
     print(*Faculty_Postgraduate[0][i], "\n")
# print(*Faculty_Bachelor)
    

# print(Faculty_Postgraduate)
# for i in templates[0]["question"][0]["На какой уровень образваония вы планируете поступать?"]["Бакалавриат"]:
#     print(i)
# Bachelor.append(templates[0]["question"][0]["На какой уровень образваония вы планируете поступать?"]["Бакалавриат"])
# Master.append(templates[0]["question"][0]["На какой уровень образваония вы планируете поступать?"]["Магистратура"])
# Postgraduate.append(templates[0]["question"][0]["На какой уровень образваония вы планируете поступать?"]["Аспирантура"])
# print(Bachelor[0], Master[0], Postgraduate[0])
# for i in templates[0]["question"][0]["Бакалавриат"]:

#     Bachelor.append(i)

# for i in templates[0]["question"][0]["Магистратура"]:
#     Master.append(i)

# for i in templates[0]["question"][0]["Аспирантура"]:
#     Postgraduate.append(i)


#F{{{{{}}}}}
# for i in templates[0]["question"][0]["Бакалавриат"]:
#     Bachelor.append(i)

# for i in templates[0]["question"][0]["Магистратура"]:
#     Master.append(i)

# for i in templates[0]["question"][0]["Аспирантура"]:
#     Postgraduate.append(i)

# print(*Bachelor, "\n", *Master, "\n", *Postgraduate)

# print(templates)




# for section, commands in templates.items():
#     print(section)
#     print('\n'.join(commands))
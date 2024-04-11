import json
a = "  "
Bachelor = list()
Master = list()
Postgraduate = list()
with open('base.json') as f:
    templates = json.load(f)

a = templates[0]["question"][0]["На какой уровень образваония вы планируете поступать?"]["Бакалавриат"]
# for i in templates[0]["question"][0]["На какой уровень образваония вы планируете поступать?"]["Бакалавриат"]:
#     print(i)
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


print(*Bachelor, "\n", *Master, "\n", *Postgraduate)

# print(templates)




# for section, commands in templates.items():
#     print(section)
#     print('\n'.join(commands))
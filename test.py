import json
a = "  "
Faculty_Bachelor = list()
Faculty_Master = list()
Speciality_Postgraduate = list()

Directions_Bachelor = [['a'] * 4 for i in range(2)]
Directions_Master = [[' '] * 4 for i in range(2)]

with open('testbd.json') as f:
    templates = json.load(f)


#Факультеты
for i in templates[0]["main"][0]["Бакалавриат"]:
    Faculty_Bachelor.append(i)

for i in templates[0]["main"][0]["Магистратура"]:
    Faculty_Master.append(i)

for i in templates[0]["main"][0]["Аспирантура"]:
    Speciality_Postgraduate.append(i)

# print(*Faculty_Postgraduate)


#Направления
for i in range(2):
    for j in range(4):
        Directions_Bachelor[i][j] = templates[0]["main"][0]["Бакалавриат"][Faculty_Bachelor[i]][j]

print(Directions_Bachelor)

for i in range(2):
    for j in range(4):
        if Faculty_Master[i] == "Факультет психологии и педагогики":
            j + 2
            Directions_Master[i][j] = templates[0]["main"][0]["Магистратура"][Faculty_Master[i]][j]
            if j == 0:
                break
        else:
            Directions_Master[i][j] = templates[0]["main"][0]["Магистратура"][Faculty_Master[i]][j]
a = templates[0]["main"][0]["Магистратура"][Faculty_Master[i]][j]
print(*a)
# for i in range(2):
#     for j in range(4):
#         Directions_Postgraduate[i][j] = templates[0]["main"][0]["Аспирантура"][Faculty_Postgraduate[i]][]


# a = templates[0]["main"][0]["Бакалавриат"][1]
# for i in a:
#     print(i)

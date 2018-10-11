import re


pattern = '.*/[0-9]{8}'
prog = re.compile( pattern )

with open('URLs.txt', 'r') as f:
    tematics = {}
    for line in f:
        # убираем символ переноса строки для каждой читаемой строчки
        line_n = line.split("/")
        tematics.setdefault(line_n[1],0)
        tematics[line_n[1]] += 1


print("Распределение тематик новостей: {}".format(tematics))


for i in tematics:
    print('{} {} раз упоминается в тексте \n'.format(i,tematics[i]))
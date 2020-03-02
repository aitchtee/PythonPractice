'''
Найти людей, не выполнивших тест с первого раза. Вывести их значения повторных попыток, если таковые есть.
'''
import csv
infile = open('files/1.csv', 'r', encoding='utf-8')
table = []
for row in csv.reader(infile):
    table.append(row)
infile.close()
firstEl = table[:len(table)]
table = table[1:len(table)-2]
resDict = {}
for i in range(len(table)):
    fio = table[i][0].upper() + ' ' + table[i][1].upper()
    if fio not in resDict:
        resDict[fio] = 1
    else:
        resDict[fio] += 1
for i in range(len(list(resDict.values()))):
    if list(resDict.values())[i] > 1:
        print(list(resDict.keys())[i], ':', list(resDict.values())[i])

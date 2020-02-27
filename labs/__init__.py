'''

print('Введите цвета первого ребенка')
firstChildColors = input().split()

print('Введите цвета второго ребенка')
secondChildColors = input().split()

a = set(firstChildColors)
b = set(secondChildColors)
print('Цвета первого', a)
print('Цвета второго', b)
print('Общие', a.intersection(b))
print('Разные', a.difference(b))

'''

# вводится кол-во учеников, для каждого из них вводится кол-во языков и эти языки
# вывести языки, которые знает хотя бы один ребенок
# вывести языки, которые знают все

'''
firstStudent = 'eng fra rus'
firstStudent = firstStudent.split()
fullSet = set(firstStudent)
allKnownSet = set(firstStudent)

numStudents = int(input())
for i in range(numStudents-1):
    nextStudentLang = input().split()
    resFullSet = fullSet.union(set(nextStudentLang))
    resAllKnownSet = allKnownSet.intersection(set(nextStudentLang))

print('Знают хотя бы один', resFullSet)
print('Знают все', resAllKnownSet)

'''

# в стране К партий, если хоть одна бастует - страна не работает. начинаем с пн - это 1-ое
# сб и вс выходные
# сколько дней отдыхала страна

'''
numOfDays = int(input())
numOfParties = int(input())
parties = []
setOfDays = set()

for i in range(numOfParties):
    parties.append(tuple(map(int, input('start day and period: ').split())))
for party in parties:
    setOfDays.add(party[0])
    for day in range(party[0], numOfDays, party[1]):
        if (day-6) % 7 != 0 and (day % 7) != 0:
            setOfDays.add(day)
print(setOfDays)

'''

# Вам известно за кого проголосовал каждый штат и сколько голосов было отдано данным штатом.
# Подведите итоги выборов: для каждого из участников голосования определите число отданных за него голосов.

f = open('lab.txt')
lines = f.readlines()
f.close()
resDict = {}
for line in lines:
    if line.rstrip().split()[0] not in resDict:
        resDict[line.rstrip().split()[0]] = line.rstrip().split()[1]
    else:
        resDict[line.rstrip().split()[0]] = int(resDict.get(line.rstrip().split()[0])) + int(line.rstrip().split()[1])
for key in sorted(resDict):
    print(key, resDict[key])

# 1 11 21 1211 111221 312211 13112221 1113213211



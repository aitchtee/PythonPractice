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

'''
# вводится кол-во учеников, для каждого из них вводится кол-во языков и эти языки
# вывести языки, которые знает хотя бы один ребенок
# вывести языки, которые знают все

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

numOfDay = int(input())
numOfParties = int(input())
setOfDays = set()
beginDay = set()
periodDay = set()

for i in range(numOfDay):
    setOfDays.add(i+1)

for i in range(numOfParties):
    beginDay.add(int(input()))
    periodDay.add(int(input()))

for i in range(numOfDay):
    print()

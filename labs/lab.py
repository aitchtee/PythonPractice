#2 ребенка играют в кубики
#вводим кол-во цветов 1го ребенка, затем цвета
#аналогично для 2го
#найти общие цвета
#цвета что есть у 1го и нет у второго (наоборот соответственно)

#child1 = set(input('цвета у первого:\n').split())
#child2 = set(input('Цвета у второго:\n').split())
#print(str(child1.intersection(child2))+'\n'+str(child1.difference(child2))+'\n'+str(child2.difference(child1)))

#вводим число школоты 
#для каждого вводятся языки
#вывести языки которые знают хотя бы одно дитя
#вывести языки которые знают все

#langonce = set()
#langall = set()
#inLang = set(input('язык:  ').split())
#langonce = inLang
#langall = inLang
#for i in range(int(input('введите число школоты = ')) - 1):
#	inLang = set(input('язык:  ').split())
#	langonce = inLang.union(langonce)
#	langall = langall.intersection(inLang)
#print(str(langonce)+'\n'+str(langall))

#количетво дней
#количество партий
#вводится 1й день забастовки и период до повтора

#daysZ = set()
#days = int(input('количество дней: '))
#for i in range(int(input('количество партий: '))):
#	dayZ = int(input('начало: '))
#	dayT = int(input('период: '))
#	for j in range(1+(days - dayZ) // dayT):
#		if((((dayZ+j*dayT) % 7) != 0) and (((dayZ+j*dayT + 1) % 7) != 0)):
#			daysZ.add(dayZ+j*dayT)
#print(len(daysZ))

#result = dict()
#statekol = int(input('количество штатов: '))
#kandkol = set(input('кандидаты: ').split())
#for j in kandkol:
#	result[j] = int(input(j + ' чисо голосов: '))
#for i in range(statekol-1):
#	for j in kandkol:
#		result[j] += int(input(j + ' чисо голосов: '))
#print(result)

#result = dict()
#for i in range(int(input('размер базы: '))):
#	temp = input().split()
#	if(temp[0] in result.keys()):
#		if(temp[1] in (result[temp[0]]).keys()):
#			(result[temp[0]])[temp[1]] += int(temp[2])
#		else:
#			(result[temp[0]])[temp[1]] = int(temp[2])
#	else:
#		result[temp[0]] = dict([(temp[1], int(temp[2]))])
#print(result)


#палиндром
#добавить буквы справа до палиндрома

#import re
#st = re.compile('[^a-zA-Z]').sub('',input("строка = ")).upper()
#if(st == st[::-1]):
#	print('ДА')
#else:
#	print('НЕТ')

#import re
#st = re.compile('[^a-zA-Z]').sub('',input("строка = ")).upper()
#kol = len(st) + 1
#for i in (range(len(st))):
#	j = i + 1
#	while(st+(st[i:j])[::-1] != (st+(st[i:j])[::-1])[::-1] and j < len(st)):
#		j += 1
#	if(j < len(st) and kol > j - i):
#		print((st+(st[i:j])[::-1]))
#		kol = j - i
#print(kol)

result = '1'
for i in range(1,int(input('N = '))):
	temp = ''
	kol = 1
	for j in range(1,len(result)):
		if(result[j] == result[j-1]):
			kol += 1
		else:
			temp += str(kol) + result[j-1]
			kol = 1
	result = temp + str(kol) + result[len(result)-1]
print(result)

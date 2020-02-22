'''
Дан файл, содержащий текст на русском языке.
Определить, сколько раз встречается в нем самое длинное слово.
'''

import re
f = open('third.txt', encoding='utf-8')
st = f.readlines()
f.close()
res = re.compile('[^а-яА-ЯёЁ ]').sub('', str(st))
maxLen = len(res.split()[0])
for i in range(len(res.split())):
    if len(res.split()[i]) > maxLen:
        maxLen = len(res.split()[i])
        findWord = res.split()[i]
count = 0
for i in res.split():
    if i == findWord:
        count += 1
print(findWord, ':', count)

'''
Дана строка S, целое число N (> 0) и файл-архив целых чисел, сожержащий данные из нескольких файлов.
Восстановить из файла-архива файл с номером N и сохранить его под именем S.
Если файл-архив содержит данные из менее чем N файлов, то оставить результирующий файл пустым
'''

n = int(input())
f = open('arcFile.txt')
numFiles = int(f.readline())
if n > numFiles:
    fi = open('resFile.txt', 'tw', encoding='utf-8')
    fi.close()
else:
    lines = []
    for i in range(numFiles):
        lines.append(int(f.readline().rstrip()))
    fileContent = []
    for i in range(numFiles):
        fileContent.append(f.readline().rstrip())
    fi = open('resFile.txt', 'tw', encoding='utf-8')
    fi.write(fileContent[n-1])
    fi.close()
f.close()

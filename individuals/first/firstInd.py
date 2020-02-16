'''
Для заданной последовательности неотрицательных целых чисел необходимо найти
минимальную сумму двух ее элементов, номера которых различаются не менее чем на 4.
Значение каждого элемента последновательности не превышает 1000. Количество элемнтов
последовательности не превышает 10000.
'''

f = open('first.txt')
kol = int(f.read(1))
arr = list(map(int, f.read().split()))
f.close()
sortArr = sorted(arr)
minSum = sortArr[kol-1] + sortArr[kol-2]
# print('Старый минимум', minSum)
for i in range(kol-4):
    for j in range(i+4, kol):
        newMin = arr[i] + arr[j]
        if newMin < minSum:
            minSum = newMin
print('Новый минимум', minSum)

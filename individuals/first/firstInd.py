'''
Для заданной последовательности неотрицательных целых чисел необходимо найти
минимальную сумму двух ее элементов, номера которых различаются не менее чем на 4.
Значение каждого элемента последновательности не превышает 1000. Количество элемнтов
последовательности не превышает 10000.
'''
f = open('first.txt')
kol = f.read(1)
arr = list(map(int, f.read().split()))
sortArr = sorted(arr)
minSum = sortArr[len(arr)-1] + sortArr[len(arr)-2]
# print('Старый минимум', minSum)
f.close()
for i in range(len(arr)):
    for j in range(len(arr)):
        if abs(i-j) >= 4:
            newMin = arr[i] + arr[j]
            if newMin < minSum:
                minSum = newMin
print('Новый минимум', minSum)

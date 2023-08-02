from random import randint

# Заполните список элементами арифметической
# прогрессии.


start = int(input('Введите начальный элемент: '))
count = int(input('Введите количество элементов: '))
step = int(input('Введите шаг прогрессии: '))
list = []
for i in range(count):
    list.append(start+i*step)
print(list)


# Определить индексы элементов списка, значения которых принадлежат
# заданному диапазону (не меньше и не больше)

print(list_2 := [randint(1, 10) for _ in range(20)])
begin = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))
# Здесь бы еще проверку что end больше start
result = []
for i in range(len(list_2)):
    if begin < list_2[i] < end:
        result.append(i)
print(result)


# Напишите рекурсию summ_(a, b), возвращающую сумму двух
# целых чисел неотрицательных чисел. Из всех арифметических операций
# допускаются только +1 и -1. Также нельзя использовать циклы.

def summ_(a, b):
    if b == 0:
        return a
    return summ_(a+1, b-1)


print(summ_(10, 25))

# Найти N-ое число Фибоначчи

from random import randint


def fibo(n):
    if n in [0, 1]:
        return 1
    return fibo(n-1) + fibo(n-2)


print(fibo(8))


# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет
# оценки Василия, но наоборот: все максимальные на минимальные

# print (sorted(list1)) # Сортировка по возрастанию
# print (sorted(list, reverse = True)) # Сортировка по убыванию


print(list_1 := [randint(1, 5) for item in range(1, 11)])

min_ = min(list_1)
max_ = max(list_1)

for i in range(len(list_1)):
    if list_1[i] == max_:
        list_1[i] = min_
print(list_1)


# Функция является ли число простым

def is_prime(num: int) -> bool:
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for dev in range(3, num//2 + 1, 2):
        if num % dev == 0:
            return False
    return True


print(is_prime(17))


# С помощью рекурсии, которая перевернет ввод в обратную сторону
# без использования списков и циклов

def sum(n):
    if n < 1:
        return ''
    i = input()
    return sum(n-1) + ' ' + i


num = int(input('Введите: '))
print(sum(num))

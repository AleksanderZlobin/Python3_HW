# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а
# некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть

from random import randint

coinNumber = randint(10, 20)
coinCount = None
headsCount = 0
tailsCount = 0

for i in range(coinNumber):
    coinCount = randint(0, 1)

    if coinCount == 0:
        headsCount += 1
        print('орел', end=', ')
    else:
        tailsCount += 1
        print('решка', end=', ')

print(f'\n{headsCount}') if headsCount < tailsCount else print(
    f'\n{tailsCount}')


# Альтернативное решение:
coins = int(input('Введите количество монет: '))
heads = 0

for _ in range(coins):
    coin = randint(0, 1)
    print(coin, end=' ')
    heads += coin
print(f'\nНужно перевернуть {1 if heads < coins // 2 + 1 else 0}')

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает
# Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их
# отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.


S = int(input('Введите сумму: '))
P = int(input('Введите произведение: '))

for x in range(1000):
    y = S - x
    if x*y == P:
        print(f'Значение x = {x}, значение y = {y}')
        break

# Решение через дискриминант:
disc = S**2 - 4*P
x = int((-S + disc**(0.5))//-2)
y = int((-S - disc**(0.5))//-2)
print(f'Загаданные числа - {x} и {y}')


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input('Введите число N: '))
twoDegree = 1
print(twoDegree, end=', ')

while twoDegree <= N:
    twoDegree *= 2
    if twoDegree > N:
        break
    print(twoDegree, end=', ')

# Альтернативное решение

number = int(input('Введите число: '))
num = 1
while num < number:
    print(num)
    num *= 2

# Даны два массива чисел. Требуется вывести те элементы первого
# массива (в том порядке, в каком они идут в первом массиве), которых
# нет во втором массиве. Пользователь вводит число N - количество
# элементов в первом массиве, затем число M - количество элементов во
# втором массиве.

from random import randint

# print(list_1 := [randint(1, 10) for _ in range(int(input('N: ')))])
# print(list_2 := [randint(1, 10) for _ in range(int(input('M: ')))])
# list_3 = []

# for item in list_1:
#     if item not in list_2:
#         list_3.append(item)
# print(list_3)


# Вывести количество элементов списка, соседи которого больше

# print(list_4 := [randint(1, 10) for _ in range(int(input('N: ')))])

# count = 0

# for i in range(1, len(list_4) - 1):
#     # if list_4[i] < list_4[i-1] and list_4[i] < list_4[i+1]:
#     if list_4[i-1] > list_4[i] < list_4[i+1]:
#         count += 1
# print(count)


# Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента, равные
# друг другу образуют пару, которую необходимо посчитать.

print(list_5 := [randint(0, 5) for _ in range(10)])
print(sum([list_5.count(i)//2 for i in set(list_5)]))

count = 0
for i in set(list_5):
    count += list_5.count(i)//2
print(count)


# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k.

def sum_devs(num: int):
    summ_ = 0
    for i in range(1, num//2 + 1):
        if num % i == 0:
            summ_ += i
    return summ_


digit_dict = {i: sum_devs(i) for i in range(1, 10000)}

for digit, summ_ in digit_dict.items():
    if digit == digit_dict.get(summ_) and digit < summ_:
        print(digit, summ_)

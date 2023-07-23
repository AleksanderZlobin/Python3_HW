# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

number = input('Введите строку: ')

count_dict = {}
# total = [] # Опционально, если нужно результат сохранить в списке

for i in number:
    # Обращается к ключу словаря, если его нет
    # записывает в словарь и значение увеличивает на единицу
    count_dict[i] = count_dict.get(i, 0) + 1
    # Аналогичное выражение:
    # if i in count_dict:
    #     count_dict[i] += 1
    # else:
    #     count_dict[i] = 1

    print(
        f'{i}' + (f'_{count_dict[i]-1}' if count_dict[i] > 1 else ''), end=' ')
    # Опционально, если нужно результат сохранить в списке:
    # total.append(f'{i}' + (f'_{count_dict[i]-1}' if count_dict[i] > 1 else ''), end=' ')

# Опционально, если нужно результат сохранить в списке
# print(*total)


# Пользователь вводит текст(строка). Словом считается
# последовательность не пробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.

# "She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure. So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells"

string = "She sells. sea, shells on the sea shore The shells"
list_1 = list(string.upper().replace('.', ' ').replace(',', ' ').split())
print(list_1)
print(len(set(list_1)))


# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих слайдах:
# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#  n = int(input())
#  if max_number > n:
#  max_number = n
# print(max_number)
#
# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n)

n = int(input())
max_number = n
while n > 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)

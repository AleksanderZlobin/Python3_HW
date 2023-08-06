# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке

print(lst := input('Введите фразы через пробел: ').split())
# res = []
# for i in range(len(lst)):
#     res.append(len(list(filter(lambda x: x in 'аяуюэеиыоё', lst[i]))))
res = [(len(list(filter(lambda x: x in 'аяуюэеиыоё', lst[i]))))
       for i in range(len(lst))]
# print(res)
print('Парам пам-пам') if len(set(res)) == 1 else print('Пам парам')


# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.


def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        return_string = ""
        for j in range(1, num_columns + 1):
            return_string += str(operation(i, j)) + " "
        print(return_string.strip())


print_operation_table(lambda x, y: x * y)

# Альтернативное решение


def print_operation_table(operation, num_rows=6, num_columns=6):
    a = [[operation(i, j) for j in range(1, num_columns + 1)]
         for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f'{x:>3}' for x in i])


print_operation_table(lambda x, y: x * y)

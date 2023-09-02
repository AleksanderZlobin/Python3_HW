import calendar


def isleap(year):
    if calendar.isleap(year):
        return True
    else:
        return False


print(isleap(int(input('Введите год: '))))


year = int(input())


def is_leap(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True
    else:
        return False


print('Високосный') if is_leap(year) else print('Не високосный')


num = int(input())


def fibo(n):
    n1 = 0
    n2 = 1
    l = [n1, n2]
    while n1+n2 < n:
        l.append(n1+n2)
        n1 = n2
        n2 = l[-1]
    return l


lst = fibo(num)
print(lst)

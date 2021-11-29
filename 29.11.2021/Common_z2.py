import math     # Подключение модуля math
import time     # Подключение модуля time

def decorator1(func):       # Функция-декоратор 1
    def wrapper1(n,s):
        start = time.time()
        print('Была вызвана функция area')
        res = func(n,s)
        print('Время, затраченное на выполнение функции =', time.time() - start)
        return res
    return wrapper1

def decorator2(func):       # Функция-декоратор 2
    def wrapper2(n):
        start = time.time()
        print('Была вызвана функция sum')
        res = func(n)
        print('Время, затраченное на выполнение функции =', time.time() - start)
        return res
    return wrapper2

@decorator1     # Применение декоратора к функции area
def area(n, s):     # Функция для вычисления площади многоугольника
    print(n * s ** 2 / (4*math.tan(math.pi / n)))

@decorator2     # Применение декоратора к функции sum
def sum(n):     # Функция для вычисления суммы арифметической прогрессии
    print(n * (n + 1) / 2)

s = int(input())        # Ввод значения s для многоугольника
n = int(input())        # Ввод значения n для многоугольника
area(s, n)    # Вызов функции area с декоратором

n = int(input())        # Ввод значения n для прогрессии
sum(n)     # Вызов функции sum с декоратором
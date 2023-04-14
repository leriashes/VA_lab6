import numpy as np
import matplotlib.pyplot as plt
import math
import getch
import random as rand

#вычисление значений функции
def count_function(xs, func):
    ys = []

    for i in range(len(xs)):
        x = xs[i]
        ys.append(eval(func))
    return ys

#метод Симпсона
def Simpson(func, xs, h):

    if len(xs) % 2 == 0:
        xs = np.append(xs, xs[len(xs) - 1] + h)
    
    x = xs[0]
    result = eval(func)

    x = xs[len(xs) - 1]
    result += eval(func)

    for i in range (1, len(xs), 2):
        x = xs[i]
        result += eval(func) * 4

    for i in range (2, len(xs) - 1, 2):
        x = xs[i]
        result += eval(func) * 2

    result *= h / 3

    return result

#метод Монте-Карло
def MonteKarlo(func, a, b, N):
    xs = np.arange(a, b + 0.001, 0.001)
    ys = count_function(xs, func)
    M = max(ys)
    
    plt.plot([xs[0], xs[0], xs[len(xs) - 1], xs[len(xs) - 1]], [0, M, M, 0], 'y', linestyle = '--')
    plt.plot([xs[0], xs[len(xs) - 1]], [0, 0], 'black')
    
    
    K = 0

    for i in range(N):
        x = a + rand.random() * (b - a)
        y = M * rand.random()

        if y < eval(func):
            K += 1
            plt.plot(x, y, 'bo')
        else:
            plt.plot(x, y, 'go')

    plt.plot(xs, ys, 'r')
    plt.grid(True)

    plt.xlabel(r'$x$', fontsize=14)
    plt.ylabel(r'$y$', fontsize=14)

    plt.show()

    result = M * (b - a) * K / N
    return result

while True:
    print('Введите функцию: y = ', end='')
    func = input()
    print('\n')

    print('Введите левую границу отрезка: a = ', end='')
    a = float(input())
    print('\n')

    while True:
        print('Введите правую границу отрезка: b = ', end='')
        b = float(input())
        print('\n')

        if b > a:
            break

    while True:
        print('Введите шаг для метода Симпсона: h = ', end='')
        h = float(input())
        print('\n')

        if h <= b - a:
            break

    while True:
        print('Введите общее количество точек для метода Монте-Карло: N = ', end='')
        N = int(input())
        print('\n')

        if N > 0:
            break

    xs = np.arange(a, b + h, h)

    print('\nМетод Симпсона: ', Simpson(func, xs, h), end='')
    if (len(xs) % 2 == 0): print(' (добавлена одна точка справа)', end='')

    print('\n\nМетод Монте-Карло: ', MonteKarlo(func, a, b, N))

    print('\n\nЧтобы продолжить нажмите Enter. Для выхода из программы нажмите любую другую клавишу. ', end='\n')
    cont = getch.getch()
   
    if cont == '\n' or cont == b'\r':
        print('\n\n')
    else:
        break


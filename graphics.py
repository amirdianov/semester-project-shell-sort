import math

import matplotlib.pyplot as plt


# from benchmark import time_x, time_add_y, time_extract_y


def paint_grafics(time_x, time_sort_y):
    def func(x):
        a = []
        for i in x:
            a.append(i ** 2)
        return a

    plt.plot(time_x, time_sort_y, color='b')
    plt.plot(time_x, func(time_x), color='r')
    plt.title('Время работы алгоритма')
    plt.ylabel('Время')
    plt.xlabel('Количество поданных данных')
    plt.show()

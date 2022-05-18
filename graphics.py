import math

import matplotlib.pyplot as plt


# from benchmark import time_x, time_add_y, time_extract_y


def paint_grafics(time_x, time_sort_y,  time_another_y):

    plt.plot(time_x, time_sort_y, color='b')
    plt.plot(time_x, time_another_y, color='r')
    plt.title('Время работы алгоритма')
    plt.ylabel('Время')
    plt.xlabel('Количество поданных данных')
    plt.show()

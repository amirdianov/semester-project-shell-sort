import random
import pandas as pd

from typing import Callable
from sorting_algorithm import shell_sort
from generate_random_list import random_list
from time import time
import graphics

ATTEMPTS: int = 100


def time_it(function: Callable) -> Callable:
    def wrap_and_time(*args):
        start = time()
        function(*args)
        end = time()
        result = end - start
        return result

    return wrap_and_time


def start_testing(queue_length: int, attempt: int):
    new_list = random_list(queue_length, attempt)
    return new_list


@time_it
def check_time(test_queue: list):
    shell_sort(test_queue)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

@time_it
def func(x):
    insertion_sort(x)


res = {'size_data': [],
       'sort_time': []}
aver = {'size_data': [],
        'sort_time': []}
time_x = []
time_sort_y_average = []
time_y_algorithm_average = []
for i in range(500, 10001, 500):
    ans = []
    values = []
    data_v = i
    for attempt in range(ATTEMPTS):
        test_sort_list1: list = start_testing(data_v, attempt)
        test_sort_list2: list = [random.randint(-10000, 10000) for _ in range(data_v)]
        time_work = check_time(test_sort_list1)
        time_work_algorithm = func(test_sort_list2)
        ans.append(time_work)
        values.append(time_work_algorithm)
        res['sort_time'].append(time_work)
        res['size_data'].append(data_v)
    # print(ans)
    time_x.append(data_v)
    aver['size_data'].append(data_v)
    average_ans = sum(ans) / len(ans)
    average_value = sum(values) / len(values)
    aver['sort_time'].append(average_ans)
    time_sort_y_average.append(average_ans)
    time_y_algorithm_average.append(average_value)

print('-' * 10)

graphics.paint_grafics(time_x, time_sort_y_average, time_y_algorithm_average)


res = pd.DataFrame(res)
aver = pd.DataFrame(aver)
salary_sheets = {'Research': res, 'Average': aver}
writer = pd.ExcelWriter('./table.xlsx', engine='xlsxwriter')

for sheet_name in salary_sheets.keys():
    salary_sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

writer.save()

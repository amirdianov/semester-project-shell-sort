'''
generation dataset
'''
# Здесь будет производиться генерация наборов данных и их запись в файл .txt
import random

PATH: str = '/Users/bulat/PycharmProjects/semester-project-shell-sort/dataset_local/'


def random_list(list_length: int, attempt: int):
    '''создание рандомнго листа'''
    path = PATH + fr'{list_length}_{attempt}.txt'
    testing_list = []
    for _ in range(list_length):
        random_value = random.randint(-10000, 10000)
        testing_list.append(random_value)

    with open(path, 'w', encoding='utf-8') as file:
        for val in testing_list:
            file.write(f'{val}\n')
    return testing_list

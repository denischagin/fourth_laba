import os


def dir():
    while True:
        way = input('Введите директорию:')
        if os.path.isdir(way) == True:
            return way
        else:
            print('Вы ввели не правильный путь к файлу')


def dict_way_size(way):
    pass

def analysis(dict1):
    pass


def duplicate(duplicate):
    pass

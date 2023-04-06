import dateparser
import datetime


def delete(base, id):
    base = base.split('\n')
    flag = True
    for i in base:
        if id == i.split(';')[0]:
            base.remove(i)
            flag = False
    if flag:
        print('Работника с таким Id нет !')
    del base[-1]
    return base


def changeWorker(base, id):
    base = base.split('\n')
    for i in range(len(base) - 1):
        x = base[i].split(';')
        if id == x[0]:
            x[1] = input('Заголовок   ')
            x[2] = input('Текст   ')
            date_parsed = dateparser.parse(str(datetime.datetime.now()))
            date_string = date_parsed.strftime('%Y-%m-%d %H:%M:%S')
            x[3] = date_string
            base[i] = ';'.join(x)
            del base[-1]
    return base


def find(base):
    worker = input('Введите запрос поиска  ')
    base = base.split('\n')
    flag = True
    result = []
    for i in base:
        if worker in i:
            flag = False
            print(i)
    if flag:
        result.append('Работник не найден !')


def add_id(base):
    base = base.split('\n')
    if len(base) == 1:    
        return 1
    else:
        return int(base[len(base) - 2].split(';')[0]) + 1

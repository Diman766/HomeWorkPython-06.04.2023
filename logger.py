import os
import datetime
import dateparser


def writer(id, heading, text):
    with open('base.csv', 'a') as f:
        date_parsed = dateparser.parse(str(datetime.datetime.now()))
        date_string = date_parsed.strftime('%Y-%m-%d %H:%M:%S')
        f.write(f'{id};{heading};{text};{date_string}\n')


def get_base():
    current_directory = os.getcwd()
    contents = os.listdir(current_directory)
    filename = 'base.csv'

    if filename in contents:
        with open(filename, 'r') as f:
            return f.read()
    else:
        with open(filename, 'a+') as f:
            return f.read()


def rewriter(base):
    f = open('base.csv', 'w+')
    f.close()
    with open('base.csv', 'a') as f:
        for i in base:
            x = ''.join(i)
            f.write(f'{x}\n')

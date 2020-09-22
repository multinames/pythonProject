from tempfile import mkstemp
from os import close
from shutil import move


def write_lines(file='C:\\tmp\\file21.txt'):
    ft, temp = mkstemp()  # создать temp-файл
    lines = []  # "уникальные" строки из file

    with open(temp, 'w') as t, open(file) as f:
        for line in f:  # читать file построчно
            if line not in lines:  # для line, отсутствующих в lines
                lines.append(line)  # сохранить line в lines
                t.write(line)  # записать line в temp-файл
    close(ft)  # закрыть temp-файл
    move(temp, 'C:\\tmp\\file22.txt')  # переместить/переименовать temp-файл в file
from tempfile import mkstemp
from os import close
from shutil import move

file ='C:\\tmp\\file21.txt' #исходный файл

file_temp, temp = mkstemp() # создать temp-файл
lines = [] # уникальные строки из file
with open(temp, 'w') as tf, open(file) as f:
         for line in f: # читать file построчно
             if line not in lines: # для line, отсутствующих в lines
                 lines.append(line) # сохранить line в lines
                 tf.write(line) # записать line в temp-файл
close(file_temp) # закрыть temp-файл
move(temp, file) # переместить/переименовать temp-файл в file

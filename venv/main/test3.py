import random
#  здесь указываете реальный путь к файлу
path = r"c:\\tmp\\file21.txt"
fin = open(path, 'r')
lines = fin.readlines()
lines[-1] += '\n'
fin.close()
#random.shuffle(lines)
fout = open(path, 'w')
lines = fout.writelines(lines)
fout.close()
with open('C:\\tmp\\file21.txt') as fin:    # открываем исходный файл
    fout = open('C:\\tmp\\file22.txt', 'w+')    # открываем новый файл
    flag = False    # устанавливаем флаг
    for line in fin:    # читаем исходный файл в первом цикле
        for tmp in fout:    # читаем новый файл во втором цикле
            if tmp == line: # сравниваем строки
                flag = True
                print('Совпадение найдено!')
                break
        if flag == False:
            fout.write(line)
        elif flag == True:
            flag = False
        fout.seek(0)    # переход на начало нового файла во втором цикле
    fout.close()
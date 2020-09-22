f1 = open('C:\\tmp\\file22.txt','w+')
flag = False
with open('C:\\tmp\\file21.txt') as f2:
    for line in f2:
        for tmp in f1:
            if tmp == line:
                flag = True
                print('Совпадение найдено!')
                break
        if flag == False:
            f1.write(line)
        elif flag == True:
            flag = False
        f1.seek(0)
    f1.close()
f = open("c:\\tmp\\file1.txt",'r')
f2 = open ("c:\\tmp\\file2.txt",'w+')

for line in f:

    for line2 in f2:
        print(line)
        if line not in line2:

                f2.write(line)
f.close
f2.close
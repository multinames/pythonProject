f = open("c:\\tmp\\file1.txt",'r')
f2 = open ("c:\\tmp\\file2.txt",'w')
l_file = set()

for line in f:
    if line not in l_file:
        f2.write(line)
    l_file.add(line)
f.close
f2.close
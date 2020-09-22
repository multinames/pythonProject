
f ='c:\\tmp\\file21.txt'

read_lines = set(open(f,'r').readlines())
write_to_file = open(f,'w').writelines(set(read_lines))
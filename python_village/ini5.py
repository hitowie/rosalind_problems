#!/usr/bin/env python3

file_in = open('rosalind_ini5.txt', 'r')
file_out = open('ini5.out', 'w')

count = 0

for line in file_in.readlines():
    count += 1
    if count % 2 == 0:
        file_out.writelines(line)

file_in.close()
file_out.close()
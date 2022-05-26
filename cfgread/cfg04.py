#!/usr/bin/env python3
######## EXPLORE READ ##########

## display number of lines in the file read
#num_lines = open('vlanconfig.cfg').read().count('\n')
#print(num_lines)

with open("vlanconfig.cfg", "r") as fp:
    num_lines = sum(1 for line in fp)
    print('Total lines:', num_lines)


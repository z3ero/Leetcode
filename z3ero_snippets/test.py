import sys
# input one line : \n is end
'''
str = raw_input()
print(str)
'''

for line in sys.stdin: 
    for value in line.split(): 
        print(value)

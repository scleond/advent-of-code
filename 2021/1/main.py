# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 07:37:33 2021

@author: chris
"""

last_line = None
greater_count = 0

# part 1
with open('data.txt') as f:
    lines = f.readlines()
    for line in lines:
        if last_line == None:
            last_line = int(line)
            continue
        greater_count = greater_count + (int(line) > last_line)  #True == 1
        last_line = int(line)
   # print(greater_count)
    
line_n1 = None
line_n2 = None
last_sum = None
greater_sum_count = 0
    
# part 2
with open('data.txt') as f:
    lines = f.readlines()
    
    # load n-1 and n-2 terms at start of loop
    for line in lines:
        if line_n1 == None:
            line_n1 = int(line)
            continue
        if line_n2 == None:
            line_n2 = line_n1
            line_n1 = int(line)
            continue
        
        # init last sum
        new_sum = line_n1 + line_n2 + int(line)
        line_n2 = line_n1
        line_n1 = int(line)
        if last_sum == None:
            last_sum = new_sum
            continue
        
        greater_sum_count = greater_sum_count + (new_sum > last_sum)  #True == 1
        last_sum = new_sum

        
    print(greater_sum_count)    
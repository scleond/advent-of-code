# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

# part 1
with open('input.txt') as f:
    lines = f.readlines()
    
    # [horizontal_pos, depth]
    loc = np.array([0,0])


    # [horizontal_pos, depth]    
    command = {'forward': np.array([1, 0]),
               'up':      np.array([0, -1]),
               'down':    np.array([0, 1])}
    
    for line in lines:
        [direction, dist] = line.split()
        loc = loc + ( command[direction] * int(dist))
    # print(loc.prod())
        
# part 2
with open('input.txt') as f:
    lines = f.readlines()
    
    # [horizontal_pos, depth, aim]
    loc = np.array([0,0,0])
    
    # [[horizontal_pos, depth, aim],
    command_dict = {'forward': np.array([1, 1, 0]),
                    'up':      np.array([0, 0, -1]),
                    'down':    np.array([0, 0, 1])}
    
    for line in lines:
        [command, dist] = line.split()
        loc = loc \
            + (command_dict[command] * [1,0,1] * int(dist)) \
            + (command_dict[command] * [0,1,0] * int(dist) * loc[2])
    print(loc[:2].prod())

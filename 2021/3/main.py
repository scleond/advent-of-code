# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 11:19:02 2021

@author: chris
"""


# part 1

with open('input.txt') as f:
    lines = f.read().splitlines()  # doesn't read \n
    
    reportSum = [0] * len(lines[0])
    gammaRateArray = [0] * len(lines[0])
    epsilonRateArray = [0] * len(lines[0])
    
    for line in lines:
        for i, bitStr in enumerate(line):
            bit = int(bitStr)
            reportSum[i] = reportSum[i] + ((bit ^ 0) - (bit ^ 1))
    
    for i,bit in enumerate(reportSum):
        gammaRateArray[i] = (bit/abs(bit) + 1) / 2
        epsilonRateArray[i] = (bit/abs(bit) * -1 + 1) / 2
        
    gammaRateArray.reverse()
    epsilonRateArray.reverse()
    
    gammaRate = 0
    epsilonRate = 0
    
    for i in range(len(gammaRateArray)):
        gammaRate = gammaRate + gammaRateArray[i] * (2 ** i)
        epsilonRate = epsilonRate + epsilonRateArray[i] * (2 ** i)
    
    print(gammaRate * epsilonRate)
    
# part 2
import pandas as pd

df = pd.read_csv('input.txt', dtype = str)  
        
            
        
        

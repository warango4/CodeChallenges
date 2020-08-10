#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    all_freq = {}   
    for i in s: 
        if i in all_freq: all_freq[i] += 1
        else: all_freq[i] = 1
    print(all_freq)
    for x in all_freq.values():
        count = 0
        for k in all_freq.values():
            if k != x and k - x == 1: count += 1
            if k != x and (k - x > 1 or count > 1): return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open('answer.txt', 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
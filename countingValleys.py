#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    step = 0
    for i in s:
        if i == 'U': step += 1
        else: step -= 1

        if step == 0 and i == 'U':
            valleys += 1    
    return valleys


if __name__ == '__main__':
    fptr = open('answer.txt', 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    valid_clouds = []
    c_size = len(c)
    for i in range(c_size):
        if c[i] == 1: continue
        valid_clouds.append(i)
    steps = 0
    i = 0
    while i < len(valid_clouds) - 2:
        if valid_clouds[i + 2] - valid_clouds[i] == 2: i += 2
        else: i += 1
        steps += 1
    steps += 1
    print(steps)
    return steps

if __name__ == '__main__':
    fptr = open('answer.txt', 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

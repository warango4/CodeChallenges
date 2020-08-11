import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colors = {}
    for i in ar:
        if i in colors: colors[i] += 1
        else: colors[i] = 1
    
    count = 0
    for i in colors.values():
        n_pairs = int(i / 2)
        count += n_pairs
    return count


if __name__ == '__main__':
    fptr = open('aswer.txt', 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

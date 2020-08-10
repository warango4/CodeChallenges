import math
import numpy as np

def findSmallestInterval(numbers):
    numbers = np.array(numbers)
    numbers = np.sort(numbers)
    smallest = numbers[1] - numbers[0]
    for i in range(2, len(numbers)):
        if(abs(numbers[i] - numbers[i - 1]) < smallest): smallest = abs(numbers[i] - numbers[i - 1])
    return smallest

numbers = [24, 10, 7, 16, 37]
print(findSmallestInterval(numbers))
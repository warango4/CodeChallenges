import sys
import math
from contextlib import redirect_stdout
import re

def solve(image_width, image_height, image, pattern_width, pattern_height, pattern):
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr)
    r = re.compile(pattern)
    newlist = list(filter(r.match, image))
    
    return []

# Ignore and do not change the code below
def main():
    image_width, image_height = [int(i) for i in input().split()]
    image = []
    for i in range(image_height):
        image.append(input())
    pattern_width, pattern_height = [int(i) for i in input().split()]
    pattern = []
    for i in range(pattern_height):
        pattern.append(input())
    with redirect_stdout(sys.stderr):
        coordinates = solve(image_width, image_height, image, pattern_width, pattern_height, pattern)
    for i in range(2):
        print(coordinates[i])

if __name__ == "__main__":
    main()
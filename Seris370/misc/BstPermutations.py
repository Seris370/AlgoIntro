#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'permuteBST' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY sequence as parameter.
#

combinations = {}

def separate(root, lst):
    return ([i for i in lst if i < root], [i for i in lst if i >= root])

def choose(n, k):
    if (n, k) in combinations:
        return combinations[n, k]
    else:
        if k > n:
            return 0
        c = math.factorial(n) / math.factorial(k) / math.factorial(n-k)
        combinations[n, k] = c
        combinations[n, n-k] = c
        return c

def permuteBST(sequence):
    # Write your code here
    if len(sequence) < 2:
        result = 1
    else:
        root = sequence[0]
        lst = sequence[1:]
        tree = separate(root, lst)
        left = tree[0]
        right = tree[1]
        result = int(choose(len(lst), len(right)) * permuteBST(left) * permuteBST(right))
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sequence_count = int(input().strip())

    sequence = []

    for _ in range(sequence_count):
        sequence_item = int(input().strip())
        sequence.append(sequence_item)

    result = permuteBST(sequence)

    fptr.write(str(result) + '\n')

    fptr.close()

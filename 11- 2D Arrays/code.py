#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    max_sum = ""
    for i in range(4):
        for j in range(4):
            sum = 0
            for k in range(3):
                sum += arr[i][j+k]
                sum += arr[i+2][j+k]
            sum += arr[i+1][j+1]
            if max_sum == "":
                max_sum = sum
            else:
                max_sum = max(max_sum, sum)
    print(max_sum)
            

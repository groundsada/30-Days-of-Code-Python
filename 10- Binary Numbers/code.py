#!/bin/python3

import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input())
def bin(n,l):
    if n >= 1:
        bin(n//2,l)
    l.append(n%2)
l, counting,counter,max_counter = [], False, 0,0
bin(n,l)
for i in range(len(l)):
    if l[i] == 1:
        counting = True
        counter += 1
    if l[i] == 0 and counting == True or i == len(l)-1:
        counting = False
        max_counter = max(max_counter, counter)
        counter = 0
print(max_counter)

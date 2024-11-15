#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pcount=0
    ncount=0
    zcount=0
    for i in arr:
        if i>0:
            pcount+=1
        elif i<0:
            ncount+=1
        else:
            zcount+=1
    n=len(arr)
    print("{:.6f}".format(pcount/n))
    print("{:.6f}".format(ncount/n))
    print("{:.6f}".format(zcount/n))
            
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

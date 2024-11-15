#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min=10**10
    max=0
    minsum=0
    maxsum=0
    for i in arr:
        minsum+=i
        maxsum+=i
        if(i<min):
            min=i
        if(i>max):
            max=i 
    minsum-=max
    maxsum-=min      
    print(minsum,maxsum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

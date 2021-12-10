import math
import os
import random
import re
import sys

def near_fibo(num):
    if (num == 0):
        print(0)
        return
    first = 0
    second = 1
    third = first + second
    while (third <= num):
        first = second
        second = third
        third = first + second
    if (abs(third - num) >=
        abs(second - num)):
        ans = second
    else:
        ans = third
    print(ans-num)

arr = [15,1,3]
num = sum(arr)
near_fibo(num)

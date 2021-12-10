import math
import os
import random
import re
import sys

def CheckLeap(year1,year2):  
    year = []
    for i in list(range(year1, year2+1)):
        if ((i % 400 == 0) or  
            (i % 100 != 0) and  
            (i % 4 == 0)):   
            year.append(i)
    print(year)

year1 = int(input("Enter the first number: "))
year2 = int(input("Enter the second number: "))
CheckLeap(year1,year2)  

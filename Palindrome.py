import math
import os
import random
import re
import sys

def Palindrome(string):
    new_string = ""
    reverse_string = ""
    y = -1
    for letter in string:
        if letter != " ":
            new_string += letter
        if string[y] != " ": 
            reverse_string += string[y]
        y -= 1
    if new_string.lower() == reverse_string.lower():
        print(string,'#--> palindrome')
    else:
        print(string,'#--> not palindrome')

string = str(input('Masukkan kalimat: '))
Palindrome(string)

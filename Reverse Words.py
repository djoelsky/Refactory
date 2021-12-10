import math
import os
import random
import re
import sys

def reverse_words(sentence):
    words = sentence.split()
    reverse = [word[::-1] for word in words]
    print(" ".join(reverse))

sentence = str(input('Masukkan kalimat: '))
reverse_words(sentence)

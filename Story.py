import math
import os
import random
import re
import sys
import itertools
from datetime import datetime

all_items = []
price_total = []

def cashier():
    code = str(input('add or done? : '))
    if code == 'add':
        items = str(input('Items : '))
        all_items.append(items)
        price = int(input('Price : '))
        price_total.append(price)
        cashier()
    elif code == 'done':
        result()
    else:
        cashier()

def result():
    print('\n\n\n')
    print(resto_name)
    print('Tanggal : ',now)
    print('Nama Kasir : '.ljust(15)+cashier_name.rjust(15))
    print(30*'=')
    for (a,b) in zip(all_items,price_total):
        i = str(a); j = str(b)
        print(i.ljust(15)+('Rp'+j).rjust(15))
    print(30*'_'+'+')
    x = sum(price_total); y = str(x)
    print('Total '.ljust(15)+('Rp'+y).rjust(15))

time = datetime.now()
now = time.strftime('%Y/%m/%d %H:%M:%S')
resto_name = str(input('Input resto name: '))
cashier_name = str(input('Input cashier name: '))
cashier()

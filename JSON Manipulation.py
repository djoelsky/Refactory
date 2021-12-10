import json

#Open the file json
with open('Data.json') as d:
    data = json.load(d)

#1. Find items in the Meeting Rom
print('All items in the Meeting Room:')
for placement in data:
    if placement['placement']['name'] == 'Meeting Room':
        print(placement['name'])
print('\n')

#2. Find all electronic devices
print('All electronics:')
for electronic in data:
    if electronic['type'] == 'electronic':
        print(electronic['name'])        
print('\n')  

#3. Find all the furniture
print('All furnitures:')
for furniture in data:
    if furniture['type'] == 'furniture':
        print(furniture['name'])        
print('\n')

#4. Find all the items were purchase on 16 Januari 2020
import datetime
print('All items purchased on 16 Januari 2020:')
time1 = datetime.datetime(2020,1,16,0,0,0).timestamp()
time2 = datetime.datetime(2020,1,16,23,59,59).timestamp()
for purchase in data:
    if time1 < purchase['purchased_at'] < time2:
        print(purchase['name'])        
print('\n')

#5. Find all items with brown color
print('All item with brown color:')
for color in data:
    if 'brown' in color['tags']:
        print(color['name'])   
print('\n')

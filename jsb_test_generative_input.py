### PART I : STAND ALONE 

### random input/memory setting generation for test cases
### 1. random start date before today (within 1 month range) X1 (dayID = 0; full dd/mm/yy omitted)
### 2. random 'today's date' after today (within 1 month range) X2 (dayID 
### 3. joints.txt is 1 
### 4. last pay date is placed randomly between 1. and 2. (can be 2.) [MANUAL CHECK FOR ERROR FIRST] X3
### 5. streak begins is randomly placed between 1. and 2. (can be 2.) [should be ok]
### 6. random 1/0
### run check tests
### end of stand alone test
### does not carry over information, redefined everytime the program is run

'''PART I : STAND ALONE'''

import random
import calendar
from datetime import date
from datetime import timedelta

minpaydays = 5

x1 = random.randint(0, 31) 
x2 = random.randint(0, 30) #will have to add to date last logged in
x3_range = x1 + x2
x3 = random.randint(0, x3_range)
x4 = random.randint(0, x3_range)
basejoint = str(1)

##random start date x1
real_present_day = date.today()
programbegins = real_present_day - timedelta(days = x1)
print("Program pretends to begin on:")
print(programbegins)

##random today's date x2
todayis = real_present_day + timedelta(days = x2)
todayID = x3_range
print("Today pretends to be:")
print(todayis)
print("Today's fakeID:")
print(todayID)

##random streakbegins date (if streakbegins comes before last pay, it means streak length x4
streakbeginsID = x3
print("Streakbegins FakeID:")
print(streakbeginsID)

##random last pay date x4
lastpayrand = x4
var1 = x4 % minpaydays
lastpayID = lastpayrand - var1
print("Lastpay randID:")
print(lastpayrand)
print("Lastpay supposed remainder:")
print(var1)
print("Correct LastpayID should be:")
print(lastpayID)

'''write to files'''

def generateinput(inputtext, filename):
    f = open(filename, 'w')
    inputtext = str(inputtext)
    f_write = f.write(inputtext)
    f.close()
    #print(filename + " has been written")

generateinput(basejoint,"jsb2_randtest_joints.txt") 
generateinput(lastpayID, 'jsb2_randtest_lastpay.txt')
generateinput(streakbeginsID, 'jsb2_randtest_streakbegins.txt')
generateinput(todayID, 'jsb2_randtest_today.txt')

### PART II: PERSISTENT

### for the following version, allow for simulation of multiple program runs
### 1. a new random 'today's date' 
### 2. a new random 1/0
### run everything with the rest of the memory
### run check tests for each round


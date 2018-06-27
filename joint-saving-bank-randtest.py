##babybaby
##baby-prefix denotes variable in external storage
##list of baby-variables: 1. babystreakbegins 2. babylastpayday 3. babyjoint

import calendar
import datetime
from datetime import date
from datetime import timedelta

## input
smokeboolean = int(input("Enter 1 to seek permission to smoke. Enter 0 to view progress."))
minpaydays = 5

## read
def readinput(filename):
    a = open(filename, 'r')
    a_read = a.read()
    return int(a_read)
    a.close()
    
## days
today = readinput('jsb2_randtest_today.txt')

## streak
streakbegins = readinput('jsb2_randtest_streakbegins.txt')
streakbegins_update = streakbegins

## accounting
lastpay = readinput('jsb2_randtest_lastpay.txt')
lastpay_update = lastpay

## figure out account length
if lastpay < streakbegins:
    accountbegins = streakbegins
    print("User was last paid before he began his new streak.")
else:
    accountbegins = lastpay
    print("User was last paid as he continued his streak.")

accountlength = today - accountbegins

## joint
babyjoint = readinput('jsb2_randtest_joints.txt')
j_count_original = babyjoint
print("Previous Balance:")
print(babyjoint)

j_pay = 0
j_count_update = j_count_original

if accountlength > minpaydays - 1:
    j_pay = int(accountlength/minpaydays)     
    j_count_update = j_count_original + j_pay
    print("Current Joint Balance:")
    print(j_count_update)

    dayremainder = accountlength%minpaydays
    lastpay_update = today - dayremainder
    print("Last pay day ID update:")
    print(lastpay_update)
else:
    print("Current Joint Balance")
    print(j_count_update)
    
if smokeboolean > 0:
    j_count_update = j_count_update - 1
    streakbegins_update = today
    print("Streak begins day ID update:")
    print(streakbegins_update)
    print("You requested permission to smoke a joint.")
    print("If you smoke per requested, your remaining joint balance will be:")
    print(j_count_update)
else:
    print("Good streak! Your streak which began " + str(today - streakbegins_update) + " days ago continues")
    
    ## write streakbegins
    babyID_streakbegins = str(streakbegins_update)
    e = open('jsb_streakbegins.txt', 'w')
    e_write = e.write(babyID_streakbegins)
    e.close()

##### projecting forward to see first day of payterm
print("%%%%%%%%% Next round, the accounting term begins on:")
if lastpay_update < streakbegins_update:
    print("%%%%%%%%% Streak begins")
else:
    print("%%%%%%%%% Lastpay")

###############################################################################
############################ T E S T _ 0 1 ####################################
###############################################################################

## a function that has one program (one return) to test if JOINT NUMBER output is correct
def test_01(a, b):
    if a < minpaydays and b == 0:
        return 0 # compare with (babyjoint - j_count_original) at the end
    if a < minpaydays and b == 1:
        return -1
    if a >= minpaydays and b == 0:
        return j_pay
    if a >= minpaydays and b == 1:
        return j_pay - 1

## call a function?
j_check = test_01(accountlength, smokeboolean)
test_01_is = j_check == (j_count_update - j_count_original)
print("@@@@@@@@@ Internal test of joint number:")
print("@@@@@@@@@ " + str(test_01_is))


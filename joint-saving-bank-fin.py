##babybaby
##baby-prefix denotes variable in external storage
##list of baby-variables: 1. babystreakbegins 2. babylastpayday 3. babyjoint

import calendar
import datetime
from datetime import date
from datetime import timedelta

## input
smokeboolean = int(input("smokey baby? (yes = 1/no = 0)"))

##### test input
print(smokeboolean)

## days
todayis = date.today()
#try changing today's date, todayis = date(2018, 6, 20)
programbegins = date(2018, 5, 2)
programlength = todayis - programbegins
dayID_todayis = programlength.days
todayis = dayID_todayis

##### test days
print("Program begins on (type=date):")
print(programbegins)

print("Today dayID (type=int):")
print(todayis)

## streak

a = open('jsb_streakbegins.txt', 'r')
a_read = a.read()
a.close()

babydayID_streakbegins = int(a_read)
streakbegins = babydayID_streakbegins

streaklength = todayis - streakbegins

streakbegins_update = streakbegins 

# to pass update variable for projecting test 
streakbegins_update = streakbegins

##### test streak
print("Streak begins on (type=date):")
print(programbegins + timedelta(days=streakbegins))

print("Streak begins on day(type=int):")
print(babydayID_streakbegins)

print("Current streak length (type= int):")
print(streaklength)


## accounting

b = open('jsb_lastpay.txt', 'r')
b_read = b.read()
b.close()

babydayID_lastpay = int(b_read)
lastpay = babydayID_lastpay

if lastpay < streakbegins:
    accountbegins = streakbegins
    print("//use streakbegins as accountbegins")
else:
    accountbegins = lastpay
    print("//use lastpay as account begins")

accountlength = todayis - accountbegins

# to pass update variable for projecting test
lastpay_update = lastpay

##### test accounting
print("Last pay was on (type=date):")
print(programbegins + timedelta(days=lastpay))

print("Last pay was on (type=int):")
print(lastpay)

print("Account length to be paid (type=int):")
print(accountlength)

## joint
c = open('jsb_joints.txt', 'r')
read_c = c.read()
c.close()

babyjoint = int(read_c)
j_count_original = babyjoint

j_pay = 0
j_count_update = j_count_original

if accountlength > 4:
    j_pay = int(accountlength/5)     
    j_count_update = j_count_original + j_pay

    dayremainder = accountlength%5
    lastpay_update = todayis - dayremainder

    ## write lastpay
    babyID_lastpay = str(lastpay_update)    
    d = open('jsb_lastpay.txt', 'w')
    d_write = d.write(babyID_lastpay)
    d.close()

if smokeboolean > 0:
    j_count_update = j_count_update - 1
    streakbegins_update = todayis

    ## write streakbegins
    babyID_streakbegins = str(streakbegins_update)
    e = open('jsb_streakbegins.txt', 'w')
    e_write = e.write(babyID_streakbegins)
    e.close()
    
## write joint
babyjoint = str(j_count_update)    
f = open('jsb_joints.txt', 'w')
f_write = f.write(babyjoint)
f.close()

##### test joint
print("Old Joint Balance:")
print(j_count_original)
print("Joint earned:")
print(j_pay)
print("New Joint Balance:")
print(babyjoint)

##### projecting forward to see first day of payterm
print("Next round, the accounting term begins on:")
if lastpay_update < streakbegins_update:
    print("streakbegins")
else:
    print("lastpay")

###############################################################################
############################ T E S T _ 0 1 ####################################
###############################################################################

## a function that has one program (one return) to test if JOINT NUMBER output is correct
def test_01(a, b):
    if a < 5 and b == 0:
        return 0 # compare with (babyjoint - j_count_original) at the end
    if a < 5 and b == 1:
        return -1
    if a >= 5 and b == 0:
        return j_pay
    if a >= 5 and b == 1:
        return j_pay - 1

## call a function?
j_check = test_01(accountlength, smokeboolean)
test_01_is = j_check == (j_count_update - j_count_original)
print("Test of joint number:")
print(test_01_is)


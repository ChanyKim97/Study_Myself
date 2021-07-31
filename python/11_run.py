# import calculator as calc

# print(calc.add(1,2))

from calculator import add

print(add(2,5))

#standard library

import math

print(math.log10(100))
print(math.cos(0))
print(math.pi)

import random

#0.0 부터 1.0
print(random.random())
print(random.randint(1,20))
#1<=        <=20
print(random.uniform(1,20))
#사이 소수

import os
print(os.getlogin())
print(os.getcwd())

import datetime
pi_day = datetime.datetime(2021,7,30,13,4,59)
print(pi_day)
today = datetime.datetime.now()
print(today)

print(today - pi_day)

timedelta = datetime.timedelta(days=2, hours=3, minutes=3, seconds=3)
print(today+timedelta)
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10
if number == 0:
    print ("Last digit of {} is {} and is 0".format(number, number))
elif lastdigit > 5:
    print ("Last digit of {} is {} and is grater than 5".format(number, lastdigit))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, lastdigit))

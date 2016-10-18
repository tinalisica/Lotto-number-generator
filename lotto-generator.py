# -*- coding: utf-8 -*-.

print "Welcome to the Lottery numbers generator."

how_many_numbers = raw_input("Please enter how many random numbers would you like to have:")

from random import randint

list=[]
for p in range (0, int(how_many_numbers)):
    lotto_number=randint(1, 39)
    list.append(lotto_number)

print list













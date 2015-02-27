#! /usr/bin/env
# Random Dice Generator

import random
from random import SystemRandom
import argparse

# Parsing
parser = argparse.ArgumentParser(description='Calculate Dice throws')
parser.add_argument("XdY", help="Do a normal XdY+Z roll and find the sum",
                    type=str)
parser.add_argument("-a","--advantage", help="Roll with advantage mechanic",
                    action="store_true")
parser.add_argument("-r","--altrandom", help="Use python randomness instead of OS randomness (Faster)",
                    action="store_true")
parser.add_argument("-e","--experiment", help="Experimentall calculate the distribution of values from dice rolls",
                    action="store_true")

args = parser.parse_args()

# Functions
def singleroll(sides): # Roll one die with x sides
    if args.altrandom:
        x = random.randint(1,int(sides))
    else:
        x = SystemRandom().randint(1,int(sides))
    return x

def advantage(sides): # Advantage mechanic for dnd 5e
    x = []
    if args.advantage:
            for i in range(2):
                y = singleroll(sides)
                x.append(y)
                output = max(x)
    else:
        output = singleroll(sides)
    return output

def bulkroll(qnty,sides):
    x=0
    for i in range(int(qnty)):
        y = advantage(sides)
        x = x + y
    return x

def makelist(qnty,sides):
    x = []
    for i in range(qnty*sides-qnty+1):
        x.append(0)
    return x

# Setting up dice input
input = args.XdY.lower()

# Optional addition onto the roll
addon = 0
if input.find("+") != -1:
    addon = int(input[input.find("+")+1:])
    input = input[0:input.find("+")]

# Separate input into basic parts
qnty = int(input[0:input.find("d")])
sides = int(input[input.find("d")+1:])

if args.experiment: # Experimental Array
    asize = int(raw_input("How many interations? ").strip())
    list = makelist(qnty,sides)
    for i in range(asize):
        x = bulkroll(qnty,sides)
        list[x-qnty] = list[x-qnty]+1
    print "Value"+"  "+"Qnty"
    for i in range(len(list)):
        print str(i+qnty)+"   "+str(list[i])      
else: # Normal dice roll
    result = bulkroll(qnty,sides)
    print result + addon

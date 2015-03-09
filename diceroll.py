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
parser.add_argument("-e","--experiment", type=int, help="Experimentally calculate the distribution of values from dice rolls")

args = parser.parse_args()

# Functions
def singleroll(sides): # Roll one die with x sides
    if args.altrandom:
        x = random.randint(1,int(sides))
    else:
        x = SystemRandom().randint(1,int(sides))
    return x

# Do a roll and take the maximum numb of rolls qnty>=numb
## For this function, advantage is qnty=2 and numb=1
def rollmaximum(sides,qnty = 1,numb = 1,takesum = True):
    x = []
    for i in range(qnty):
            y = singleroll(sides)
            x.append(y)
    x = sorted(x, reverse = True)
    if takesum:
        return sum(x[0:numb])
    else:
        return x[0:numb]

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
    x = 0
    rollsum = 0
    while x<qnty:
        y = advantage(sides)
        rollsum = rollsum + y
        x=x+1
    return rollsum

def makelist(qnty,sides):
    x = []
    for i in range(qnty*sides-qnty+1):
        x.append(0)
    return x

def rollarray(qnty,sides):
    asize = args.experiment
    list = makelist(qnty,sides)
    x=0
    rollsum = 0
    while x<asize:
        y = bulkroll(qnty,sides)
        list[y-qnty] = list[y-qnty]+1
        x = x+1
    print "Value"+"  "+"Qnty"
    for i in range(len(list)):
        print str(i+qnty)+"   "+str(list[i]) 

### Begin XdY+Z anaylsis
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

### End XdY+Z analysis

if args.experiment is not None: # Experimental Array
    rollarray(qnty,sides)     
else: # Normal dice roll
    result = bulkroll(qnty,sides)
    print result + addon

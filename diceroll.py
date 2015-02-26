# Random Dice Generator

import random
from random import SystemRandom
import argparse

# Parsing
parser = argparse.ArgumentParser()
parser.add_argument("normal", help="Do a normal XdY+Z roll and find the sum",
                    type=str)
parser.add_argument("-a","--advantage", help="Roll with advantage mechanic",
                    action="store_true")
parser.add_argument("-r","--altrandom", help="Use python randomness instead of OS randomness",
                    action="store_true")

args = parser.parse_args()

# Functions
def howto():
    print './diceroll.py XdY+C [args]'

def singleroll(sides): # Roll one die with x sides
    if args.altrandom:
        x = random.randint(1,int(sides))
    else:
        x = SystemRandom().randint(1,int(sides))
    return x

def advantage(sides): # Advantage mechanic for dnd 5e
    x = []
    for i in range(2):
        y = singleroll(sides)
        x.append(y)
    return max(x)

def bulkroll(qnty,sides):
    x=0
    for i in range(int(qnty)):
        y = singleroll(sides)
        x = x + y
    return x

# Setting up dice input
input = args.normal.lower()

# Optional addition onto the roll
addon = 0
if input.find("+") != -1:
    addon = int(input[input.find("+")+1:])
    input = input[0:input.find("+")]

# Separate input into basic parts
qnty = input[0:input.find("d")]
sides = input[input.find("d")+1:]

# Basic dice roll
result = bulkroll(qnty,sides)
print result + addon

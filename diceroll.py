# Random Dice Generator

import random
from random import SystemRandom

cont = "y"
while cont.strip() == "y":
    input = raw_input("Input X dice with Y sides (XdY): ").lower()
    qnty = input[0:input.find("d")]
    sides = input[input.find("d")+1:]
    x=0
    for i in range(int(qnty)):
        A = SystemRandom().randint(1,int(sides))
        x = x + A
        print "Roll",i,"is",A
    
    print "Result of rolling",qnty,"dice, with",sides,"sides each, is:",x

    cont = raw_input("Roll again? (y/n) ").lower()

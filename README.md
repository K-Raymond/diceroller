# Diceroller

For large quantities of dice rolls!

Uses Python 2.7, have not tested 3.x

This is a simple script to roll a large quantity of a dice that have an arbitrary number of sides.
For example,
```
Input X dice with Y sides (XdY): 3d6
Roll 0 is 6
Roll 1 is 5
Roll 2 is 2
Result of rolling 3 dice, with 6 sides each, is: 13
Roll again? (y/n) 
```

The program itself can be easily modified to suit whatever needs, as it is very simple.

Future versions may have more options for different types of dice rolls, perhaps even game specific features.
(ie, advantage from dnd: roll two dice and take the highest of the two)
```
d1 = SystemRandom().randint(1,int(sides))
d2 = SystemRandom().randint(1,int(sides))
A = max(d1,d2)
```

# diceroller

This is a basic dice roller program built in python 2.7.x

To X number of dice with Y sides, just run as,
```
python diceroller.py XdY
```
If you wish to add a number to the resulting roll you can simply just,
```
python diceroller.py XdY+Z
```
There are also analyitics that you can run on a range of dice rolls.
For instance, if you wanted to roll 2d6 and wanted to collect a large number of rolls to experimentally determine the probablility of rolling a particular value, simply,
```
python diceroller.py 2d6 -e [samplesize]
```
samplesize can be an ungodly number, like `10**10`.

Happy rolling!
==========
# Future features may include,
1. Analytics
  1. Calculating probablilities from a general formula
  2. Better formatting for analytics output
2. Types of rolls
  1. Particular types of rolls for different games
  2. Pick X highest dice out of Y rolls
>>>>>>> origin/dev

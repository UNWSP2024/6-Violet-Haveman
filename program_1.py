
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.

def randDice():
    sum = 0.0
    # Write your logic to generate 2 numbers between 1 and 6 here

    import random
    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)
    # Sum 2 numbers
    print ("First Dice =", roll_1)
    print ("Second Dice =", roll_2)
    tot = roll_1 + roll_2
    # return sum to calling function
    print ("Sum of Both Dice =", tot)
    return sum
randDice()
#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
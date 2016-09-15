#!/usr/bin/python
import sys
import math
from MyPRNG import *

# EX. guess.py -h -v -s seed -m 1 -M 400

def GuessHandler(userGuess,count, randomNumber):
    # Takes care of current guess by storing it in an array and takes the absolute value of the difference
    # Handles the previous guess as well to compare to see if it was warmer or colder
    currentGuessDifference = userGuess[count] - randomNumber
    currentGuessDifference = math.fabs(currentGuessDifference)
    previousGuessDifference = userGuess[count - 1] - randomNumber
    previousGuessDifference = math.fabs(previousGuessDifference)

    # If the current guess is smaller then it will return true which means they are approaching the random number
    if (currentGuessDifference < previousGuessDifference):
        return True
    else:
        return False

def main():
    prng = MyPRNG()
    count = 0
    randomNumber = 0
    verbose = False
    loop = True
    userGuess = []
    minimum = 1
    maximum = 1000
    seed = 101
    index = 0
    hMessage = "This program will create a game which runs the PRNG to pick the 101st random number for the user to guess"


    for currentArg in sys.argv:
        if (currentArg == "-h"):
            print (hMessage)
        elif (currentArg == "-v"):
            verbose = True
        elif (currentArg == "-s"):
            seed = int(sys.argv[index + 1])
        elif (currentArg == "-m"):
            minimum = int(sys.argv[index + 1])
        elif (currentArg == "-M"):
            maximum = int(sys.argv[index + 1])
        index += 1

    prng.seed(seed)
    randomNumber = prng.next_prn()

    while(loop):
        userGuess.append(int(input(">> ")))
        if( (userGuess[count] > randomNumber) or (userGuess[count] < randomNumber) ):
            if(GuessHandler(userGuess, count, randomNumber)):
                print("warmer")
            else:
                print("colder")
        if (userGuess[count] == randomNumber):
            print("winner")
        if (userGuess[count] == 0):
            loop = False
        count += 1
if __name__ == "__main__":
    main()

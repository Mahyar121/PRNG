#!/usr/bin/python3
import sys
import math
import time
from MyPRNG import *
# Author: Mahyar Haji Babaie
# Email: mahyarhajibabaie@csu.fullerton.edu
# This file uses a guesshandler to handle the warmer and colder, it also allows command line arguments
# It will use functions from the MyPRNG class to generate a random number


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
# This function is invoked when -h is involved in the commandline for when a user needs help on how to use the program
def Usage():
    print("Usage: ", sys.argv[0], "[-h] [-v] [-s seed] [-m min number] [-M max number")
    print("This program will create a game which runs the PRNG to pick the 101st random number for the user to guess.")
    print("If you don't use the command line, the answer could have up to 2 decimal places ex. 100.25")

def main():
    prng = MyPRNG() #declaring a variable to handle MyPRNG class functions
    count = 0 #initiliazing the userGuess array value to 0
    randomNumber = 0 #initalizing the randomNumber value to 0
    loop = True #initializing the loop value to True so the while loop can begin
    userGuess = [] #initliazing a list to store the user guesses
    minimum = 1 #This variable will accept the command line argument for -m
    maximum = 1000 #This variable will accept the command line argument for -M
    seed = time.time() #This variable will accept the command line argument for -s seed
    index = 0 #This is used to loop through the sys.argv[index]
    guessNumber = 0
    for currentArg in sys.argv:
        if (currentArg == "-h"):
            Usage() #will print the help features
        elif (currentArg == "-v"):
            print("This message means you are in debugging mode")
        elif (currentArg == "-s"):
            if (index+1 < len(sys.argv)):
                seed = int(sys.argv[index + 1]) #if there is a seed set it to the variable
            else:
                seed = time.time(); #otherwise use this default value
        elif (currentArg == "-m"):
            if (index+1 < len(sys.argv)):
                minimum = int(sys.argv[index + 1]) #if there is a minimum number set it to the variable
            else:
                minimum = 1 #otherwise use this default value of 1
        elif (currentArg == "-M"):
            if(index+1 < len(sys.argv)):
                maximum = int(sys.argv[index + 1]) #if there is a maximum number set it to the variable
            else:
                maximum = 1000 #otherwise use this default value of 1000
        index += 1 #increment the index so we can keep looping through the sys.argv[index]

    #initliazes the seed value and generates a random number
    prng.seed(seed)
    for x in range (101):
        randomNumber = prng.next_prn()
    guessNumber = (maximum - minimum) + 1
    guessNumber = randomNumber % guessNumber
    guessNumber = guessNumber + minimum
    randomNumber = guessNumber

    while(loop):
        response = int(input("Guess a number or press 0 to quit "))
        userGuess.append(response)
        if( (userGuess[count] > randomNumber) or (userGuess[count] < randomNumber) ):
            if(GuessHandler(userGuess, count, randomNumber)): #if GuessHandler returns true then they are warmer
                print("warmer")
            else:
                print("colder") #otherwise they are colder
        if (userGuess[count] == randomNumber):
            print("winner") #if they choose the correct number they win
            loop = False
        if (userGuess[count] == 0): #they can type 0 to quit
            loop = False
        count += 1
if __name__ == "__main__":
    main()
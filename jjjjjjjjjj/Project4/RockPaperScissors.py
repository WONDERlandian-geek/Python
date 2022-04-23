'''
The Objective of this program is to make a Rock, Paper, Scissors game for the user to play against the computer.

@author: Wonder Pries
'''

import random


keepPlaying = True

While(keepPlaying):

    print("Welcome to Rock Paper Scissors! Best two out of three. Press 'q' to quit.")
    
    userScore = 0
    cpuScore = 0
    
    While(userScore < 2) and (cpuScore < 2):
        
        userChoice = input("Rock, Paper, or Scissors? Or q?").lower()
        
        list = ["rock", "paper", "scissors"]
        cpuChoice = random.choice(list)
        
        #This statement checks to see if the user and CPU tied.
        If((userChoice == "rock" and cpuChoice == "rock") or (userChoice == "paper" and cpuChoice == "paper") or (userChoice == "scissors" and cpuChoice == "scissors")):
            print("DRAW")
            print("User: " + str(userScore) + " CPU: " + str(cpuScore))
        
        #This statement checks to see if the user wins
        Elif((userChoice == "rock" and cpuChoice == "scissors") or (userChoice == "paper" and cpuChoice == "rock") or (userChoice == "scissors" and cpuChoice == "paper")):
            userScore = userScore + 1
            print("User Won")
            print("User: " + str(userScore) + " CPU: " + str(cpuScore))
            
        #This statement checks to see if the CPU wins
        Elif((userChoice == "rock" and cpuChoice == "paper") or (userChoice == "paper" and cpuChoice == "scissors") or (userChoice == "scissors" and cpuChoice == "rock")):
            cpuScore = cpuScore + 1
            print("CPU Won")
            print("User: " + str(userScore) + " CPU: " + str(cpuScore))
        
        #This statement checks to see if the user quit
        Elif(userChoice == "q"):
            break
        
        #This statement checks to see if the user entered a nonviable option
        Else:
            print("Not an option, try again.")
    
    print("Thanks for playing!")
    
    If(userScore == 2):
        print("You win!")
    
    If(cpuScore == 2):
        print("CPU wins!")
    
    print("User: " + str(userScore) + " CPU: " + str(cpuScore))
#getting and using a package (code soemone else wrote)
import random

#num is a variable name 
num = random.randint(1, 10)
#variable assignment
guess = None 

# != and == are comaparision operators
while guess != num:
    #indentation has meaning in python 
    guess = input("guess a number between 1 and 10: ")#collecting user input 
    guess = int(guess) #type conversion 

    if guess == num:
        print("congratulations! you won!")
        break #loop keyword
    else:
        print("nope, sorry. try again!")#terminal output

#for loop and while loop are called as conditional statements 

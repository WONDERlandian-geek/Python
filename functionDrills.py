'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by putting in some parameters
and printing what is returned outside of the function.

EXAMPLE TASK:
'''
#EX) Define a function that has two parameters. Make the function add the two
#numbers together and return the result.
from builtins import True, False
from test.subprocessdata.sigchild_ignore import num_polls
from test.test_unparse import for_else
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that has two int parameters. Make the function subtract 
#the first parameter minus the second one. Then, return the result. Now call 
#the function.
#Print what the function returns.

def subract_int(num1, num2):
    subtract_int = num1 - num2
    return(subtract_int)

subtract_int(num1, num2)
print(subtract_int)

#2) Define a function that has one parameter. Make the function divide the 
#parameter by 2, multiply it by 77, and then add 10,000. Return the result.
#Now call the function.
#Print what the function returns.

def drill_2(num1):
    a = num1 / 2
    b = a * 77
    drill_2 = b + 1000
    return(drill_2)

drill_2(num1)
print(drill_2)

#3) Define a function that has two int parameters. Make the function check if 
#two numbers are equal. If they are equal, return true. If they are not equal, 
#return false. Now call the function.
#Print what the function returns.

def equal(num1, num2):
    If (num1 == num2):
        return(True)
    Else:
        return(False)

equal(num1, num2)
print(equal)

#4) Define a function that has two int parameters. Make the function
#check which parameter is bigger, and return the bigger parameter. 
#If they are the same, it should just return either parameter. Now call the 
#function.
#Print what the function returns.

def bigger(num1, num2):
    If (num1 < num2):
        return(num1)
    Elif (num1 > num2):
        return(num2)
    Else:
        return(num1 or num2)

bigger(num1, num2)
print(bigger)

#5) Define a function that has two string parameters. Make the function
#add the two strings together. And then return the combined string. Now call 
#the function.
#Print what the function returns.

def string(str1, str2):
    string = str1 + str2
    return(string)

string(str1, str2)
print(string)

#6) Define a function that has three int parameters. If the first number is 
#equal to the second OR the third number, return true. Else, return false. Now 
#call the function.
#Print what the function returns.

def equal_2 (num1, num2, num3):
    If (num1 == num2) or (num1 == num3):
        return(True)
    Else:
        return(False)
    
equal_2(num1, num2, num3)
print(equal_2)

#7) Define a function that prints your name. It should have no parameters and 
#shouldn't return anything. Now call the function.

def name("Wonder"):
    print(name)

name("Wonder")

#8) Define a function that has one string parameter. The string should be a
#color. If that string is equal to your favorite color, it prints "That's my 
#favorite color!". If it is not, it prints "That is not my favorite color. 
#Try again.". It shouldn't return anything. Now call the function.

def color("teal"):
    If (color == "maroon"):
        "That's my favorite color!"
    Else:
        "That is not my favorite color. Try again."

color("teal")

#9) Define a function that has one int parameter. The int should be 
#positive. If the number is not equal to zero, the function runs a loop that
#decrements the parameter by 1 and prints it each time. Now call the function.

def zero(num1):
    While (num1 > 0)
    
        print(num1)
        
        num1 = num1 - 1

zero(num1)

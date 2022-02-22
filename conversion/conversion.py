'''
This program will calculate different conversions.
By Wonder Pries
'''

#Use input() to get the number of miles from the user. And store
#that int in a variable called miles.

miles = int(input("How many miles would you like to input?"))

#Convert miles to yards, using the following:
# 1 mile = 1760 yards.
#
#Store the value in a variable called yards and print it out with a 
#simple statement.

yards = miles * 1760
string = " miles converts to "
sentence = str(miles) + string + str(yards) + " yards."
print(sentence)

#Convert miles to feet, using the following:
# 1 mile = 5280 feet.
#
#Store the value in a variable called feet and print it out with a 
#simple statement.

feet = miles * 5280
string = " miles converts to "
sentence = str(miles) + string + str(feet) + " feet."
print(sentence)


#Convert miles to inches, using the following:
# 1 mile = 63,360 inches.
#
#Store the value in a variable called inches and print it out with a 
#simple statement.

inches = miles * 63360
string = " miles converts to "
sentence = str(miles) + string + str(inches) + " inches."
print(sentence)

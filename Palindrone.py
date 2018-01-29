'''
Created on Jan 29, 2018

@author: Mike Noble
'''
# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)


# Ask user to enter a string. allocate input to a variable
str = raw_input("Enter a string")
# create an empty list
str2 = []

# loop through string backwards and apply contents to second empty list
for i in range(len(str),0,-1):
    str2.append(str[i-1])

# compare each element of each list. If elements match then add 1 to a counter
count = 0
for i in range(len(str)):
    if (str[i] == str2[i]):
        count = count +1
       
# If the value of the counter is equal to the length of the string then it is a palindrome. 
# Inform user of result
if (count == len(str)):
    print "your string is a palindrome"
else:
    print "your string is NOT a palindrome"

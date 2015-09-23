# Nicole Ignasiak
# CIS 125 82A
# Week Three Assignment
# StarWarsAssignment.py
# September 25, 2015

# Write a program that does the following steps:  
# 1. Prompt the user to input their First and Last name and their mother's maiden name and the city where they where born.  
# 2. Calculate their "Star Wars" name.  
# 3. Print out their "Star Wars" name.


First = input("What is your first name? ")                            
Last = input("What is your last name? ")
Mother = input("What is your mother's maiden name? ")
City = input("What is the name of the city where you were born? ")

StarWarsFirst = Last[:3] + First[:2]                                            # Makes Star Wars First Name
StarWarsLast = Mother[:2] + City[:3]                                            # Makes Star Wars last name

print (StarWarsFirst.capitalize(), StarWarsLast.capitalize())                   # Capitalizes the first letter in each name
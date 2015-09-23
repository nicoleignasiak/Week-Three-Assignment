# Nicole Ignasiak
# CIS 125 82A
# Week Three Assignment
# PigLatin.py
# September 25, 2015

# Write a program to the following specifications:  
# 1. The program should prompt the user to enter an English word to translate.  
# 2. The program should translate the word in to Simple Pig Latin, given the following rules.  
# 3. The program should print the translated word.

Word = input("Enter a word in english that you would like to translate: ")

vowels = "aeiouAEIOU"                                                           # I solved the case sensitivity by not only adding the vowels to be tested in lower case but also in upper case. This allows the words to work no matter the capilization.

if Word[0] in vowels:                                                           # If the first letter is a vowel then
    print((Word + "yay").capitalize())                                          # Print the word plus "yay"
else:                                                                           # If the first letter is a consonant then
    print((Word[1:] + Word[0] + "ay").capitalize())                             # Print the word minus the first letter, then the first letter, then "ay"
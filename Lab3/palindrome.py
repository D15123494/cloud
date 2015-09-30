#!/usr/bin/python3
'''This method determine if the word is a palindrome or not
	param : string is the word to test
	return : true if the word is a palindrome, otherwise false
'''
def isPalindrome (word):
  return word==word[::-1]


cont = True
print ("welcome in the palindrome programm")
while(cont):
  word = input("Please enter a word : ")
  if isPalindrome(word):
    print ("it's a palindrome")
  else :
     print("it's not a palindrome")
  word = input("do you want to continue : (Y/N)")
  if word == 'N':
    cont = False
print ("bye see you soon")

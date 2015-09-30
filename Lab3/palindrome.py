#!/usr/bin/python3
'''This method determine if the word is a palindrome or not
	param : string is the word to test
	return : true if the word is a palindrome, otherwise false
'''
def isPalindrome (word):
  return word==word[::-1]


cont = True

while(cont):
  word = input("Please enter a word : ")
  print (isPalindrome(word))
  word = input("do you want to continue : (Y/N)")
  if word == 'N':
    cont = False

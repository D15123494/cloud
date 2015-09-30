#!/usr/bin/python3

def isPalindrome (word):
  return word==word[::-1]


cont = True

while(cont):
  word = input("Please enter a word : ")
  print (isPalindrome(word))

#!/usr/bin/python3

x=1
y=2

evenSum = 0
while y<=4000000:
  oldx=x
  x=y
  y+=oldx
  if x%2==0:
    evenSum+=x

print (evenSum)

#!/usr/bin/python3
resultat = 0
for i in range (1000):
  if i%3 == 0 or i%5 == 0:
    resultat += i

print (resultat)
exit(0)

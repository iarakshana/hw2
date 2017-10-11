#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.

N = 101 #the 101 is not required for this solution method
from math import factorial
# Apparently there is a straight factorial function itself so I just used that instead of actually
#writing it out fully, hope that is alright

#In order to get all the possible paths it is best to use the combinations formula as discussed in the discussion board so
#I just defined a combinations formula in solutions and set n and r to 200 and 100 respectively

#It is important to double the n to account for the total number of movements, i.e. right and down in order
#to reach the diagonal end,hence 200. r is 100 because it is just the right movements in the question

n=200
r=100
solution = (factorial(n) // (factorial(r) * factorial(n - r))) #Used // for integer division as was suggested in the discussion board
#as was getting the exponential form with just /

print(solution)

# Check for the correct answer.
if N == 101:
  print("#6 : Grid ::", "Correct." if solution == 90548514656103281165404177077484163874504589675413336841320 else ("Wrong: " + str(solution)))

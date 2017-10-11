#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0
multiple = 0

i = 1
for i in range(1,100000):# range has to start from 1 otherwise 0 is also counted in the list so the 9th multiple will be different
    if (i % 4 == 0) and (i % 13 == 0) and (i % 14 == 0) and (i % 26 == 0) and (i % 50 == 0): #we have to use and because
        #question asks 9 multiple of all the numbers not if it is a multiple of any of the numbers
        multiple += 1
        if multiple == 9: #we use break so that the computation stops after the 9th check
            solution = i
            break
    i += 1


# Check for the correct answer.
if multiple == 9:
  print("#1 : 9th Multiple ::", "Correct." if solution == 81900 else ("Wrong: " + str(solution)))

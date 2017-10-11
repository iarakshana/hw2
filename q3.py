#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0
number   = 175832868806

#Using the code for not_prime in the lecture notes and setting prime as is not not_prime, we get the set for prime under 300
not_prime = {j for i in range(2,   300)
               for j in range(i*2, 300, i)}

prime = ([x for x in range(2,300) if x not in not_prime])

for i in prime:
    if (number%i == 0) : #to find if the numbers in the list of primes is a factor of 175832868806, we use the mod function
        solution += 1 #if the mod is 0 we add 1 to our solution list which gives us that there are only 6 prime factors
print(solution)

# Check for the correct answer.
if number == 175832868806:
  print("#3 : Count Prime Factors ::", "Correct." if solution == 6 else ("Wrong: " + str(solution)))

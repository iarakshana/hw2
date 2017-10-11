#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.
solution = 0     # solution is the variable to hold the sum, i.e. our answer
max_fib  = 1e9
a = 1;   # First number
b = 1;   # Second number

# While the second number is less than 1e9
# We set 1e9 as the max value for b so that we can only get the sum till 1e9 as requested in the question
while b < 1e9:
    # Incrementing the numbers in order to obtain the Fibonacci sequence as in the class notes
    o = a
    a = b
    b = a + o

    # If the number is divisible by 17, we add it to our solution
    if(a%17 == 0): # The mod function helps find what is divisible or not divisible
        solution += a

print('The sum is: ' + str(solution))

# Check for the correct answer.
if max_fib == 1e9:
    print("#2 : Fibonacci ::", "Correct." if solution == 15129388 else ("Wrong: " + str(solution)))

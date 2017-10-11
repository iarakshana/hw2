#!/usr/bin/env python 

# The 'solution' variable should hold the
# solution when the script is done.
def collatz(n): #We add a count to the function definition in the question so that when n is greater than 1, we add 1 to each count
    count = 0
    while n>1:
        count += 1
        if n %2 == 0:
            n = n/2
        else:
            n = (3*n) + 1
    return count

def get_max_collatz(max_num):#We define another function to get the max that counts the max number in our range of 2000000
    counts = [0]*max_num
    for i in range(max_num):
        counts[i] = collatz(i+1) # this keeps going until we reach 1 we require in the collatz function

    max_count = max(counts)
    max_val = counts.index(max_count) + 1

    return max_val

get_max_collatz(2000000)
solution = get_max_collatz(2000000) #Please note that it takes quite a long time for this code to run
print(solution)

if max_start == 2000000:
  print("#7 : Collatz Sequence ::", "Correct." if solution == 1723519 else ("Wrong: " + str(solution)))

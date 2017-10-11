#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.
for a in range(1,1000): #Since in pythagorean triples a<b<c, we can set the ranges as such so that b starts from a till 1000 and
    #similarly c starts from b till 1000
    for b in range(a,1000):
        for c in range (b, 1000):

            if (a+b+c == 1000) and (a*a + b*b == c*c):
# here we set the two conditionals and say that of true then solution is 
#the product of a,b and c
#I'm not sure if there is a better way to do it because it took soooo long to run and don't really know why but
#it still produced the answer - maybe it was the multiple interation ranges but that seemed the most logical
                   solution = (a*b*c)
print(solution)


# Check for the correct answer.
print("#5 : Pythagorean Triplet ::", "Correct." if solution == 31875000 else ("Wrong: " + str(solution)))

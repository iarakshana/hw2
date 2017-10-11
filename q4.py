#!/usr/bin/env python

long_number = '''1334689116556462941882035808943573171674164401363769460864490234588978262666944913475783756741523897245184207879400801772948519107022172112703850995250828017643114989532341638256433902974862681950869909550724964438670365005594138770568327987006988181115098238786559343074732216472150049113865859400036834001396323915862736324118712200726467082136557785333250304970064033489578066450615899117582800671492006891892806304956446965790733095470234925553972275220958407990275926200444595858581681275746318089599931238390577959492535670612451917097856204279936698818808473734179069393970559180304303301694835535657388574351479006304909345090039619401560275818621377887855535660203417104398980782823962234208247262452130875884319383852931728105858548604792291573328992559286762014408216849863235232618879146570156278193016458175265873338775411585800402047649148239253335046636431821919485725262483287374052121386952248950622806575169311906365131300057110279941542555942008569206742619537842879039448112019071'''

#First we define our function 'findproduct' that basically finds the product of two consecutive digits in our long number
def findproduct(numString):
    product = 1
    for i in range(len(numString)):
        product = product * int(numString[i])
    return product

# The 'solution' variable should hold the
# solution when the script is done.
# these are the variables that we start with as given in question
solution = 0
product = 0
length = 12

# We then use our findproduct function on all the sets of 12 consecutive numbers in our 1000 digits and if the product that
# is got in the product variable assigned is bigger than our solution, it gets assigned to the solution and we get our answer
# Iterate over the 1000 digits except for the end digits
# For each iteration find the string of numChar length and
#  pass it to the function to find product
for i in range(1000-length):
    product = findproduct(long_number[i:i+length]) # goes through all elements of long_number from start to start plus 12 (length in q)
    # and finds the product and stores it in product
    # it keeps finding the product of 12 consecutive numbers until it is greater than the solution, when the that happens it
    #stores it in solution giving us the answer
    if (product > solution):
        solution = product

print(solution)

# Check for the correct answer.
if length == 12:
  print("#4 : Consecutive Product ::", "Correct." if solution == 2257403904 else ("Wrong: " + str(solution)))

# Python 

You can join this assignment, [here](https://classroom.github.com/assignment-invitations/39f415bb7b155b439c113add0f03f21c).  It is due October 12 at 1:30am.

### Excitement and Exercises!
There is a 'skeleton' for each of these, in the assignment that you've checked out.
The answers are also there, so that you can check your work.
Fill your code into the existing files, as indicated.
You can run `./hw2_test.py` to check the whole thing.
If everything passes, commit your code (git add, commit, push).
Check your repository online to see that the push was successful.

Remember that you will be graded on correctness, style, and commenting.

When you are done, go to Canvas and take this very short [quiz]().
You will have to make small modifications of your code on the fly.

1. Find the 9th positive integer that is a multiple of 4, 13, 14, 26, and 50.
2. Fibonacci numbers are defined by adding the previous two terms.  Starting with 1 and 1, that gives 1, 1, 2, 3, 5, 8, etc.  Find the sum of all Fibonnacci numbers divisible by 17 and below 1 billion.  (`while` and `if`, and `%`)
3. The number 175832868806 has no prime factors above 300.  Count the unique prime factors.  (Hint: first make a list of all the primes up to 300.  How would you express a prime in python?)
4. There is a 1000-digit number, below.  If you multiply five consecutive digits, the largest value you can find is 9 × 5 × 9 × 9 × 9 = 32805.  Multiplying 12 consecutive digits, what is the largest product you can find?
5. Pythagorean triples have the property _a² + b² = c²_.
   For instance the familiar 3, 4, 5 triangle has 3² + 4² = 9 + 16 = 25 = 5².
   There is one pythagorean triple for which _a + b + c_ = 1000.  Find the product _a × b × c_.
6. In the 2×2 grid shown below, the shortest path between two opposite corners is four units long.
   There are six options for such a path (see below).  For a 100×100 grid, the shortest path is 200 units long.  How many such paths are there? </br>
   Hints: What is necessary for a path to be a "shortest path"?
   Alternative hint: use `import math`.
7. **Challenge:** A Collatz sequence is defined by:
   1. n → n/2 (for even n)
   2. n → 3n + 1 (for odd n)
   Using this rule, for 13, we get: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1.
   Successive links in a Collatz sequence can be expressed in python by the _function_, 
   ```
   def collatz(n):
     if n%2: return 3*n + 1
     else:   return int(n/2)

   link = collatz(link)
   ```

   It is believed that the sequence ends at 1, for all numbers.  What is the longest Collatz sequence that _starts_ below 2 million?</br>
   Double bonus: Use precomputation and recursive functional calls.

![Paths](paths.png?raw=true "Paths")

Here is the 1000-digit number, for exercise 4.
> `1334689116556462941882035808943573171674164401363769460864490234588978262666944913475783756741523897`
> `2451842078794008017729485191070221721127038509952508280176431149895323416382564339029748626819508699`
> `0955072496443867036500559413877056832798700698818111509823878655934307473221647215004911386585940003`
> `6834001396323915862736324118712200726467082136557785333250304970064033489578066450615899117582800671`
> `4920068918928063049564469657907330954702349255539722752209584079902759262004445958585816812757463180`
> `8959993123839057795949253567061245191709785620427993669881880847373417906939397055918030430330169483`
> `5535657388574351479006304909345090039619401560275818621377887855535660203417104398980782823962234208`
> `2472624521308758843193838529317281058585486047922915733289925592867620144082168498632352326188791465`
> `7015627819301645817526587333877541158580040204764914823925333504663643182191948572526248328737405212`
> `1386952248950622806575169311906365131300057110279941542555942008569206742619537842879039448112019071`

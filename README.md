# Collatz_Conjecture
Collatz  conjecture is an unproven idea in mathematics that states any positive integer n with a protocol defined below will eventually come to 1.

if n is even, n = n / 2
if n is odd, n = 3n + 1

Once the value reaches 1, it enters an infinite loop with 1-2-4-1-2-4...

Collatz_Function.py defines and returns number of iterations to reach infinite loop, as well as plotting the values.
Collatz_Series.py  plots the required number of iterations for a range of initial values.

According to Wikipedia, all the numbers up to 10^12 is checked, and the most iteration it took to enter the infinite loop was for the nummber 989345275647, 
which took 1348 iterations.

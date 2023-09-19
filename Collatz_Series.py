#This code plots how many iterations it took to reach infinite loop for a series of numbers from 1 to n

from Collatz_Function import Collatz
import matplotlib.pyplot as plt


A = [] #Number of iterations to reach infinite loop for each number will be saved in this  matrice.
n = int(1e3) #Maximum number that will be checked for Collatz Iterations

for x in range(1, n+1):
    A.append((Collatz(x)))

A_enum = (list(enumerate(A, start=1))) #Enumeration of the result list
#print(A_enum)
plt.plot([z[0] for z in A_enum], [z[1] for z in A_enum])


#Loop to search for the value in which maximum number of iterations needed
maxim_x = 0
maxim_y = 0
for x, y in A_enum:
    if y > maxim_y:
        maxim_x = x
        maxim_y = y

print(f"The largest number of iterations before reaching the infinite loop occured in the number {maxim_x} with {maxim_y} iterations")

text = f"Number of iterationns for initial values up to {n}"
plt.title(text)
plt.xlabel("Initial Value")
plt.ylabel("Number of Iterations")
#plt.savefig(f"{text}", dpi=300)
plt.show()

#This code calculates the number of iterations in Collatz Conjecture to reach infinite loop for a given number.

import matplotlib.pyplot as plt

def Collatz(x):

    x0 = x #Saving the initial value

    n = 0 #Iteration Count

    #Matrices to save the values in
    N = []
    X = []

    #Initializing the lists
    X.append(x) #Number of Iteration
    N.append(n)  #Values

    while True:
        if x % 2 == 0:
            x = x / 2
        elif x % 2 == 1:
            if x == 1:
                break
            else:
                x = 3 * x + 1

        n += 1
        N.append(n)
        X.append(x)
    if __name__ == "__main__":
        print(N, len(N))
        print(X, len(X))
        print(f"It took {len(N) - 1} iterations for number {x0} to reach infinite loop.")

        text = "Collatz iterations for number " + str(x0)
        plt.plot(N, X, "r", label=text)
        plt.title(text)

        plt.legend()
        plt.ylabel("Values")
        plt.xlabel("Number of Iterations")
        plt.show()

    return len(X)-1

if __name__ == "__main__":
    Collatz(9)


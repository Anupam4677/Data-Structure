# when the two program solve the sam eproblem but look different .
# does one program better than other ?
# in order to answer this we must remember that there is important difference btw program and there underlying algorithm

# compute the sum of n integers 
import time 

def sum_n(n):
    start = time.time()
    totlasum = 0
    for ele in range(1,n+1):
        # print(f"ele:{ele}")
        totlasum += ele
        # print(f"totlasum:{totlasum}")
    end = time.time()
    return (f"Sum:{totlasum},Time Taken: {start-end}")

def foo(tom):
    start = time.time()
    fred = 0
    for bill in range(1,tom+1):
        barney = bill
        fred = fred + barney
    end = time.time()
    return (f"Sum:{fred},Time Taken: {start-end}")

ans = sum_n(100000)
print(ans)
ans2 = sum_n(100000)
print(ans2)

# the first func is better than the second as far as redeability is concerned
# Algorithm Analysis is concerned with comparing algo based on amout of computing resources
# There are 2 ways to look at computing resource '
# 1. amout of space and memory required to solve the prob 
# 2. Time they require to excecute 
# so above is benchmart technique which is dependent on programming language , hardware and time 
# so we require a better way 

## Big-O Notion 
# 1 - constant 
# log(n) - logrithmic
# n - linear 
# n(log(n)) - log linear 
# n^2 - quadratic 
# n^3 - Cubic 
# 2^n - Exponential 


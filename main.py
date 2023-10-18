                         # FINONACCI GENERATOR
import time

def fibo_iter(n):
    pre_num = 0
    current_num = 1
    for i in range(1, n):
        pre_pre_num =  pre_num
        pre_num = current_num
        current_num = pre_num + pre_pre_num

    return current_num


def fibo_recur(n):
    if n==0:
        return 0
    elif(n==1):
        return 1
    else:
        return fibo_recur(n-1) + fibo_recur(n-2)

if __name__ == "__main__":
    num = int(input("Enter A Number: "))
    init = time.time()
    # print(f"Using Recursions Value Of Fib({num}) is {fibo_recur(num)}")
    print(f"Using Iter Value Of Fib({num}) is {fibo_iter(num)}")
    print(f"It Took {time.time() - init} Seconds")

"""
NOTE: In Fibonacci Gernerator we create Two Methods First Method is "fibo_iter" and Second Metod is "fibo_recur" for Genearate a numbers in a fibonacci series.
 First Method is too fast, it tooks less time to generate a numbers and  takes low memory space.
 Second Method is too Slow, it tooks too much time to generate a numbers and takes very high memory space.
"""
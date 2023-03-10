
import time

def fib_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(n):
            c = a + b
            a =b
            b = c
        return c

def factorial_recursion(n):
    if n == 1:
        return 1
    else:
        return n*factorial_recursion(n-1)

def factroial(n):
    x = 1
    if n == 1:
        return 1
    else:
        for i in range(2,n):
            x *= i
        return x

def funtiocn_performance(fun,n):
    start = time.time()
    fun(n)
    end = time.time()
    print(f'time: {end-start}')




funtiocn_performance(fib_recursion,40)
funtiocn_performance(fib,40)
funtiocn_performance(factorial_recursion,40)
funtiocn_performance(factroial,40)


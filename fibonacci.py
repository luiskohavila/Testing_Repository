# Fibonacci
import sys
from time import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        pass
    
    return fibonacci(n-1) + fibonacci(n-2)
    
data_fibo = {}
def fibonacci_opt(n):
    global data_fibo
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        pass
    
    # Comprobar si ya se encontró el valor anteriormente
    if n in data_fibo.keys():
        return data_fibo[n]
    else:
        data_fibo[n] = fibonacci_opt(n-1) + fibonacci_opt(n-2)    
        return data_fibo[n]
    
if __name__ == "__main__":
    start_time = time()
    print(fibonacci_opt(300))
    end_time = time()
    print(end_time - start_time)
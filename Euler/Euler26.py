from math import *

def prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
for i in range(2, 990):
    if prime(i):
        print(i)

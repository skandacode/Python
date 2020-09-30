from math import *
primes=[]
def prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
'''for i in range(2, 10000):
    if prime(i):
        primes.append(i)'''
for i in range(9, 100001, 2):
    if prime(i)==False:
        done=False
        for x in range(1, int(sqrt(i/2))+1):
            if prime(i-(2*x*x)):
                done=True
                break
        if done==False:
            print(i)

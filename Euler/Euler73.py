from math import *
ans=0
count=0
for j in range(2, 1000001):
    for i in range(int(j/3)+1, int(j/2)+1):
        count+=1
        if gcd(i, j)==1:
            ans+=1
print(ans-1)

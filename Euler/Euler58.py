import math as m
def prime(n):
    playnum=n
    for i in range(2, m.ceil(m.sqrt(playnum))+1):
        if playnum%i==0:
            playnum=playnum/i
            return False
    return True
def trying(n):
    l=[]
    for i in range(0, n):
        center=(2*i+1)**2
        l.append(center-6*i)
        l.append(center-4*i)
        l.append(center-2*i)
        l.append(center)
    ans=0
    print(l)
    for i in l:
        if prime(i)==True:
            ans+=1
    return (100*ans/(len(l)))
'''for i in range(13342, 13345):
    if trying(i)<10:
        print(2*i+1)
        break
    print(i)
'''

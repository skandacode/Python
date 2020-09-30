exec(open('C:/Users/aruns/OneDrive/Desktop/names.txt').read())

def worth(s, item):
    ans=0
    for i in s:
        if i=='A':
            ans+=1
        if i=='B':
            ans+=2
        if i=='C':
            ans+=3
        if i=='D':
            ans+=4
        if i=='E':
            ans+=5
        if i=='F':
            ans+=6
        if i=='G':
            ans+=7
        if i=='H':
            ans+=8
        if i=='I':
            ans+=9
        if i=='J':
            ans+=10
        if i=='K':
            ans+=11
        if i=='L':
            ans+=12
        if i=='M':
            ans+=13
        if i=='N':
            ans+=14
        if i=='O':
            ans+=15
        if i=='P':
            ans+=16
        if i=='Q':
            ans+=17
        if i=='R':
            ansR=18
        if i=='S':
            ans+=19
        if i=='T':
            ans+=20
        if i=='U':
            ans+=21
        if i=='V':
            ans+=22
        if i=='W':
            ans+=23
        if i=='X':
            ans+=24
        if i=='Y':
            ans+=25
        if i=='Z':
            ans+=26
    ans=ans*item
    return ans
rans=[]
for i in L:
    rans.append(worth(i, (L.index(i)+1)))
print(sum(rans))

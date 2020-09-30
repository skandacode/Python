
l=[]
for i in range(0, 501):
    center=(2*i+1)**2
    print(center-6*i)
    print(center-4*i)
    print(center-2*i)
    print(center)
    l.append(center-6*i)
    l.append(center-4*i)
    l.append(center-2*i)
    l.append(center)
print(sum(l)-3)

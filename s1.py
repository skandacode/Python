def m(l):
    sss=l[0]
    for i in l:
        if i <sss:
            sss=i
def sort(li):
    for t in range(0, int(len(li))):
        first=list(li)
        final=[]
        final.append(m(first))
        del first[sss]
    print(final)

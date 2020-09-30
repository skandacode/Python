def is_p(num):
    s=str(num)
    print(s)
    L=len(s)
    ans=True
    for i in range(1, L+1):
        if str(i) in s:
            print(i)
            pass
        else:
            ans=False
            print('this failed '+str(i))
            break
    return ans

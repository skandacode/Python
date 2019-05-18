def prime(num):
    if num==2:
        print("prime")

    else:
        for i in range(2, num+2):
            if num%i==0:
                print("not prime")
                break
            else:
                print("prime")
                break
        

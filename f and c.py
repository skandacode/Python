while True:
    print('Enter 1 to convert F to C or 2 to convert C to F?')

    a=input()

    if a == '1':
        f=input('what is F? ')
        f = int(f)
        c=(f-32)*100/180
        print('Temperature in C is '+str(int(round(c,0))))
    elif a == '2':
        c=input('what is c? ')
        c = int(c)
        f=(c/100*180)+32
        print('Temperature in f is '+str(int(round(f,0))))


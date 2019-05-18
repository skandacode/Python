def cal(numofnums):
    num=1
    list1=[1]
    for i in range(1, numofnums+1):
        num=num*2
        list1.append(num)
    myfile = open('C:\\Users\\aruns\\Desktop\\power of 2.txt', 'w')
    for j in list1:
        myfile.write(str(j) + '\n')
    myfile.close()

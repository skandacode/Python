file=open('C:/Users/aruns/OneDrive/Desktop/p099_base_exp.txt').read()
lines=file.split('\n')
matrix=[]
for line in lines:
    matrix.append(line.split(','))
ans=0

print("Split finished")
print("Calculating Started")
count=0
for i in matrix:
    count+=1
    subans=int(i[0])**int(i[1])
    if subans>ans:
        ans=subans
        ansnum=count
    print(count)
print(ansnum)

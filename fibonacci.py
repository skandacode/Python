first=1
sec=1
fib=[1, 1]
for i in range(0, 100):
    total=first*2
    first=sec
    sec=total
    fib.append(total)
print(fib)

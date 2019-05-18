import random
numbers=[]
for i in range(1, 100):
    numbers.append(random.randint(1, 1000))

numbers.sort()
for ik in numbers:
    print(ik)

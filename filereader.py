my_file = open("C:/Users/aruns/Desktop/skanda pro programs/Scratch Projects/simplefile.txt", "r")
my_sum = 0
for oneline in my_file:
    my_sum=my_sum+int(oneline)

print('the total is '+str(my_sum))

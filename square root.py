side1=input('what is length of one side in the right angle triangle?')
side1=int(side1)
side2=input('what is length of hypotenuse side in the right angle triangle?')
side2=int(side2)
# square root of a number
import math

# input number
side3_square = (side2 * side2) - (side1 * side1)
side3 = math.sqrt(side3_square)
#print("Other side is ", side3)
if (side3%1 == 0):
    print("Other side is ", int(side3))
else:
    print("Other side is ", side3)

# calculate square-root
#square = math.sqrt(num)

# print square-root
#print(square)

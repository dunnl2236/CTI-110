# Area of Rectangle Problem
# 11/15/2018
# CTI-110 P2H2-Male Female Percentage
# Lacey Dunn

# get length and width of two rectangles.

lengthA=int(input("Length rectangle A: "))
widthA=int(input("Width rectangle A: "))

lengthB=int(input("Length rectangle B: "))
widthB=int(input("Width rectangle B: "))                   

# caculate gectangles size using formula.

areaA=(lengthA*widthA)
areaB=(lengthB*widthB)

# print areaA & areaB

print("The area of rectangle A: ", areaA)
print("The area of rectangle B: ", areaB) 

# create if statement for which rectangles is larger?

if areaA > areaB:
    
    print("Rectangle A is larger.")

elif areaB > areaA:

    print("Rectangle B is larger.")

else:
    
    print("Rectangle A and Rectangle B are equal.")

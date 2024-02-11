side1 = int(input('Enter Side 1 length '))
side2 = int(input('Enter Side 2 length '))
side3 = int(input('Enter Side 3 length '))

if (side1 == side2 and side1 == side3) :
    print (" All sides are equal, so Equilateral triangle")
elif (side1 == side2 and side1 != side3) :
    print ("Only 2 sides are equal, so isosceles triangle")
else :
    print("No 2 sides are equal, so scalene triangle")


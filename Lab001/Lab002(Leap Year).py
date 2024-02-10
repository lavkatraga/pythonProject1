
leap_year = int(input("Enter any year:"))
# rem = leap_year%4
# print (rem)
print(leap_year % 4)
print(leap_year % 100)
print(leap_year % 400)
if (leap_year % 4 == 0 and leap_year % 100 == 0) and (leap_year % 400 == 0):
    print("This is a Leap Year")
else:
    print("Not a Leap Year")

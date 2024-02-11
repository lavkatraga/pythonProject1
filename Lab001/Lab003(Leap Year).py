
l_year = int(input("Enter any year:"))
# rem = leap_year%4
# print (rem)
print(l_year % 4)
print(l_year % 100)
print(l_year % 400)
if (l_year % 4 == 0 and l_year % 100 == 0) and (l_year % 400 == 0):
    print("This is a Leap Year")
else:
    print("Not a Leap Year")

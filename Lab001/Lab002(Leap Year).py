
#Why 1700 is not a leap year?
#The rule is that if the year is divisible by 100 and not divisible by 400, leap year is skipped. The year 2000 was a leap year, for example,
#but the years 1700, 1800, and 1900 were not. The next time a leap year will be skipped is the year 2100.

leap_year = int(input("Enter any year:"))
#rem = leap_year%4
#print (rem)
print (leap_year%4)
print (leap_year%100)
print (leap_year%400)
if (leap_year%4 == 0 and leap_year%100 == 0 ) and (leap_year%400 == 0) :
    print("This is a Leap Year")
else :
    print("Not a Leap Year")



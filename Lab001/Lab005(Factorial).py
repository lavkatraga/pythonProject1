import math

n = int(input("Enter a number :"))
#print (math.factorial(n))
temp = 1
if n >= 1:
    for i in range (1, n+1):
        temp=temp *i
print("Factorial of the number is: ", temp)
# Task 1: Check if a Number is Even or Odd
n=int(input("Enter a Number :"))
if n%2==0:
    print(n,"is a Even Number.")
else:
    print(n,"is a Odd Number.")

# Task 2: Sum of Integers from 1 to 50 Using a Loop
sum=0
n=int(input("Enter any integer:"))
b=n+1
for i in range (1,b):
    sum=sum+i
    if sum==n*b/2:
        print("The sum of numbers from 1 to",n,":",sum)


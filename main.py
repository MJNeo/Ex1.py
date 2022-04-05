#1. This program prints Hello, World.
print('Hello World!')


#2. This program adds two numbers
num1 = int(input("Enter a value: "))
num2 = int(input("Enter a value: "))
# Add two numbers
sum = num1 + num2
# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


#3. To check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


#4. To calculate the square root
num = int(input("Enter a number: "))
num_sqrt = num ** 0.5
print(num_sqrt)


#5. To calculate the area of the triangle
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
#to calculate the semi-perimeter
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) **0.5
print('The area of the trainagle is %0.2f' %area)


#6. To check if a number is positive, negative or 0.
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

  
#7. Solve the quadratic equation ax**2 + bx + c = 0
# import complex math module
import cmath
a = int(input("Enter a value: "))
b = int(input("Enter a value: "))
c = int(input("Enter a value: "))
# calculate the discriminant
d = (b**2) - (4*a*c)
# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))


#8.  To swap two variables

x = input('Enter value of x: ')
y = input('Enter value of y: ')
# create a temporary variable and swap the values
temp = x
x = y
y = temp
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


#9.  Program to generate a random number between 0 and 100
# importing the random module
import random
print(random.randint(0,100))


#10. To convert KM to Miles  
#Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))
# conversion factor
conv_fac = 0.621371
# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))


#11. To convert temperature in celsius to fahrenheit
# change this value for a different result
celsius = float(input("Enter value in celsius: "))
# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))


#12 To check if year is a leap year or not
year = int(input("Enter a value: "))
# To get year (integer input) from the user
# year = int(input("Enter a year: "))
# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))


#13. To find the largest number among the three input numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("The largest number is", largest)
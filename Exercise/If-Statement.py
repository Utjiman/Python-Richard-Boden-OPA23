#0. Check sign
'''
Number = int(input("Write a number: "))

if Number < 0:
    print(f"The number {Number} is negative")
elif Number == 0:
    print(f"The number {Number} is Zero")
else: 
    print(f"The number {Number} is positive")
'''

#1. Smallest
'''
NumberOne = int(input("Write a number: "))
NumberTwo = int(input("Write a number: "))
if NumberOne < NumberTwo:
    print(f"{NumberOne} is the smallest")
else:
    print(f"{NumberTwo} is the smallest")
'''
#2. Right angle
'''
angleOne = int(input("Enter the first angle: "))
angleTwo = int(input("Enter the second angle: "))
angleThree = int(input("Enter the third angle: "))

# Check if the angles can form a triangle
if angleOne + angleTwo + angleThree == 180 and angleOne > 0 and angleTwo > 0 and angleThree > 0:
    # Check if the triangle has a right angle
    if angleOne == 90 or angleTwo == 90 or angleThree == 90:
        print("The triangle is a right-angle triangle.")
    else:
        print("The triangle is not a right-angle triangle.")
else:
    print("The angles do not form a valid triangle.")
'''
#3. Medicine

'''
age = int(input("Enter age in years: "))
weight = int(input("Enter weight in kg: "))

# Determine the number of pills based on weight and age criteria
if weight > 40 or (age > 12 and weight >= 40):
    print("Recommended: 1-2 pills")
elif weight >= 26 and weight <= 40:
    print("Recommended: 1/2-1 pill")
elif weight >= 15 and weight < 26:
    print("Recommended: 1/2 pill")
else:
    print("Consult a doctor for the appropriate dosage.")
'''

#4. Divisible

'''
number = int(input("Enter a number: "))


if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")


if number % 5 == 0:
    print(f"The number {number} is divisible by 5.")
else:
    print(f"The number {number} is not divisible by 5.")


if number % 5 == 0 and number % 2 != 0:
    print(f"The number {number} is divisible by 5 and odd.")
else:
    print(f"The number {number} is not both divisible by 5 and odd.")
'''

#5. Luggage size
'''
weight = float(input("Enter weight in kg: "))
lenght = int(input("Enter lenght in cm: "))
width = int(input("Enter width in cm: "))
height = int(input("Enter height in cm: "))

if weight <= 8 and lenght <= 55 and width <= 40 and height <= 23:
    print("The luggage is allowed")
else:
    print("The luggage is to not allowed")
'''    

     


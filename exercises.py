# Exercise 1: Calculate Area of a Triangle
#
# Write a function named `calculate_area_triangle` that takes the base and height of a triangle and returns the area.
# The area formula is (base * height) / 2.
#
# Examples:
# calculate_area_triangle(10, 5) should return 25.0.
# calculate_area_triangle(7, 3) should return 10.5.
#
# Define your function and call it below.


def calculate_area_triangle(base, height):
    return float((base * height) / 2)

print('Exercise 1:', calculate_area_triangle(10, 5))


# Exercise 2: Calculate Simple Interest
#
# Write a function named `simple_interest` that takes principal, rate of interest (as a percentage), and time (years).
# Calculate and return the simple interest using the formula (principal * rate * time) / 100.
#
# Examples:
# simple_interest(1000, 5, 2) should return 100.
# simple_interest(1500, 3.5, 5) should return 262.5.
#
# Define your function and call it to see the result.
def simple_interest(principal, rate, time):
    return ((principal * rate * time) / 100)

print('Exercise 2:', simple_interest(1000, 5, 2))

# Exercise 3: Apply a Discount
#
# Write a function named `apply_discount` that takes a product's price and a discount percentage (from 0 to 100).
# Return the new price after applying the discount.
#
# Examples:
# apply_discount(100, 25) should return 75.
# apply_discount(80, 10) should return 72.
#
# Define your function and call it to display the discounted price.
def apply_discount(price, discount):
    return int(price - price * (discount/100))


print('Exercise 3:', apply_discount(100, 25))


# Exercise 4: Convert Temperature
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.
# The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32.
# The formula for converting Fahrenheit to Celsius is (Fahrenheit - 32) * 5/9.
#
# Examples:
# convert_temperature(0, 'C') should return 32.0.
# convert_temperature(32, 'F') should return 0.0.
#
# Define the function and then call it below.


def convert_temperature(temperature, unit):
    if unit.lower() == "c":
        temperature = (temperature * 9/5) + 32
    elif unit.lower() == 'f':
        temperature = (temperature - 32) * 5/9
        
    else: 
        print("Pass C or F in the 2nd parameter")
    return temperature    

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))



# Exercise 5: Sum to N
#
# Write a function named `sum_to` that takes a single integer n and returns the sum of all integers from 1 to n.
#
# Examples:
# sum_to(6) should return 21.
# sum_to(10) should return 55.
#
# Define the function and then call it below.


# Dumb Way to do it
# def sum_to(n):
#     sum = 0
#     for i in range(n+1):
#         sum += i
#     return sum

# Using recursion
def sum_to(n):
    if (n==1):
        return n
    return (n + sum_to(n-1))
    

print('Exercise 5:', sum_to(6))

# Exercise 6: Find the Largest Number
#
# Write a function named `largest` that takes three integers as arguments and returns the largest of them.
#
# Examples:
# largest(1, 2, 3) should return 3.
# largest(10, 4, 2) should return 10.
#
# Define your function and test it with different inputs.


def largest(num1, num2, num3):
    max = num1
    if max < num2:
        max = num2
    if max < num3:
        max = num3
    return max 
print('Exercise 6:', largest(1, 2, 3))

# Exercise 7: Calculate a Tip
#
# Create a function called `calculate_tip`. It should take the bill amount and the tip percentage (as a whole number).
# The function should return the amount of the tip.
#
# Examples:
# calculate_tip(50, 20) should return 10.
#
# Write your function and test its output below.

def calculate_tip(billAmount, tipPercentage):
    return int(billAmount * tipPercentage/100)

print('Exercise 7:', calculate_tip(120, 20))


# Exercise 8: Calculate Product of Numbers
#
# Write a function named `product` that takes an arbitrary number of numbers, multiplies them, and returns the product.
# Review your notes on *args for handling an arbitrary number of arguments.
#
# Examples:
# product(-1, 4) should return -4.
# product(2, 5, 5) should return 50.
#
# Define the function and call it with different sets of numbers to test.


def product(*numbers):
    result = 1
    for i in numbers:
        result= result *i 
    return result
print('Exercise 8:', product(-1, 4))


# Exercise 9: Basic Calculator
#
# Create a function named `basicCalculator` that takes three arguments: 
# two numbers and a string representing an operation ('add', 'subtract', 'multiply', 'divide'). 
# Perform the provided operation on the two numbers. In operations where the order of numbers is important, 
# treat the first parameter as the first operand and the second parameter as the second operand.
#
# Examples:
# basicCalculator(10, 5, 'subtract') should return 5.
# basicCalculator(10, 5, 'add') should return 15.
# basicCalculator(10, 5, 'multiply') should return 50.
# basicCalculator(10, 5, 'divide') should return 2.
#
# Define the function and then call it below.


def basicCalculator(num1, num2, operation):
    if operation.lower() == 'add':
        return (num1 + num2)
    elif operation.lower() == 'subtract':
        return (num1 - num2)
    elif operation.lower() == 'multiply':
        return (num1 * num2)
    elif operation.lower() == 'divide':
        return (num1 / num2)
    else: 
        return f"{operation} isn't valid please pass ('add', 'subtract', 'multiply', 'divide') in the 3rd parameter"
        
print('Exercise 9 Result:', basicCalculator(10, 5, "subtract"))

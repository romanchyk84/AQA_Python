# Task 1
# Create a program that could convert temperature in degrees Celsius (C) to Kelvin (K) and Fahrenheit (F).
print('***** Temperature converter *****')

celsius = float(input('Enter temperature in Celsius: '))
temp_fahr = celsius * 9 / 5 + 32
temp_kelv = celsius + 273.15

print('Temperature in Fahrenheit = ', temp_fahr,'F')
print('Temperature in Kelvin = ', temp_kelv,'K')


# Task 2
# Create a simple calculator.
print("\n***** Simple calculator *****")

var1 = float(input("Enter the first number: "))
operator = input("Choose the operator (+, -, *, /): ")
var2 = float(input("Enter the second number: "))

if operator == '+':
    result = var1 + var2
elif operator == '-':
    result = var1 - var2
elif operator == '*':
    result = var1 * var2
elif operator == '/':

    if var2 == 0:
        result = "ERROR: Division by zero"
    else:
        result = var1 / var2
else:
    result = "Unknown operator"

print("Result = ", result)

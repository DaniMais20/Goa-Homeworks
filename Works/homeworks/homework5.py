name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))

print(name, age, height)

print(age >= 18 and height > 170)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print(number1 > 0 or number2 > 0)

favorite_color = input("Enter your favorite color: ")
age = int(input("Enter your age: "))

print(favorite_color == "blue" or age < 18)

name = input("Enter your name: ")
balance = float(input("Enter your balance: "))
vip = input("Are you a VIP? (True or False): ") == "True"

print(balance > 100 or vip)
name = input("Enter your name: ")#dani
age = int(input("Enter your age: "))#17
height = float(input("Enter your height in cm: "))#180

print(name, age, height)

print(age >= 18 and height > 170)

number1 = int(input("enter the first number: "))
number2 = int(input("enter the second number: "))

print(number1 > 0 or number2 > 0)

favorite_color = input("enter your favorite color: ")
age = int(input("enter your age: "))

print(favorite_color == "red" or age < 18)

name = input("enter your name: ")
balance = float(input("enter your balance: "))
vip = input("are you a vip? (True or False): ") == "true"

print(balance > 100 or vip)
age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ")

if age >= 18 and citizen == "yes":
    print("Access granted")
else:
    print("Access denied")









    numbers = [5, 12, 8, 25, 3, 17, 9, 30]

for num in numbers:
    if num > 10:
        print(num)












        cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi", "Gori", "Zugdidi"]

index = int(input("Enter an index (0-5): "))

print(cities[index])






num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > 100 or num2 > 100:
    print("Condition met")
else:
    print("Condition not met")







    numbers = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]

for num in numbers:
    if num % 2 == 0:
        print(num)







        fruits = [
    "Apple", "Banana", "Orange", "Grape", "Mango",
    "Peach", "Pear", "Kiwi", "Cherry", "Plum"]

first_five = fruits[:5]

print(first_five)





numbers = [50, 120, 75, 200, 99, 101, 45, 150, 80, 300]

i = 0

while i < len(numbers):
    if numbers[i] > 100:
        print(numbers[i])
    i += 1







    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[::2])









numbers = [60, 45, -5, 20, 100, 0, 55, 30]

for num in numbers:
    if num > 50 or num < 0:
        print("Large")
    else:
        print("Normal")











        temperature = int(input("Enter the temperature: "))

if temperature < 0 or temperature > 35:
    print("Extreme temperature")
else:
    print("Temperature is normal")
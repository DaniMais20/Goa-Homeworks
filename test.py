age_input = input("enter your age:")
age = int(age_input)

if age > 0:
    print("users age is positive ")
else: 
    print("your age is positive")
    








Days = ["monday", "tuesday", "wendsday", "thursday", "friday", "saturday", "sunday"]

index = input("enter index number: ")

index = int(index)

if 0 <= index <= 7: 
    print(Days[index])






Elements = [ 2.5, "String", 15, True, False, 10.5, 20.5, "Water", "Food", 40, 100, 200, "Bottle", 14, "Color" ]

number = 0

for element in Elements: 
    number += 1 

print("Total elements in list")


numbers = [22, 43, 12, 5, 100, 25, 49, 86, 37, 72]

for index, number in enumerate(numbers):
    if number % 2== 0:
        print(index)
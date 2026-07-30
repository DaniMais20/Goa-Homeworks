
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")



num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > 0 and num2 > 0:
    print("Both numbers are positive")
else:
    print("At least one number is not positive")



num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 % 2 == 0 or num2 % 2 == 0:
    print("At least one number is even")
else:
    print("Both numbers are odd")


num = input("Enter a number: ")
num = int(num)

print(num ** 2)

score = int(input("Enter a score (0-100): "))

if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")


for i in range(1, 21):
    print(i)


i = 10

while i >= 1:
    print(i)
    i -= 1


fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango", "Kiwi"]

print(fruits[0])   # First element
print(fruits[-1])  # Last element
print(fruits[2])   # Third element



numbers = [5, 10, 15, 20, 25]

for num in numbers:
    print(num)



numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

print(numbers)


items = ["A", "B", "C", "D", "E", "F", "G", "H"]

for i in range(0, len(items), 2):
    print(items[i])



N = int(input("Enter N: "))

total = 0

for i in range(1, N + 1):
    total += i

print(total)


N = int(input("Enter a number: "))

i = 2

while i <= N:
    print(i)
    i += 2



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a == b == c:
    print("All numbers are equal")
elif a == b or a == c or b == c:
    print("Two numbers are equal")
else:
    print("All numbers are different")
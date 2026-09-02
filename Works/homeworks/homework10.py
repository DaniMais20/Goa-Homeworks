numbers = [5, 8, 12, 3, 7, 10, 15, 20, 9, 14]

for num in numbers:
    print(num)

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")





countries = ["Georgia", "France", "Germany", "Italy", "Japan", "Brazil", "Canada"]

while True:
    index = int(input("Enter an index (-1 to quit): "))

    if index == -1:
        print("Program ended.")
        break

    if 0 <= index < len(countries):
        print("Country:", countries[index])
    else:
        print("Invalid index. Try again.")

        
        






numbers = [4, 8, 12, 16, 20]

print("List:", numbers)

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)












numbers = [5, -3, 0, 8, -1, 0, 12, -7, 4, 0]

positive = 0
negative = 0
zero = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zero values:", zero)







numbers = [12, 45, 7, 89, 23, 56, 91, 34]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)
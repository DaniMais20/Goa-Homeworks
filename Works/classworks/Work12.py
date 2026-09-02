numbers = [17, 5, 2, 6, 8, 12, 15, 18, 13]

even_sum = 0
odd_sum = 0

for number in numbers:
    if number % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

print("sum of even numbers:", even_sum)
print("sum of odd numbers:", odd_sum)



names = ["dani", "zuka", "nika", "alex", "zukito"]

index = 0

for name in names:
    print(index, name)
    index += 1



numbers = [10, -5, 7, -3, 12, -8, 4, -1]

positive_sum = 0
negative_sum = 0

for number in numbers:
    if number > 0:
        positive_sum += number
    else:
        negative_sum += number

print("sum of positive numbers:", positive_sum)
print("sum of negative numbers:", negative_sum)
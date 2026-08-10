def filter_evens(numbers):
    evens = []

    for number in numbers:
        if number % 2 == 0:
            evens.append(number)

    return evens


def sum_numbers(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


even_numbers = filter_evens([5, 6, 4, 10, 8, 12, 9, 7])
result = sum_numbers(even_numbers)

print(result)






def positives(numbers):
    positive_array = []

    for number in numbers:
        if number > 0:
            positive_array.append(number)

    return positive_array


def filter_odds(numbers):
    odd_numbers = []

    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)

    return odd_numbers


def sum_numbers(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


result = positives([-5, -2, 3, -12, 19, -3, 7, -8, 20])
result = filter_odds(result)
result = sum_numbers(result)

print(result)




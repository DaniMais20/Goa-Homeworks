def add_numbers(a, b):
    return a + b

print(add_numbers(5, 7))


def square(number):
    return number * number

print(square(6))


def is_even(number):
    return number % 2 == 0

print(is_even(8))
print(is_even(5))


def greet(name):
    print("Hello,", name + "!")

greet("Saba")


def largest_number(numbers):
    return max(numbers)

print(largest_number([3, 8, 2, 10, 5]))


def text_length(text):
    return len(text)

print(text_length("Hello World"))


def make_upper(text):
    return text.upper()

print(make_upper("hello world"))


def even_numbers(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result

print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8]))


def average(numbers):
    if len(numbers) == 0:
        return "The list is empty."
    return sum(numbers) / len(numbers)

print(average([10, 20, 30, 40]))
print(average([]))


def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("level"))
print(is_palindrome("hello"))
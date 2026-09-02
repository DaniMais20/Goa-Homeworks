def sum_numbers(n):
    total = 0

    for i in range(n + 1):
        total += i

    return total


print(sum_numbers(5))












def count_positive(numbers):
    count = 0

    for number in numbers:
        if number > 0:
            count += 1

    return count


print(count_positive([-2, 5, 7, -1, 0, 3]))











def count_vowels(text):
    count = 0

    for letter in text:
        if letter.lower() in "aeiou":
            count += 1

    return count


print(count_vowels("Hello World"))













def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


print(is_prime(7))   
print(is_prime(10))  








def second_largest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None

    unique_numbers.sort(reverse=True)

    return unique_numbers[1]


print(second_largest([5, 2, 8, 10, 8, 3]))  
print(second_largest([5, 5, 5]))            
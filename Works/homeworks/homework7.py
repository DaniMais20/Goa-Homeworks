number = int(input("enter a number: "))

for i in range(1, number + 1):
    print(i)







    start = int(input("enter start: "))
stop = int(input("enter stop: "))
step = int(input("enter step: "))

for i in range(start, stop, step):
    print(i)











    first_name = input("enter your first name: ")
last_name = input("enter your last name: ")

for i in range(50):
    print(first_name, last_name)






    n = int(input("enter a number: "))

for i in range(n, -1, -1):
    print(i)















    n = int(input("enter a number: "))

i = 0

while i <= n:
    print(i ** 2)

    if i % 2 == 0:
        print(True)
    else:
        print(False)

    i += 1















    number = int(input("enter a number: "))

i = 10

while i <= number:
    print(i)
    i += 1










    start = int(input("enter start: "))
stop = int(input("enter stop: "))

i = start

while i <= stop:
    print(i)
    i += 1












    name = input("enter your name: ")

i = 0

while i < 50:
    print(name)
    i += 1










    total = 0

while True:
    number = int(input("enter a number: "))

    if number < 0:
        break

    total += number

print(total)






secret_number = 73
guess = 0

while guess != secret_number:
    guess = int(input("guess the secret number: "))

print("you guessed the secret number")
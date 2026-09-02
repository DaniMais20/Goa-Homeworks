num = 0

while num <= 10:
    print(num)
    num += 1


num2 = 10

while num2 >= 0:
    print(num2)
    num2 -= 1



num4 = 0
sum = 0

while num4 <= 5:
    sum += num4
    num4 += 1

print(sum)




name = input("Enter your name: ")
n = int(input("Enter a number: "))

i = 0

while i < n:
    print(name)
    i += 1



correct = False

while correct == False:
    password = input("enter the password: ")

    if password == "python123":
        correct = True

print("access Granted")

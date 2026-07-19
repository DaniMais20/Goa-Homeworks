for number1 in range(10): 
     print('dani')

for i in range(5, 31):
    print(i)

start = int(input("start: "))
stop = int(input("stop: "))

for i in range(start, stop + 1):
    print(i)


n = int(input("enter number: "))
name = input("enter your name: ")

for i in range(n):
    print(name)



number = int(input("enter number: "))

for i in range(1, 11):
    print(number ** i)



number = int(input("enter your number: "))

sum = 0

for i in range(1, number + 1):
    sum += i

    print("sum:", sum)
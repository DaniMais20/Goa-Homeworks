age = int(input("enter your age: "))

if age >= 18:
    print("you are adult")
else:
    print("you are not adult")



    num1=float(input("enter first number: "))
    num2=float(input("enter second number: "))







num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))

if num1 > 0 and num2 > 0:
    print("both numbers are positive")
else:
    if num1 > 0 or num2 > 0:
        print("only one number is positive")
    else:
        print("neither number is positive")





for i in range(10):
    num = int(input("enter a number: "))

    if num > 0 and num % 2 == 0:
        print("the number is positive and even")
    else:
        if num > 0 or num % 2 == 0:
            print("the number is positive or even")
        else:
            print("the number is neither positive nor even")



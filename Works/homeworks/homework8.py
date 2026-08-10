score = float(input("Enter exam score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 91:
    print("A")
elif score >= 81:
    print("B")
elif score >= 71:
    print("C")
elif score >= 61:
    print("D")
else:
    print("F")










positives = 0
negatives = 0
evens = 0
odds = 0

for i in range(10):
    num = int(input("Enter number " + str(i + 1) + ": "))
    
    if num > 0:
        positives += 1
    elif num < 0:
        negatives += 1
    
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1

print("Results:")
print("Positive numbers: " + str(positives))
print("Negative numbers: " + str(negatives))
print("Even numbers: " + str(evens))
print("Odd numbers: " + str(odds))



num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print("The first number is greater")
elif num2 > num1:
    print("The second number is greater")
else:
    print("The numbers are equal")




CORRECT_PASSWORD = "python123" 
attempts = 3

while attempts > 0:
    password = input("Enter password: ")
    
    if password == CORRECT_PASSWORD:
        print("Access granted!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect password! Attempts remaining: " + str(attempts))

if attempts == 0:
    print("Attempt limit reached. Access denied!")
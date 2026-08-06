name = input("Enter your name: ")
print("formatted name:", name.capitalize())

text = input("Enter some text: ")
print("Uppercase:", text.upper())



text = input("Enter some text: ")
print("Lowercase:", text.lower())




sentence = input("Enter a sentence: ")
word = input("Enter the word to search for: ")

position = sentence.find(word)

if position != -1:
    print("The word starts at position " + str(position) + ".")
else:
    print("The word was not found.")
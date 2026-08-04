#  print() - prints the text on the screen
print("Hello, World")



#  input() - the user gets informatiom
name = input("Enter your name: ")




#  len() - returns the total number of items in an object
length = len(name)



#  type() - shows the variables type
print(type(name))


#  int() - changes the str into an number int
age = int(input("Enter your age: "))

#function in a code block that executes a certain order
#function is used for the code to be more compact and more understandable for the user and the client 
#instad of making the code repeat several times we make function that we use when needed 



# .upper() - this method changes the strings every lowercase into an UPPERCASE

print("hello".upper())          # HELLO
print("python".upper())         # PYTHON
print("good morning".upper())   # GOOD MORNING

# .lower - this is the same as UPPERCASE but instead changes every string into and lowercase

print("HELLO".lower())          # hello
print("PyThOn".lower())         # python
print("GOOD MORNING".lower())   # good morning



# .capitalaize() - this only changes the first letter into UPPERCASE the other letters do not chage


print("hello".capitalize())         # Hello
print("pYTHON".capitalize())        # Python
print("good morning".capitalize())  # Good morning





# .find()  - this fuction finds the word and then returns their first index if it cant find the index it will return -1



print("Python".find("t"))           # 2
print("Hello World".find("World"))  # 6
print("Programming".find("z"))      # -1
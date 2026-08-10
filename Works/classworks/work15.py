number = [5, 25, 50, 100]
number.append(200)
print(number)



fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)





numbers = [10, 20, 30]
numbers.pop(2)
print(numbers)



colors = ["red", "green", "blue"]
colors.pop(1)
print(colors)




numbers = [1, 3, 4]
numbers.insert(1, 2)
print(numbers)



weather = ["sunny", "cloudy", "rainy", "foggy",]
weather.insert(1, "snowy")
print(weather)




numbers = [5, 10, 15, 20]
print(len(numbers))



animals = ["dog", "cat", "bird"]
print(len(animals))




# sort - sorts the number in ascend order and sorts words alphabetically 
numbers = [5, 2, 8, 1]
numbers.sort()
print(numbers)



fruits = ["c", "a", "b"]
fruits.sort()
print(fruits)


# remove - removes the first one thats in line works with strings removes the first time it sees the set string

numbers = [10, 20, 30, 20]
numbers.remove(20)
print(numbers)

colors = ["red", "green", "blue"]
colors.remove("green")
print(colors)



#reverse - reverses the order in the list and worsk the same with words

numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)


animals = ["dog", "cat", "bird"]
animals.reverse()
print(animals)
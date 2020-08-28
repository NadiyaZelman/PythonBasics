### Chapter 4: Working with lists
# states = ['New York', 'New Jersey', "connecticut", 'California']
# for state in states:
#     print(f"Welcome to {state}!!!")
# print()
# list_of_pizza = ['pepperoni', 'margarita', 'three cheeses']
# for pizza in list_of_pizza:
#     print(pizza)
#     print(f"I like {pizza} pizza.")
# print(f"I really like pizza!")

# for num in range(5):
#     print(f"my current number: {num}")
#
# for num in range(3, 6):
#     print(f"my current number from range(3, 6) : {num}")
#
# for num in range(5, 13):
#     print(num ** 2)
#
# squares = list()

# print(num_sqr)
# print(squares)
# list_of_animals = ['cat', 'dog', 'monkey']
# print(list_of_animals)
# for animal in list_of_animals:
#     print(animal)
#     print(f"A {animal} would make a good pet.")
# print(f"Any of these animals would make a great pet!")
# print()
# for num in range(5):
#     print(f"My number: {num}")
# for num in range(3, 6):
#     print(f"my current number; {num}")
# print(range(5))
# numbers = list(range(5))
# print(numbers)
#
# square = []
# for num in range(1, 11):
#     square = num ** 2
#     squares.append(num ** 2)
# print(squares)
# squares = [num ** 2 for num in range(5, 13)]
# print(squares)
# print(f"============4-5=========")
# num = list(range(1, 1000001))
# print(max(num))
# print(min(num))
# print(f"===============4-6============")
# odd_numbers =list(range(1, 21, 2))
# for number in odd_numbers:
#     print(number)
# print(f"=============4-7=============")
# numbers = list(range(3, 31))
# for number in numbers:
#     print(number * 3)
# print(f"=============4-8============")
# numbers = list(range(1, 11))
# # for number in numbers:
# #     print(number ** 3)
#
# cubes = [number ** 3 for number in range(1, 11)]
# print(cubes)
# items = ["pan", 'pencil', 'book', 'car', 'bag']
# print("The first tree items in the list are:")
# print(items[:3])
# print("Three items from the middle of the list are:")
# print(items[1:4])
# print("The last tree items in the list are:")
# print(items[-3:])
pizzas = ['pepperoni', 'margarita', 'three cheeses']
friends_pizzas = pizzas[:]
pizzas.append('new')
friends_pizzas.append('mushrooms')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"\t{pizza.title()}")
print("My friends favorite pizzas are:")
for friends_pizza in friends_pizzas:
    print(f"\t{friends_pizza.title()}")

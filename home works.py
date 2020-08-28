############## 5-1 ##################
# car = 'mazda'
# print("Is car == 'mazda'? I predict TRUE.")
# print(car == 'mazda')
#
# print("\nIs car == 'audi'? I predict FALSE.")
# print(car == 'audi')
#
# print(car =='honda')
# print(car == 'mazda')
# animal = 'cat'
# print(animal == 'dog')
# print(animal == 'cat')
# print(animal == 'rabbit')
# country = 'USA'
# if country =='USA':
#     print (country.lower())

# cars = ['audi', 'bmw', 'mazda']
# for car in cars:
#  if 'bmw' in cars:
#     print(f"I want to owm {car.title()

############# 5-3 #####################
# alien_color = 'green'
# if alien_color == 'green':
#     print("You just earned 5 points")
#
# alien_color = 'green'
# if alien_color == 'yellow':
#     print("You just earned 0 points")
# #
# print(alien_color == 'green')
# print(alien_color == 'red')

# ################ 5-4 ####################
# alien_color = 'green'
# if alien_color == 'green':
#     print("You just earned 5 points for shooting the alien")
# else:
#     print("You earned 10 points")
#
# alien_color = 'red'
# if alien_color == 'green':
#     print("You just earned 5 points for shooting the alien")
# else:
#     print("You earned 10 points")

################## 5-5 #####################
# alien_color = 'green'
# if alien_color == 'green':
#     print("You just earned 5 points for shooting the alien")
# elif alien_color == 'yellow':
#     print("You earned 10 points")
# elif alien_color == 'red':
#     print("You earned 15 points")
#
# alien_color = 'red'
# if alien_color == 'green':
#     print("You just earned 5 points for shooting the alien")
# elif alien_color == 'yellow':
#     print("You earned 10 points")
# elif alien_color == 'red':
#     print("You earned 15 points")
#
# alien_color = 'yellow'
# if alien_color == 'green':
#     print("You just earned 5 points for shooting the alien")
# elif alien_color == 'yellow':
#     print("You earned 10 points")
# elif alien_color == 'red':
#     print("You earned 15 points")

################### 5-6 #############################
# age = int(input("How old are you?"))
# if age < 2:
#     print("You are a baby")
# elif age < 4:
#     print("You are a toddler!")
# elif age < 13:
#     print("You are a kid!")
# elif age < 20:
#     print("You are a teenager!")
# elif age < 65:
#     print("You are an adult!")
# else:
#     print("You are an elder!")

################## 5-7 ###############################
# favorite_fruits = ['apples', 'bananas', 'mangoes']
# if 'apples' in favorite_fruits:
#     print("Your really like apples!")
# if 'bananas' in favorite_fruits:
#     print("Your really like bananas!")
# if 'mangoes' in favorite_fruits:
#     print("Your really like mangoes!")
# if 'strawberries' in favorite_fruits:
#     print("Your freally like strawberries!")
# if 'watermelons' in favorite_fruits:
#     print("Your really like watermelons!")

####################### 5-8 ###########################
# user_names = ['admin', 'andriy', 'victor', 'vlad', 'yuliya']
# for user in user_names:
#     if user == 'admin':
#         print(f"Hello {user}, would you like to see a status report?")
#     else:
#         print(f"Hello {user.title()}, thank you for logging in again.")

#################### 5-9 #########################################
# user_names = ['admin', 'andriy', 'victor', 'vlad', 'yuliya']
# for user in user_names:
#     if user == 'admin':
#         print(f"Hello {user}, would you like to see a status report?")
#     elif user =='andriy' or user == 'victor' or user == 'vlad' or user =='yuliya':
#         print(f"Hello {user.title()}, thank you for logging in again.")
#     else:
#         print("We need to find some users!")

# user_names = []
# for user in user_names:
#     if user == 'admin':
#         print(f"Hello {user}, would you like to see a status report?")
#     else:
#         print(f"Hello {user.title()}, thank you for logging in again.")
# else:
#         print("We need to find some users!")

########################### 5-10 ############################
# current_users = ['NADIYA', 'Andriy', 'victor', 'vlad', 'yuliya']
# new_users = ['nadiya', 'andriy', 'liliya', 'maria', 'dima']
# for new_user in new_users:
#     if new_user.lower() in current_users:
#         print(f"{new_user.title()}, you need enter a new username.")
#     else:
#         print(f"{new_user.title()}, you are available")
#
# ####################### 5-11 ##################################
# numbers = list(range(1,10))
# for number in numbers:
#     if number == 1:
#         print(f"{number}st")
#     elif number == 2:
#         print(f"{number}nd")
#     elif number == 3:
#         print(f"{number}rd")
#     else:
#         print(f"{number}th")

##################### 6-1 ###############################
# sister = {'first_name': 'lilia', 'last_name': 'pashchak', 'age': '39', 'city': 'lviv'}
# print(sister['first_name'])
# print(sister['last_name'])
# print(sister['age'])
# print(sister['city'])
# #
# print("Information about my sister:")
# print(f"\tfirst name: {sister['first_name'].title()}")
# print(f"\tlast name: {sister['last_name'].title()}")
# print(f"\tage: {sister['age']}")
# print(f"\tcity: {sister['city'].title()}")

###################### 6-2 ###############################
# favorite_numbers = {'viktor': '7', 'vlad': '17', 'nadia': '3', 'yuliya': '24', 'andriy': '14'}
# for key, value in favorite_numbers.items():
#     print(f"{key.title()}'s favorite number is {value}.")

# ################### 6-3/4 ####################################
# glossary = {'whitespace': 'not printable character',
#             'variable': 'storage for data',
#             'cmd': 'command promt',
#             'string': 'text',
#             'integer': 'number',
#             }
# for word, meaning in glossary.items():
#     print(f"\n{word.title()}: {meaning}.")

##################### 6-6 ################################
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# poll_names = ['jen', 'edward', 'phil', 'vlad', 'victor']
# for name in poll_names:
#     if name in favorite_languages:
#         print(f"{name.title()}, thank you for your responding!")
#     else:
#         print(f"{name.title()}, invite you to take a poll!")

######################## 6-7 ##############################
# person1 = {'first_name': 'lilia', 'last_name': 'pashchak', 'age': '39', 'city': 'lviv'}
# person2 = {'first_name': 'svitlana', 'last_name': 'vlasova', 'age': '35', 'city': 'berlin'}
# person3 = {'first_name': 'ira', 'last_name': 'romanuk', 'age': '37', 'city': 'lviv'}
# people = [person1, person2, person3]
# for person in people:
#     print(f"{person['first_name'].title()} {person['last_name'].title()} is {person['age']} years old and she lives in {person['city'].title()}.")

# ##################### 6-8 ###########################

pet1 = {'name': 'murca', 'kind': 'cat', 'owner': 'victor'}
pet2= {'name': 'rex', 'kind': 'dog', 'owner': 'mark'}
pet3 = {'name': 'july', 'kind': 'bird', 'owner': 'vlad'}
pets = [pet1, pet2, pet3]
for pet in pets:
        print(f"{pet['name'].title()} is {pet['owner'].title()}'s {pet['kind']}.")


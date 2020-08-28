##python- VScode, PyCharm, VIM
print("Hello World!!")
students = ('john', 'mark', 'aziz')
print(students)
print(students[0])
print(students[2])
print(students[1])
print(students[0])
print(f"hello, {students[1]}! Thank you!")
print(f"hello, {students[1].title()}! Thank you!")
cars = ['mazda', 'honda', 'audi']
print(f"I want to own {cars[1]}")
print(f"before : {cars}")
cars[2] = 'tesla'
print(f"after : {cars}")
###adding elements
#1. appending
cars.append('lexus')
print(cars)
#2. inserting
cars.insert(2,'toyota')
print(cars)

###removing
#1. delete by index
del cars[3]
print(cars)
#2. delete by value
cars.remove('mazda')
print(f"after remove: {cars}")
#3. delete last element
cars.pop()
print(f"after pop : {cars}")
#4. delete by index with pop
cars.pop(0)
print(f"after pop(0) : {cars}")

###guest list, 3-4, 3-5
print("===================3-4=================================")
guests = ['victor', 'vlad', 'yuliya']
print(guests)
print(f"Hello, {guests[0].title()}, invite you to my dinner!")
print(f"Hello, {guests[1].title()}, invite you to my dinner!")
print(f"Hello, {guests[2].title()}, invite you to my dinner!")
guest_not_coming = [ ]
guest_not_coming.append(guests[0])
guests[0] = 'andriy'
print(guests)
print(f"Welcome, {guests[0].title()}, to my dinner!")
print(f"Welcome, {guests[1].title()}, to my dinner!")
print(f"Welcome, {guests[2].title()}, to my dinner!")
print(f"Guests are coming : {guests}")
print(f"Guests are not coming : {guest_not_coming}")
print(f"Message: 'Hi, i just found a bigger dinner table, so now more space is avaible!'")
guests.insert(0,'maria')
guests.insert(2,'liliya')
guests.append('dima')
print(guests)
print(f"Welcome, {guests[0].title()}, to my dinner!")
print(f"Welcome, {guests[1].title()}, to my dinner!")
print(f"Welcome, {guests[2].title()}, to my dinner!")
print(f"Welcome, {guests[3].title()}, to my dinner!")
print(f"Welcome, {guests[4].title()}, to my dinner!")
print(f"Welcome, {guests[5].title()}, to my dinner!")
print(f"Message: I'm so sorry, but i can invite only two guests.")

print(f"Message: I'm so sorry, {guests[5].title()}, but i can't invite you to my dinner.")
guests.pop()
print(guests)
print(f"Message: I'm so sorry, {guests[4].title()}, but i can't invite you.")
guests.pop()
print(guests)
print(f"Message: I'm so sorry, {guests[3].title()}, but i can't invite you'.")
guests.pop()
print(guests)
print(f"Message: I'm so sorry, {guests[2].title()}, but i can't invite you'")
guests.pop()
print(guests)
print(F"{guests[0].title()}, you are still invited!")
print(F"{guests[1].title()}, you are still invited!")
print(guests)

print()
nums = [4, 9, 6, 1, 0, 44]
print(nums)
nums.reverse()
print(nums)
nums.sort(reverse = True)
print(nums)
print(len(nums))
print(nums[-1])
print(nums[-6])
print(f"========3-8=======")
places = ['ukraine', 'miami', 'dominican republic', 'greece']
print(places)
sorted_places = sorted(places)
print(sorted_places)
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse = True)
print(places)

num = [5, 8, 55, 63, 0, 4]
print(min(num))
print(max(num))
print(sum(num))

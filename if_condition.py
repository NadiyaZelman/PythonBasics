####IF conditions

# cars = ['lexus', 'buggati', 'bmw', 'ferrari']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# number = int(input("enter your number:"))
# if number%3 ==0 and number%5 ==0:
#     print("FuzzBuzz")
# elif number%3 == 0:
#     print("Fuzz")
# elif number%5 ==0:
#     print("Buzz")


for a in range(1, 11):
    for b in range(1, 11):
        print(f"{a} x {b} = {a * b}")
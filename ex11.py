# one way to ask input from the user:
age = input("How old are you? ")

# another possible way to ask input from the user:
print("How tall are you?", end=" ")
height = input()

# take an integer input from the user:
weight = int(input("How much do you weigh? "))

print("So you are %r old, %r tall and %r heavy." % (age, height, weight))
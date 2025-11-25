import math
initial = -1
final = -1
t = -1
while initial <= 0:
    try:
        initial = int(input("Enter initial number of cells (must be an integer greater than 0): "))
    except ValueError:
        print("Please enter a positive integer.")

while final <= 0:
    try:
        final = int(input("Enter final number of cells (must be an integer greater than 0): "))
    except ValueError:
        print("Please enter a positive integer.")

while t <= 0:
    try:
        t = float(input("Enter time elapsed in hours (must be greater than 0): "))
    except ValueError:
        print("Please enter a positive value.")

growth_rate = (math.log(final) - math.log(initial)) / t
print("Growth rate is: ", growth_rate)
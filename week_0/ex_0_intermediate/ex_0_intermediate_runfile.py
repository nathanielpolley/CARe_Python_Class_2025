#YOUR CODE FOR EX_0 INTERMEDIATE HERE
import math

initial_count = input("Enter the initial count:")
final_count = input("Enter the final count:")
time = input("Enter the time of growth :")

if initial_count.isdigit() and final_count.isdigit() and time.isdigit():
    print("Values are valid")
    initial_count = int(initial_count)
    final_count = int(final_count)
    time = int(time)
    if final_count > initial_count:
        growth_rate = (math.log(final_count) - math.log(initial_count)) / time
        print("The growth rate of the microbial culture is:", growth_rate)
    else:
        print("Final count must be greater than initial count.")
else:
    print("Values are invalid, please enter only entire and positive numbers")



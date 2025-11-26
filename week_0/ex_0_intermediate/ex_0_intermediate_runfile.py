#YOUR CODE FOR EX_0 INTERMEDIATE HERE
import math

print("This program calculates the growth rate of a microbial culture given the elapsed time and starting and ending conditions")

print("Enter initial cell count ")

try:
    initial_count = int(input())
except ValueError:
    print("Positive integer values only!")
if not(initial_count > 0):
    print("Positive integer values only!")

print("Enter final cell count")
try:
    final_count = int(input())
except ValueError:
    print("Positive integer values only!")
if not (final_count > 0):
    print("Positive integer values only!")

print("Enter time in hours ")
try:
    Time = float(input())
except ValueError:
    print("Positive numbers only!")
if not(Time > 0):
    print("Positive numbers only!")


growth_rate = (math.log(final_count)- math.log(initial_count))/Time
print("growth_rate: ", growth_rate)


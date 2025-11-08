#YOUR CODE FOR EX_0 INTERMEDIATE HERE
import math
initial_count = input("Enter initial_count")
final_count = input("Enter final_count")
time = input("Enter time")
if initial_count > final_count:
    print("ERROR! Go back and check again!")
elif initial_count.isdigit() and final_count.isdigit() and time.isdigit():
    x = int(initial_count)
    y = int(final_count)
    z = int(time)
    Growth_rate = (math.log(y) - math.log(x)) / z
    print(Growth_rate)
else:
    print("ERROR! Go back and check again!")




#YOUR CODE FOR EX_0 INTERMEDIATE HERE
import math

initial_count = input("Enter the initial count:").strip()
final_count = input("Enter the final count:").strip()
time = input("Enter the time:").strip()
if initial_count.isdigit() and final_count.isdigit() and time.isdigit():
    initial_count = int(initial_count)
    final_count = int(final_count)
    time = int(time)
    if initial_count >0 and final_count >0 and time> 0:
        growth_rate = (math.log(final_count) - math.log(initial_count)) / time
        print("Growth rate:", growth_rate)
    else:
        print("please enter a positive number")
else:
    print("please enter a valid number")

#YOUR CODE FOR EX_0 INTERMEDIATE HERE
import math
initial_count = input("Enter initial_count")
final_count = input("Enter final_count")
time = input("Enter time")
if initial_count.isdigit() and final_count.isdigit() and time.isdigit():
    x = int(initial_count)
    y = int(final_count)
    z = int(time)
    if x > y:
        print("Final count should higher than initial count")
    elif x<= 0 or y <= 0 or z <= 0:
        print("Error input")
    else:
        Growth_rate = (math.log(y) - math.log(x)) / z
        print(Growth_rate)
else:
    print ("ERROR! Go back and check again!")



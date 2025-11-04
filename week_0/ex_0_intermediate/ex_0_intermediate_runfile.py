import math
ini_str = input("initial cell number: ")
ini = float(ini_str)
final_str = input("final cell number: ")
final = float(final_str)
time_str = input("enter your time elapsed: ")
time = float(time_str)
if ini <= 0 or final <= 0:
    print("Error: No Cell counts")
elif time <= 0:
    print("Error: No Time elapsed")
else:
    growth_rate= (math.log(final) - math.log(ini)) / time
print(f"growth rate is : {growth_rate}")
#YOUR CODE FOR EX_0 INTERMEDIATE HERE

import math
ini_str = input("initial cell number: ")
final_str = input("final cell number: ")
time_str = input("enter your time elapsed: ")
if ini_str.isdigit() and final_str.isdigit() and time_str.isdigit():
    ini = float(ini_str)
    final = float(final_str)
    time = float(time_str)
    if ini <= 0 or final <= 0:
        print("Error: No Cell counts")
    elif time <= 0:
        print("Error: No Time elapsed")
    else:
        growth_rate= (math.ln(final) - math.ln(ini)) / time
        print(f"growth rate is : {growth_rate}")
else:
    print("Error: Incorrect Input")
#YOUR CODE FOR EX_0 INTERMEDIATE HERE

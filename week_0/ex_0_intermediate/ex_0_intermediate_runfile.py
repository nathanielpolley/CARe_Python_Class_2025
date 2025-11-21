import math
#Ask the user for values
initial_input = input("Enter initial cell count: ")
final_input = input("Enter final cell count: ")
time_input = input("Enter time elapsed (hours): ")

#Checking the validity of entries
if initial_input.isdigit() and final_input.isdigit() and time_input.isdigit():
    initial_count = int(initial_input)
    final_count = int(final_input)
    time = int(time_input)
#Verify that the values are positive and not zero.
    if initial_count > 0 and final_count > 0 and time > 0:
#Calculation of the growth rate
        growth_rate = (math.log(final_count) - math.log(initial_count)) / time
        print(f"Growth rate (μ): {growth_rate:.4f} h⁻¹")
#Doubling time calculation
        doubling_time = math.log(2) / growth_rate
        print(f"Doubling time: {doubling_time:.2f} h")
    else:
        print("Error: All input values must be positive and greater than zero.")
else:
    print("Error: Please enter whole positive numbers only (no letters, symbols, or decimals).")

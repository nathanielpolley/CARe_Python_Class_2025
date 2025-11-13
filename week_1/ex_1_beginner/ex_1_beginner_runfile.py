#YOUR CODE FOR EX_1 BEGINNER HERE
# ------------------------------------------------------------
# Script: microbial_population_analysis.py
# Purpose: Analyze microbial population data over five days
# using basic list operations and loops.
# ------------------------------------------------------------

# 1. Define the list of microbial population counts (example values)
populations = [100, 200, 150, 300, 50]

# 2. Calculate the average population
total = 0
for count in populations:
    total += count  # accumulate the total population count
average = total / len(populations)  # average = sum / number of elements

# 3. Find the maximum population
maximum = populations[0]
for count in populations:
    if count > maximum:
        maximum = count

# 4. Find the minimum population
minimum = populations[0]
for count in populations:
    if count < minimum:
        minimum = count

# 5. Identify the days when population exceeds 200
days_above_200 = []  # list to store the day numbers
for i in range(len(populations)):
    if populations[i] > 200:
        # Days are numbered starting from 1, so add 1 to the index
        days_above_200.append(i + 1)

# 6. Print the results
print("Microbial population over 5 days:", populations)
print("Average population:", average)
print("Maximum population:", maximum)
print("Minimum population:", minimum)
print("Days with population > 200:", days_above_200)

# ------------------------------------------------------------
# Expected output for the list [100, 200, 150, 300, 50]:
# Average = (100 + 200 + 150 + 300 + 50) / 5 = 160.0
# Maximum = 300
# Minimum = 50
# Days > 200 = [4]
# ------------------------------------------------------------

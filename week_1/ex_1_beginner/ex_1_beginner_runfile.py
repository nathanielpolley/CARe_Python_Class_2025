#List of microbial population counts for five consecutive days
population_counts = [100, 200, 150, 300, 50]
#Calculation of the average population count
average_population = sum(population_counts)/len(population_counts)
print("Average population count:", average_population)
#Calculation of the maximum population count
max_population= max(population_counts)
print("Maximum population count:", max_population)
#Calculation of the minimum population count
min_population = min(population_counts)
print("Minimum population count:", min_population)
#Use a for loop to identify the day(s) when the population exceeds 200 and print the number of the day(s) when the population is greater than 200
print("Day(s) when the population exceeds 200:")
for day_index, count in enumerate(population_counts, start=1):
    if count > 200:
        print("Day", day_index)
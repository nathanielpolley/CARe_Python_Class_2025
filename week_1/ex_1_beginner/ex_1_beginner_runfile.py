populations = [100, 200, 150, 300, 50]
total = 0
days = []

# Loop to determine sum of values in list followed by division by the number of items in the list to find the average.
for population in populations:
    total += population
average = total / len(populations)
print("Average population is: ", average)

# Sort list in ascending order and the value at index 0 will be the minimum.
minimum = sorted(populations)[0]
print("Minimum population is: ", minimum)

# Sort the list in ascending order and the value at the highest index value (number of items - 1) will be the maximum.
maximum = sorted(populations)[len(populations) - 1]
print("Maximum population is: ", maximum)

# Loop checking the value of items in the population list, if it's > 200 the index of the item is appended into
# another list. Because index values start at 0, add 1 to get the day number.
for population in populations:
    if population > 200:
        days.append(populations.index(population) + 1)
    else:
        continue
print("Microbial population was greater than 200 on the following days: ", days)
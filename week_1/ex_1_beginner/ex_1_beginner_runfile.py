#YOUR CODE FOR EX_1 BEGINNER HERE
#Create a Python script that defines a list of microbial population counts (e.g., [100, 200, 150, 300, 50]) for five
#       consecutive days.

micro_pop = [100, 200, 150, 300, 50]

length_pop = len(micro_pop)

#calculates the average population

tempsum=0

for i in range(length_pop):
    tempsum+=micro_pop[i]

print("Average microbial count: ", tempsum/length_pop)

#calculate the maximum population

tempmax=micro_pop[0]

for i in range(length_pop):
    if micro_pop[i] >= tempmax:
        tempmax=micro_pop[i]

print("Maximum microbial count: ", tempmax)

#calculate minimum population

tempmin = micro_pop[0]

for i in range(length_pop):
    if micro_pop[i] <= tempmin:
        tempmin = micro_pop[i]

print("Maximum microbial count: ", tempmin)

#Use a for loop to iterate through the population counts and identify days when the population exceeds 200. Print out
#       the day numbers when this occurs.

print("Population exceeds 200 on the following days: ")
for i in range(length_pop):
    if micro_pop[i] > 200:
        print("Day ", i+1)

#-Submit the Python runfile with comments explaining each step and the results of your calculations in the submit file.

#Sorry, polley, lifesaburrito is too lazy for that. :(
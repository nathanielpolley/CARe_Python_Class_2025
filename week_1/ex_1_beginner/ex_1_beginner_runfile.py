#YOUR CODE FOR EX_1 BEGINNER HERE
microbial_population = [100, 150,200,250,300]
print(min(microbial_population))
print(max(microbial_population))
average_population = sum(microbial_population) / len(microbial_population)
print(average_population)

day_number = 1
for num in microbial_population:
    if num > 200:
        print("The day number is: ", day_number)
    day_number += 1


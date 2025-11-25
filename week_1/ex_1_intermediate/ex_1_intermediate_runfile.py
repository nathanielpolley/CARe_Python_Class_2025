microbes = {"Bacteria": 20, "Archaea": 15, "Fungi": 10}
sample_total = 0
more_than_15 = []

# Adding up the values assigned to each key in the dictionary.
for key, value in microbes.items():
    sample_total += value
print("Total number of samples collected across all species: ", sample_total)

# Checking the value assigned to each key in the dictionary; if the value is > 15, the associated key is added to a
# list.
for key, value in microbes.items():
    if int(value) > 15:
        more_than_15.append(key)
    else:
        continue
print('Species with more than 15 samples: ', more_than_15)

# Loop for adding species or increasing sample count. If "no" is entered, the loop ends. If anything other than "no"
# is entered, the user is prompted to enter the species name. The dictionary is checked to see if the species already
# exists as a key. If it does, the value is increased by 1. If it doesn't, the species is added to the dictionary
# with a value of 1.
while True:
    userinput = input('Do you want to add another species? ')
    if userinput.lower() != 'no':
        species_name = input("Enter species name: ")
        if species_name in microbes:
            microbes[species_name] += 1
        else:
            microbes[species_name] = 1
    else:
        break

# After any additional species/samples are added by the user, a loop iterates through the dictionary and prints each
# key-value pair.
print('Species and sample counts:')
for key, value in microbes.items():
    print(key, value)
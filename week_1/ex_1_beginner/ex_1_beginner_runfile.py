#YOUR CODE FOR EX_1 BEGINNER HERE

data = input("Enter population count of microbial culture for 5 following days:").split()

if len(data) == 5 and all(item.isdigit() for item in data):
        print("Values are 5 numbers so they are valid")
        data = [int(item) for item in data]

        if all(data[i] < data[i + 1] for i in range(4)):
            for i in range(1, 6):
                print(f"day {i} -> {data[i-1]}")

            print(f"Maximum: {max(data)}")
            print(f"Minimum: {min(data)}")
            average = sum(data) / len(data)
            print(f"Average: {average}")

            for i in range(5):
                if data[i] > 200:
                    print(f"Population exceeded 200 on day {i + 1} with a value of: {data[i]}")
                    break
        else:
            print("But, values need to increase days after days")
else:
    print("Values are not valid, please enter 5 increasing numbers")

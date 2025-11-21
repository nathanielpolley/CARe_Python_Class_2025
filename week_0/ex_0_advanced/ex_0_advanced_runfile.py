#YOUR CODE FOR EX_0 ADVANCED HERE

sequence = input("Enter your DNA sequence:")

if sequence.isalpha() and set(sequence).issubset({"A", "C", "G", "T"}):
    print("The length of the sequence is:", (len(sequence)))
    count_A = sequence.count("A")
    count_T = sequence.count("T")
    count_G = sequence.count("G")
    count_C = sequence.count("C")

    print("Numbers of A is:", count_A)
    print("Numbers of T is:", count_T)
    print("Numbers of G is:", count_G)
    print("Numbers of C is:", count_C)

    count_GC = ((count_C + count_G) / (len(sequence)) * 100)
    print("Percentage of GC is:", count_GC)

else:
    print("Invalid DNA sequence, please enter ACGT type sequence")


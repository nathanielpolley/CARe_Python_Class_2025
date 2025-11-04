#YOUR CODE FOR EX_0 ADVANCED HERE
x = str(input("Enter your DNA sequence: ")).upper()

count_A = x.count("A")
count_T = x.count("T")
count_G = x.count("G")
count_C = x.count("C")
count_GCcontent = (x.count("G") + x.count("C"))/len(x)


print("count_A =", count_A, "count_T =", count_T, "count_G =", count_G, "count_C =", count_C, "GC content = count_GCcontent =", count_GCcontent )
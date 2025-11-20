inp=input( "enter DNA sequence: ")
DNA = inp.upper()
inv = 0
valid = {"A", "T", "G", "C"}
for Nu in DNA:
    if Nu not in valid:
        inv = inv + 1
        break
    else:
        a = DNA.count("A")
        c = DNA.count("C")
        g = DNA.count("G")
        t = DNA.count("T")
        length = a + c + g + t
        GC = (g+c)/length * 100
if inv == 0:
    print(f"length of DNA sequence is : {length}")
    print(f"Number of each nucleotide A C G T respectively:, {a } {c} {g} {t} ")
    print(f"GC content, {GC} %")
else:
    print("invalid nucleotide")


#YOUR CODE FOR EX_0 ADVANCED HERE

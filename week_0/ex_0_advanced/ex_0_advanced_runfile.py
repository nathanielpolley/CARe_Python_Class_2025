inp=input( "enter DNA sequence: ")
DNA = inp.upper()
a = DNA.count("A") 
c = DNA.count("C") 
g = DNA.count("G") 
t = DNA.count("T")
length = a + c + g + t
GC = (g+c)/length * 100
if length == 0:
    print("No DNA input")
else:
    print(f"length of DNA sequence is : {length}")
    print(f"Number of each nucleotide A C G T respectively:, {a } {c} {g} {t} ")
    print(f"GC content, {GC} %")
#YOUR CODE FOR EX_0 ADVANCED HERE

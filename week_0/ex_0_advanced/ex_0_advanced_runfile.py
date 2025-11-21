# DNA Sequence Analysis Script

def analyze_dna(sequence: str):
    """Analyze a DNA sequence and return base composition and GC content."""
    sequence = sequence.upper()

    # check of the validity
    valid_bases = {"A","C","G","T"}
    if not set(sequence).issubset(valid_bases):
        raise ValueError("Invalid DNA sequence: only A, C, G, and T are allowed.")

    # basic calcul
    length = len(sequence)
    count_a = sequence.count("A")
    count_c = sequence.count("C")
    count_g = sequence.count("G")
    count_t = sequence.count("T")

    # calcul of GC content
    gc_content = ((count_g + count_c) / length) * 100 if length > 0 else 0

    # results
    return {
        "Length": length,
        "A": count_a,
        "C": count_c,
        "G": count_g,
        "T": count_t,
        "GC_Content(%)": round(gc_content,2)
    }

# --- principal program---
if __name__ == "__main__":
    dna_seq = input("Enter a DNA sequence: ").strip()
    try:
        result = analyze_dna(dna_seq)
        print("\n--- DNA Sequence Analysis ---")
        for k, v in result.items():
            print(f"{k}: {v}")
    except ValueError as e:
        print(f"Error: {e}")

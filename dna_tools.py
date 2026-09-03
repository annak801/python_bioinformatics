def reverse_complement (sequence):
    new_string = ""
    sequence = sequence.upper()
    for base in sequence:
        if base == "A":
            new_string = new_string + "T"
        elif base == "T":
            new_string = new_string + "A"
        elif base == "G":
            new_string = new_string + "C"
        elif base == "C":
            new_string = new_string + "G"
        else:
            new_string = new_string + "N"
    return new_string [::-1]


def gc_content(sequence):
    gc_count=0
    for base in sequence:
        if base == "G" or base =="C":
            gc_count=gc_count+1
    gc_percentage = gc_count/len(sequence)*100
    return round(gc_percentage, 2)


seq1 = "ATGGCC"
seq2 = "AATTAA"
seq3 = "GGGCCC"

dna_sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA"
print(gc_content(dna_sequence))

for seq in [seq1, seq2, seq3]:
    print(f"{len(seq)}\t{gc_content(seq):.2f}")


sequences = ["AATT", "GCCAATGC", "GATTTTCAGC", "GGGCCCCCCAAAAAT"]
print(sequences)
sequences[0]
sequences[3]
len(sequences)


results = []

for sequence in sequences:
    results.append(gc_content(sequence))



def base_composition(sequence):
    base_counts = {}
    for base in sequence:
        if base in base_counts:
            base_counts[base] = base_counts[base] + 1
        else:
            base_counts[base] = 1
    return base_counts



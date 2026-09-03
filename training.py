base_composition = {}

sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA"

for base in sequence:
    if base in base_composition:
        base_composition[base] = base_composition[base] + 1
    else:
        base_composition[base] = 1

print(base_composition)



def base_composition(sequence):
    base_counts = {}
    for base in sequence:
        if base in base_counts:
            base_counts[base] = base_counts[base] + 1
        else:
            base_counts[base] = 1
    return base_counts

    

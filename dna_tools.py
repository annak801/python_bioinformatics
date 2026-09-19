def reverse_complement(sequence):
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



def base_composition(sequence):
    base_counts = {}
    for base in sequence:
        if base in base_counts:
            base_counts[base] = base_counts[base] + 1
        else:
            base_counts[base] = 1
    return base_counts


def get_gene_name(header):
    if "[gene=" in header:
        piece = header.split("[gene=")[1]
        name = piece.split("]")[0]
    else:
        name = header.strip()
    return name


def read_gene_list (filename):
    gene_set = set()
    with open (filename) as f:
        for line in f:
            line = line.strip()
            gene_set.add(line)
    return gene_set

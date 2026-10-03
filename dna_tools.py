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



codon_to_aa = {
    'TCA': 'S',    # Serina
    'TCC': 'S',    # Serina
    'TCG': 'S',    # Serina
    'TCT': 'S',    # Serina
    'TTC': 'F',    # Fenilalanina
    'TTT': 'F',    # Fenilalanina
    'TTA': 'L',    # Leucina
    'TTG': 'L',    # Leucina
    'TAC': 'Y',    # Tirosina
    'TAT': 'Y',    # Tirosina
    'TAA': '*',    # Stop
    'TAG': '*',    # Stop
    'TGC': 'C',    # Cisteina
    'TGT': 'C',    # Cisteina
    'TGA': '*',    # Stop
    'TGG': 'W',    # Triptofano
    'CTA': 'L',    # Leucina
    'CTC': 'L',    # Leucina
    'CTG': 'L',    # Leucina
    'CTT': 'L',    # Leucina
    'CCA': 'P',    # Prolina
    'CCC': 'P',    # Prolina
    'CCG': 'P',    # Prolina
    'CCT': 'P',    # Prolina
    'CAC': 'H',    # Histidina
    'CAT': 'H',    # Histidina
    'CAA': 'Q',    # Glutamina
    'CAG': 'Q',    # Glutamina
    'CGA': 'R',    # Arginina
    'CGC': 'R',    # Arginina
    'CGG': 'R',    # Arginina
    'CGT': 'R',    # Arginina
    'ATA': 'I',    # Isoleucina
    'ATC': 'I',    # Isoleucina
    'ATT': 'I',    # Isoleucina
    'ATG': 'M',    # Methionina
    'ACA': 'T',    # Treonina
    'ACC': 'T',    # Treonina
    'ACG': 'T',    # Treonina
    'ACT': 'T',    # Treonina
    'AAC': 'N',    # Asparagina
    'AAT': 'N',    # Asparagina
    'AAA': 'K',    # Lisina
    'AAG': 'K',    # Lisina
    'AGC': 'S',    # Serina
    'AGT': 'S',    # Serina
    'AGA': 'R',    # Arginina
    'AGG': 'R',    # Arginina
    'GTA': 'V',    # Valina
    'GTC': 'V',    # Valina
    'GTG': 'V',    # Valina
    'GTT': 'V',    # Valina
    'GCA': 'A',    # Alanina
    'GCC': 'A',    # Alanina
    'GCG': 'A',    # Alanina
    'GCT': 'A',    # Alanina
    'GAC': 'D',    # Acido Aspartico
    'GAT': 'D',    # Acido Aspartico
    'GAA': 'E',    # Acido Glutamico
    'GAG': 'E',    # Acido Glutamico
    'GGA': 'G',    # Glicina
    'GGC': 'G',    # Glicina
    'GGG': 'G',    # Glicina
    'GGT': 'G'     # Glicina
}

sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA"

protein =""

for i in range (0, len(sequence), 3): #assign codons to an amino acid, stop the loop at stop codons
    codon = sequence[i:i+3]
    amino_acid = codon_to_aa[codon]
    if amino_acid == "*":
        break
    protein = protein + amino_acid
print (protein)

    

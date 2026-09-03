genes = {}

header = ""

sequence = ""

with open("pd_genes.fasta") as f:
    for line in f:
        if line.startswith(">"):
            if header:
                genes[header] = sequence
            header = line.strip()
            sequence = ""
        else:
            sequence = sequence + line.strip()

genes[header] = sequence

for name, seq in genes.items():
    print(f"{name}\t{len(seq)}")

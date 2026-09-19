import sys
from dna_tools import get_gene_name, gc_content, base_composition

genes = {}

header = ""

sequence = ""


with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith(">"):
            if header:
                genes[header] = sequence
            header = get_gene_name(line)
            sequence = ""
        else:
            sequence = sequence + line.strip()

genes[header] = sequence


with open(sys.argv[2], "w") as out:
    out.write("Gene\tLength\tGC%\tBase composition\n")
    for name, seq in genes.items():
        out.write(f"{name}\t{len(seq)}\t{gc_content(seq):.2f}\t{base_composition(seq)}\n")


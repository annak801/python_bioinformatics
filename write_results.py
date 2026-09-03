sites = {"EcoRI": "GAATTC", "BamHI": "GGATCC", "HindIII": "AAGCTT",
         "NotI": "GCGGCCGC", "XhoI": "CTCGAG"}

def gc_content(seq):
    gc_count = 0
    for base in seq:
        if base == "G" or base == "C":
            gc_count = gc_count + 1
    gc_percentage = gc_count / len(seq) * 100
    return round(gc_percentage, 2)        

with open("gc_results.tsv","w") as f:
    f.write("Enzyme\tGC\n")
    for name, seq in sites.items():
        f.write(f"{name}\t{gc_content(seq):.2f}\n")
        

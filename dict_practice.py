sites = {"EcoRI": "GAATTC", "BamHI": "GGATCC", "HindIII": "AAGCTT", "NotI": "GCGGCCGC"}

sites ["XhoI"] = "CTCGAG"

def gc_content(site):
    gc_count = 0
    for base in site:
        if base == "G" or base == "C":
            gc_count = gc_count + 1
    return round(gc_count / len(site) * 100, 2)


results = []

for site in sites:
    results.append(gc_content(sites[site]))

print(f"Enzyme\t%GC")

for name, seq in sites.items():
    print(f"{name}\t{gc_content(seq):.2f}")
    

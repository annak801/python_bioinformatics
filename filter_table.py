import sys

if len(sys.argv) < 4:
    print ("Usage: python filter_table.py <input.tsv> <output.tsv> <gc_cutoff>")
    sys.exit(1)

cutoff = float(sys.argv[3])

with open (sys.argv[1]) as f, open (sys.argv[2],"w") as out:
    header = next(f)
    out.write (header)
    for line in f:
        columns = line.strip().split("\t")
        gc = float(columns[2])
        if gc > cutoff: #filter gene tsv by GC content and write them into new tsv
            out.write("\t".join(columns) + "\n")
            
            

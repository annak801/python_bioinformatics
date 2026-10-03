import sys

if len(sys.argv) < 5:
    print ("Usage: python filter_tsv.py <input.tsv> <output.tsv> <column> <cutoff>")
    sys.exit(1)

cutoff = float(sys.argv[4])


with open (sys.argv[1]) as f, open (sys.argv[2],"w") as out:
    header_line = next(f)
    header = header_line.strip().split("\t")
    col_pos = header.index(sys.argv[3])
    out.write (header_line)
    for line in f:
        columns = line.strip().split("\t")
        value = float(columns[col_pos])
        if value > cutoff: # keep rows above the cutoff and write them to the new tsv
            out.write("\t".join(columns) + "\n")

            
            

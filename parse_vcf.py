import matplotlib.pyplot as plt
import pandas as pd
import sys

if len(sys.argv) < 3:
     print("Usage: python parse_vcf.py <input.vcf> <output.tsv>")
     sys.exit(1)
     

list_data = []
filter_counts = {}
list_qual = []
list_af = []

with open (sys.argv[1]) as f, open (sys.argv[2], "w") as out:
    for line in f:
        if line.startswith("##"):
            continue
        elif line.startswith("#"):
            header = line.strip().lstrip("#").split("\t")
            filter_pos = header.index("FILTER")
            qual_pos = header.index("QUAL")
            info_pos = header.index("INFO")
            chrom_pos = header.index("CHROM")
            pos_pos = header.index("POS")
            id_pos = header.index("ID")
            ref_pos = header.index("REF")
            alt_pos = header.index("ALT")
            out.write("CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tAF\tTYPE\n")
        else:
            data = line.strip().split("\t")
            list_data.append(data)
            list_qual.append(float(data[qual_pos]))
            info = {}
            for item in data[info_pos].split(";"):
                if "=" in item:
                    parts = item.split("=")
                    info[parts[0]] = parts[1]
                else:
                    info[item] = True
            if "AF" in info:
                        af = info["AF"].split(",")[0]
                        list_af.append(float(af))
            else:
                 af = "NA"
            ref=data[ref_pos]
            alt= data[alt_pos]
            if len(ref) == 1 and len(alt) ==1:
                 vartype="SNV"
            else:
                 vartype = "INDEL"
#limitation: 2 SNVs could be called INDEL, MNVs are also not considered
            out.write(f"{data[chrom_pos]}\t{data[pos_pos]}\t{data[id_pos]}\t{ref}\t{alt}\t{data[qual_pos]}\t{data[filter_pos]}\t{af}\t{vartype}\n")        
            key_filter = data[filter_pos]
            if key_filter in filter_counts:
                filter_counts[key_filter] += 1
            else:
                filter_counts[key_filter] = 1
#for row in list_data:
#    print("\t".join(row))
 
#print(f"Header info:{header}\n")
print(f"Quality check: {filter_counts}\n")
#print(f"The confidence of each variant existing is:{list_qual}\n")


plt.hist(list_af, edgecolor = "black", bins = 10)
plt.title("Allele frequency distribution", size = 12, weight = "bold")
plt.xlabel ("AF", size = 12, weight = "bold")
plt.ylabel("N variants", size = 12, weight = "bold")
plt.yscale("log")
plt.show()
        
df = pd.DataFrame(list_data, columns = header)
#pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
print(df)

#print(list_af)


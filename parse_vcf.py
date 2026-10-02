import os
import matplotlib.pyplot as plt
import pandas as pd
os.chdir("C:/Users/Lenovo/Documents/Python")

list_data = []
filter_counts = {}
list_qual = []
list_af = []

with open ("simple.vcf") as f:
    for line in f:
        if line.startswith("##"):
            continue
        elif line.startswith("#"):
            header = line.strip().lstrip("#").split("\t")
            filter_pos = header.index("FILTER")
            qual_pos = header.index("QUAL")
            info_pos = header.index("INFO")
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
                        list_af.append(float(info["AF"].split(",")[0]))
                    
            key_filter = data[filter_pos]
            if key_filter in filter_counts:
                filter_counts[key_filter] += 1
            else:
                filter_counts[key_filter] = 1
for row in list_data:
    print("\t".join(row))
 
print(f"Header info:{header}\n")
print(f"Quality check: {filter_counts}\n")
print(f"The confidence of each variant existing is:{list_qual}\n")


plt.hist(list_qual, edgecolor = "black", bins = 10)
plt.title("Variant quality distribution", size = 12, weight = "bold")
plt.xlabel ("QUAL", size = 12, weight = "bold")
plt.ylabel("Number of variants", size = 12, weight = "bold")
#plt.show()
        
df = pd.DataFrame(list_data, columns = header)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
print(df)

print(list_af)

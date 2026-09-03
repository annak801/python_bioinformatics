with open ("gpr37.fna") as f:
    for line in f:
        print(line)

with open ("gpr37.fna") as f:
    contents = f.read()
    print (len(contents))

contents.startswith(">")

with open ("gpr37.fna") as f:
    for line in f:
        if not line.startswith(">"):
            print (line)

sequence = ""

with open ("gpr37.fna") as f:
    for line in f:
        if not line.startswith(">"):
            sequence = sequence + line.strip()

print(len(sequence))

def reverse_complement (sequence):
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

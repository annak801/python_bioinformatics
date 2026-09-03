def gc_content(sequence):
    gc_count=0
    for base in sequence:
        if base == "G" or base =="C":
            gc_count=gc_count+1
    gc_percentage = gc_count/len(sequence)*100
    return round(gc_percentage, 2)

            

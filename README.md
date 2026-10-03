# Bioinformatics scripts

Python tools for sequence and variant analysis.

## Tools

### dna_tools.py
Shared function library imported by the other tools:
- `gc_content(sequence)` — GC percentage, rounded to 2dp
- `reverse_complement(sequence)` — reverse complement; any non-ACGT base becomes N
- `base_composition(sequence)` — dictionary of per-base counts
- `translate(sequence)` — translates DNA to protein, stopping at the first stop
  codon. Includes the codon table
- `get_gene_name(header)` — pulls the gene symbol out of an NCBI `[gene=NAME]`
  FASTA header; falls back to the full header line if that field is absent
- `read_gene_list(filename)` — reads a one-name-per-line file into a set

### fasta_stats.py
Reads a multi-FASTA file and writes a TSV with per-gene length, GC content and
base composition. Handles sequences split across multiple lines.

    python fasta_stats.py pd_genes.fasta results.tsv

Requires `dna_tools.py` in the same folder.

### filter_tsv.py
Filters a TSV on any numeric column, keeping rows above a cutoff. The column is
selected by name from the header row, so it works on any table with a header,
not just the output of `fasta_stats.py`.

    python filter_tsv.py results.tsv high_gc.tsv GC% 50
    python filter_tsv.py results.tsv long_genes.tsv Length 1500

Chain two runs to filter on more than one column.

### parse_vcf.py
Parses a VCF file: skips the `##` meta-lines, reads the `#CHROM` header, looks
up columns by name, and splits the INFO field into a dictionary, handling both
`key=value` pairs and valueless flags. Counts FILTER values, collects QUAL and
allele frequency (taking the first value at multi-allelic sites), plots a QUAL
histogram, and loads the variants into a pandas DataFrame.

Run against the included `simple.vcf`.

## Data

- `pd_genes.fasta` —

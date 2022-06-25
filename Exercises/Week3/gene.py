# determine if a valid gene is present is a sequence of DNA
def gene(dna):
    # input string length must be > 6 and len(dna) multiple of 3
    if len(dna) % 3 != 0 or len(dna) <= 6: return False

    if not dna.startswith("ATG"): return False

    codon = [dna[i:i+3] for i in range(0,len(dna)-3,3)]

    if "TAA" in codon or "TAG" in codon or "TGA" in codon: return False

    if dna.endswith("TAA") or dna.endswith("TAG") or dna.endswith("TGA"):
        return True

    return False

def main():
    print("ATGCATACTGCATAG:", gene("ATGCATACTGCATAG"))
    print("ATGCGCTGCGTCTGTACTAG:", gene("ATGCGCTGCGTCTGTACTAG"))
    print("ATGCCGTGACGTCTGTACTAG:", gene("ATGCCGTGACGTCTGTACTAG"))

main()

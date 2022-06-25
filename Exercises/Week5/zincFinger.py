import re

#Check if a candidate sequence describes a protein in the C2H2-type zinc finger domain
def main():
    candidate = "CAASCGGPYACGGAAGYHAGAH"
    regularExpression = "C.{2,4}C...[LIVMFYWC].{8}H.{3,5}H"
    result = re.match(regularExpression, candidate)

    print("Candidate sequence:", candidate)
    print("Regular Expression:", regularExpression,"\n")
    
    if result:
        print("A match.  The sequence is in the domain.")
    else:
        print("No match.  The sequence is not in the domain")

main()

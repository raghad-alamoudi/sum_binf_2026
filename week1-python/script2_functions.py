DNA_string = "AGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC"
def count_nucleotides(DNA_string):
    count_A = 0
    count_G = 0
    count_C = 0
    count_T = 0
    for nucleotide in DNA_string:
        if nucleotide == 'A':
            count_A += 1
        elif nucleotide == 'G':
            count_G += 1
        elif nucleotide == 'C':
            count_C += 1            
        elif nucleotide == 'T':
            count_T += 1
    return dict(A=count_A, G=count_G, C=count_C, T=count_T)
nucleotide_counts = count_nucleotides(DNA_string)
print(nucleotide_counts)

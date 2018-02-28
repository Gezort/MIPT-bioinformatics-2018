TRANSLATION_MATRIX = {
    'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
    'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGU': 'S',
    'AUA': 'I', 'AUC': 'I', 'AUG': 'M', 'AUU': 'I',
    'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
    'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
    'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAU': 'D',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
    'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
    'UAA': 'X', 'UAC': 'Y', 'UAG': 'X', 'UAU': 'Y',
    'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
    'UGA': 'X', 'UGC': 'C', 'UGG': 'W', 'UGU': 'C',
    'UUA': 'L', 'UUC': 'F', 'UUG': 'L', 'UUU': 'F'
}

COMPLEMENT_MATRIX = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

def translate(rna):
    res = []
    for i in range(0, len(rna), 3):
        codon = rna[i:i + 3]
        if TRANSLATION_MATRIX[codon] == 'X':
            break
        res.append(TRANSLATION_MATRIX[codon])
    return ''.join(res)


def transcript(dna):
    return dna.replace('T', 'U')


def reverse_complement(dna):
    return ''.join([COMPLEMENT_MATRIX[ch] for ch in dna][::-1])


def main():
    dna = input()
    peptide = input()
    k = 3 * len(peptide) # pattern len
    result = []
    for i in range(len(dna) - k + 1):
        patterns = [dna[i:i + k], reverse_complement(dna[i:i + k])]
        for p in patterns:
            if peptide == translate(transcript(p)):
                result.append(patterns[0])
    print(*result, sep='\n')


if __name__ == '__main__':
    main()

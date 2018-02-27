from random import randint


def gene_counts(motifs):
    """for each position in 0..len(motifs[0]) - 1 calc gene distribution
    """
    res = []
    for i in range(len(motifs[0])):
        counts = {ch: 0 for ch in 'ACGT'}
        for j in range(len(motifs)):
            counts[motifs[j][i]] += 1
        res.append(counts)
    return res


def compute_score(motifs):
    score = 0
    for counts in gene_counts(motifs):
        score += len(motifs) - max(counts.values())
    return score


def form_profile(motifs):
    profile = []
    for counts in gene_counts(motifs):
        profile.append({x: (y + 1) / (4 + len(motifs)) for x, y in counts.items()})
    return profile


def get_most_probable_kmer(dna, k, profile):
    max_prob = 0
    index = 0
    for i in range(0, len(dna) - k + 1):
        prob = 1
        for j in range(k):
            prob *= profile[j][dna[i + j]]
        if prob > max_prob:
            max_prob = prob
            index = i
    return dna[index:index+k]


def select_random_motif(dna, k):
    ind = randint(0, len(dna) - k)
    return dna[ind:ind+k]


def main():
    k, t = list(map(int, input().split()))
    dna_matrix = [input() for _ in range(t)]
    motifs = [select_random_motif(dna, k) for dna in dna_matrix]
    best_motifs = motifs
    best_score = compute_score(best_motifs)
    for _ in range(1000):
        while True:
            profile = form_profile(motifs)
            motifs = [get_most_probable_kmer(dna, k, profile) for dna in dna_matrix]
            score = compute_score(motifs)
            if score < best_score:
                best_score = score
                best_motifs = motifs
            else:
                motifs = [select_random_motif(dna, k) for dna in dna_matrix]
                break
    print(*best_motifs, sep='\n')


if __name__ == '__main__':
    main()

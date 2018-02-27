from random import randint, random


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
        profile.append({x: (y + 1) / (4 + len(motifs))
                        for x, y in counts.items()})
    return profile


def motif_prob_within_profile(motif, profile):
    prob = 1
    for j in range(len(motif)):
        prob *= profile[j][motif[j]]
    return prob


def get_profile_randomly_generated_kmer(dna, k, profile):
    n = len(dna) - k + 1
    probs = [motif_prob_within_profile(dna[i:i+k], profile) * 10**4 for i in range(n)]
    rnd = random() * sum(probs)
    ind = -1
    for i in range(n):
        rnd -= probs[i]
        if rnd < 0:
            ind = i
            break
    return dna[ind:ind+k]


def select_random_motif(dna, k):
    ind = randint(0, len(dna) - k)
    return dna[ind:ind+k]


def main():
    k, t, N = list(map(int, input().split()))
    dna_matrix = [input() for _ in range(t)]
    res = []
    for _ in range(20):
        motifs = [select_random_motif(dna, k) for dna in dna_matrix]
        best_motifs = motifs
        best_score = compute_score(best_motifs)
        for u in range(N):
            i = randint(0, t - 1)
            profile = form_profile([motifs[j] for j in range(t) if j != i])
            motifs[i] = get_profile_randomly_generated_kmer(
                    dna_matrix[i], k, profile)
            score = compute_score(motifs)
            if score < best_score:
                best_score = score
                best_motifs = motifs
        res.append(best_motifs)
    best_motifs = min(res, key=lambda x: compute_score(x))
    print(*best_motifs, sep='\n')
    print(compute_score(best_motifs))


if __name__ == '__main__':
    main()

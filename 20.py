from collections import Counter
from itertools import chain
from tqdm import tqdm

ACIDS = []
LEADER_PEPTIDE = []


def get_best_with_ties(a, score_function, n):
    a = list(a)
    if len(a) <= n:
        return a
    a = sorted(a, key=lambda x: score_function(x), reverse=True)
    score_threshold = score_function(a[n - 1])
    while n < len(a) and score_function(a[n]) == score_threshold:
        n += 1
    return a[:n]


def most_frequent_convolutions(spectrum, m):
    convolution = []
    n = len(spectrum)
    for i in range(n):
        convolution.extend(abs(spectrum[j] - spectrum[i])
                           for j in range(i + 1, n))
    convolution = list(filter(lambda x: 57 <= x <= 200, convolution))
    c = Counter(convolution)
    return get_best_with_ties(set(convolution), lambda x: c[x], m)


def extend(peptids):
    for p in tqdm(peptids):
        for acid in ACIDS:
            yield p + [acid]


def cyclospectrum(peptide):
    spectrum = [0]
    prefix_sum = [0]
    for amin in peptide:
        prefix_sum.append(prefix_sum[-1] + amin)
    n = len(peptide)
    for i in range(n):
        spectrum.extend(prefix_sum[j] - prefix_sum[i]
                        for j in range(i + 1, n + 1))
        if i > 0:
            spectrum.extend(prefix_sum[n] - prefix_sum[j] + prefix_sum[i]
                            for j in range(i + 1, n))
    return sorted(spectrum)


def score(given_spectrum, peptide):
    spectrum = cyclospectrum(peptide)
    c = Counter(spectrum)
    return sum(min(cnt, given_spectrum[amin]) for amin, cnt in c.items()
               if amin in given_spectrum)


def cut_leaderboard(given_spectrum, peptids, n):
    global LEADER_PEPTIDE
    best = []
    parent_mass = max(given_spectrum)
    for p in list(peptids):
        p_mass = sum(p)
        if p_mass > parent_mass:
            continue
        best.append(p)
        if p_mass < parent_mass:
            continue
        if score(given_spectrum, p) > score(given_spectrum, LEADER_PEPTIDE):
            LEADER_PEPTIDE = p
    return get_best_with_ties(best, lambda p: score(given_spectrum, p), n)


def main():
    m = int(input()) - 1
    n = int(input())
    given_spectrum = list(map(int, input().split()))
    global ACIDS
    ACIDS = most_frequent_convolutions(given_spectrum, m)
    given_spectrum_values = Counter(given_spectrum)
    peptids = map(lambda x: [x], ACIDS)
    while peptids:
        peptids = extend(peptids)
        peptids = cut_leaderboard(given_spectrum_values, peptids, n)
    print('-'.join(map(lambda amin: str(amin), LEADER_PEPTIDE)))


if __name__ == '__main__':
    main()

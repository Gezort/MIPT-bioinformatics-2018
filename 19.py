from collections import Counter
from itertools import chain
from tqdm import tqdm

AMIN_TABLE = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'L', 'N', 'D', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
MASS_TABLE = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
AMIN_MASS = dict(zip(AMIN_TABLE, MASS_TABLE))

LEADER_PEPTIDE = ''

def extend(peptids):
    for p in peptids:
        for amin in AMIN_TABLE:
            yield p + amin


def cyclospectrum(peptide):
    spectrum = [0]
    prefix_sum = [0]
    for amin in peptide:
        prefix_sum.append(prefix_sum[-1] + AMIN_MASS[amin])
    n = len(peptide)
    for i in range(n):
        for j in range(i + 1, n + 1):
            spectrum.append(prefix_sum[j] - prefix_sum[i])
            if i > 0 and j < n:
                spectrum.append(prefix_sum[n] - prefix_sum[j] + prefix_sum[i])
    return sorted(spectrum)


def count_mass(peptide):
    return sum(AMIN_MASS[amin] for amin in peptide)


def score(given_spectrum, peptide):
    spectrum = cyclospectrum(peptide)
    c = Counter(spectrum)
    score = 0
    for amin, cnt in c.items():
        if amin in given_spectrum:
            score += min(cnt, given_spectrum[amin])
    return score


def cut_leaderboard(given_spectrum, parent_mass, peptids, n):
    global LEADER_PEPTIDE
    best = []
    for p in peptids:
        p_mass = count_mass(p)
        if p_mass > parent_mass:
            continue
        best.append(p)
        if p_mass == parent_mass:
            if score(given_spectrum, p) > score(given_spectrum, LEADER_PEPTIDE):
                LEADER_PEPTIDE = p
    best = sorted(best, key=lambda p: score(given_spectrum, p), reverse=True)
    if len(best) <= n:
        return best
    s = score(given_spectrum, best[n - 1])
    while n < len(best) and score(given_spectrum, best[n]) == s:
        n += 1
    return best[:n]


def main():
    n = int(input())
    given_spectrum = list(map(int, input().split()))
    parent_mass = max(given_spectrum)
    given_spectrum = Counter(given_spectrum)
    peptids = ['']
    while peptids:
        peptids = extend(peptids)
        peptids = cut_leaderboard(given_spectrum, parent_mass, peptids, n)
    print('-'.join(map(lambda amin: str(AMIN_MASS[amin]), LEADER_PEPTIDE)))


if __name__ == '__main__':
    main()

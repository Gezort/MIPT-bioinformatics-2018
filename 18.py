from collections import Counter
from itertools import chain
from tqdm import tqdm

AMIN_TABLE = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'L', 'N', 'D', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
MASS_TABLE = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
AMIN_MASS = dict(zip(AMIN_TABLE, MASS_TABLE))


def extend(peptids, parent_mass):
    extended = set()
    AMINS = ''.join(AMIN_TABLE)
    for p in peptids:
        ind = AMINS.find(p[0]) + 1 if p else 0
        p_mass = sum(AMIN_MASS[acid] for acid in p)
        for amin in AMIN_TABLE[ind:]:
            if AMIN_MASS[amin] + p_mass > parent_mass:
                break
            extended.add(p + amin)
    return extended


def count_mass(peptide):
    return sum([MASS_TABLE[acid] for acid in peptide])


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


def all_shifts(peptide):
    n = len(peptide)
    for i in range(n):
        yield '-'.join(map(lambda amin: str(AMIN_MASS[amin]), peptide[i:] + peptide[:i]))


def drop_unused_amins(given_spectrum):
    global AMIN_MASS, AMIN_TABLE, MASS_TABLE
    filtered = list(filter(lambda x: x[1] in given_spectrum, zip(AMIN_TABLE, MASS_TABLE)))
    AMIN_MASS = dict(filtered)
    AMIN_TABLE, MASS_TABLE = zip(*filtered)


def main():
    given_spectrum = list(map(int, input().split()))
    given_spectrum_values = Counter(given_spectrum)
    drop_unused_amins(given_spectrum)
    peptids = {''}
    result = set()
    while peptids:
        selected_peptids = set()
        for p in tqdm(peptids):
            spectrum = cyclospectrum(p)
            if spectrum[-1] > given_spectrum[-1]:
                continue
            if len(spectrum) > len(given_spectrum):
                continue
            if spectrum[-1] < given_spectrum[-1]:
                selected_peptids.add(p)
                continue
            if spectrum == given_spectrum:
                result.add(p)
        peptids = extend(selected_peptids, given_spectrum[-1])
    print(*chain(*map(lambda p: all_shifts(p), result)))


if __name__ == '__main__':
    main()

from collections import Counter
from functools import lru_cache
from math import factorial


AMIN_TABLE = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'L', 'N', 'D', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
MASS_TABLE = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
FACTORIALS = [factorial(i) for i in range(30)]


@lru_cache(maxsize=100000)
def peptides_count(mass, cur_amin, peptide):
    if cur_amin == len(AMIN_TABLE) and mass > 0:
        return 0
    if mass < 0:
        return 0
    if mass == 0:
        amin_counts = Counter(peptide)
        res = FACTORIALS[len(peptide)]
        for cnt in amin_counts.values():
            res //= FACTORIALS[cnt]
        return res
    else:
        res = peptides_count(mass - MASS_TABLE[cur_amin], cur_amin, peptide + AMIN_TABLE[cur_amin]) +\
            peptides_count(mass, cur_amin + 1, peptide)
        return res


def main():
    m = int(input())
    print(peptides_count(m, 0, ''))


if __name__ == '__main__':
    main()

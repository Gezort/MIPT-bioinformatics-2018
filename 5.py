from collections import defaultdict
from itertools import combinations_with_replacement as combinations
from itertools import permutations

def main():
    g = input()
    k,d = list(map(int, input().split()))
    counts = defaultdict(int)
    patterns = set()
    for pattern_characters in combinations('ACGT', k):
        for perm in permutations(pattern_characters, k):
            pattern = ''.join(perm)
            patterns.add(pattern)
    complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    for pattern in patterns:
        rev_pattern = list(map(lambda ch: complement[ch], pattern))
        rev_pattern = list(reversed(rev_pattern))
        for i in range(len(g) - k + 1):
            mistmatches = 0
            rev_mistmatches = 0
            for j in range(k):
                if pattern[j] != g[i + j]:
                    mistmatches += 1
                if rev_pattern[j] != g[i + j]:
                    rev_mistmatches += 1
            if mistmatches <= d:
                counts[pattern] += 1
            if rev_mistmatches <= d:
                counts[pattern] += 1
    entries = max(counts.values())
    print(*{p for p,cnt in counts.items() if cnt == entries})


if __name__ == '__main__':
    main()

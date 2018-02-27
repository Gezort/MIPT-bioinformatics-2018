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
    for pattern in patterns:
        for i in range(len(g) - k + 1):
            mistmatches = 0
            for j in range(k):
                if pattern[j] != g[i + j]:
                    mistmatches += 1
            if mistmatches <= d:
                counts[pattern] += 1
    entries = max(counts.values())
    print(*{p for p,cnt in counts.items() if cnt == entries})


if __name__ == '__main__':
    main()

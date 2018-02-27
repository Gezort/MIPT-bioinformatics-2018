def distance(pattern, dna):
    k = len(pattern)
    n = len(dna)
    res = k
    for i in range(n - k + 1):
        dist = 0
        for j in range(k):
            if pattern[j] != dna[i + j]:
                dist += 1
        res = min(res, dist)
    return res


def main():
    pattern = input()
    dna_matrix = input().split()
    print(sum([distance(pattern, dna) for dna in dna_matrix]))


if __name__ == '__main__':
    main()

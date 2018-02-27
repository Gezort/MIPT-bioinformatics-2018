import sys


def main():
    k = int(input())
    kmers = sys.stdin.read().strip().split('\n')
    n = len(kmers) + k - 1
    prefixes = set()
    sufixes = set()
    for kmer in kmers:
        prefixes.add(kmer[:k - 1])
        sufixes.add(kmer[1:])
    first_kmer_index = 0
    for i, kmer in enumerate(kmers):
        if kmer[:k - 1] not in sufixes:
            first_kmer_index = i
            break
    used = [False for _ in kmers]
    used[first_kmer_index] = True
    res = kmers[first_kmer_index]
    while not all(used):
        for i, kmer in enumerate(kmers):
            if used[i] or kmer[:k - 1] != res[-k + 1:]:
                continue
            used[i] = True
            # check if it's last kmer we should left it until the end
            if not all(used) and kmer[1:] not in prefixes:
                used[i] = False
                continue
            res += kmer[-1]
    print(res)


if __name__ == '__main__':
    main()

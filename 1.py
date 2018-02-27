from collections import defaultdict

def main():
    g = input()
    k,l,t = list(map(int, input().split()))
    ans = set()
    counts = defaultdict(int)
    for i in range(l - k):
        pattern = g[i : i + k]
        counts[pattern] += 1
    for p,c in counts.items():
        if c >= t:
            ans.add(p)
    for i in range(1, len(g) - l + 1):
        left = g[i - 1 : i + k - 1]
        right = g[i + l - k : i + l]
        counts[left] -= 1
        counts[right] += 1
        if counts[right] >= t:
            ans.add(right)
    print (' '.join(ans))

if __name__ == '__main__':
    main()

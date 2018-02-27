from collections import defaultdict

def main():
    p = input()
    t = input()
    d = int(input())
    l = len(p)
    ans = set()
    for i in range(len(t) - l + 1):
        mistmatches = 0
        for j in range(l):
            if t[j + i] != p[j]:
                mistmatches += 1
        if mistmatches <= d:
            ans.add(i)
    print (*sorted(ans))

if __name__ == '__main__':
    main()

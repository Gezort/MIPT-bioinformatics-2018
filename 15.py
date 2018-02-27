import sys

def main():
    k, d = map(int, input().split())
    patterns = sys.stdin.read().strip().split('\n')
    res = [patterns[0].split('|')[0]]
    for i in range(d):
        res.append(patterns[i + 1].split('|')[0][-1])
    res.append(patterns[0].split('|')[1])
    for pat in patterns[1:]:
        res.append(pat.split('|')[1][-1])
    print(''.join(res))


if __name__ == '__main__':
    main()

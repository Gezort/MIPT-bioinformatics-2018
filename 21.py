import sys

sys.setrecursionlimit(1000000)


def find_change(n, coins, cache):
    if n < 0:
        return len(cache)
    if cache[n] != -1:
        return cache[n]
    res = None
    for c in coins:
        if not res:
            res = find_change(n - c, coins, cache) + 1
        else:
            res = min(res, find_change(n - c, coins, cache) + 1)
    cache[n] = res
    return res


def main():
    n = int(input())
    cache = [-1 for _ in range(n + 1)]
    cache[0] = 0
    coins = list(map(int, input().split(',')))
    print(find_change(n, coins, cache))


if __name__ == '__main__':
    main()

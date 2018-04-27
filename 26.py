def print_permutation(permutation):
    print('(', end='')
    print(*['+{}'.format(p) if p > 0 else str(p) for p in permutation], end='')
    print(')')


def main():
    permutation = input()[1:-1]
    permutation = list(map(int, permutation.split()))
    n = len(permutation)
    for k in range(n):
        for i in range(n):
            if abs(permutation[i]) == k + 1:
                break
        if i == k and permutation[i] > 0:
            continue
        if i < k:
            permutation[i : k + 1] = permutation[i : k + 1][::-1]
            for j in range(i, k + 1):
                permutation[j] = -permutation[j]
        else:
            permutation[k : i + 1] = permutation[k : i + 1][::-1]
            for j in range(k, i + 1):
                permutation[j] = -permutation[j]
        print_permutation(permutation)
        if permutation[k] < 0:
            permutation[k] = -permutation[k]
            print_permutation(permutation)


if __name__ == '__main__':
    main()

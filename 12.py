def main():
    n = int(input())
    seq = ['1' for _ in range(n)]
    occurencies = {''.join(seq)}
    for i in range((1 << n) - n):
        next_met_pattern = ''.join(seq[-n + 1:] + ['0'])
        if next_met_pattern in occurencies:
            seq.append('1')
        else:
            seq.append('0')
        occurencies.add(''.join(seq[-n:]))
    print(''.join(seq))


if __name__ == '__main__':
    main()

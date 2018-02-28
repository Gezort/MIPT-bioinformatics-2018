MASS_TABLE = {
        'G': 57, 'A': 71, 'S': 87,
        'P': 97, 'V': 99, 'T': 101,
        'C': 103, 'I': 113, 'L': 113,
        'N': 114, 'D': 115, 'K': 128,
        'Q': 128, 'E': 129, 'M': 131,
        'H': 137, 'F': 147, 'R': 156,
        'Y': 163, 'W': 186
}


def main():
    s = input()
    n = len(s)
    res = []
    for l in range(n + 1):
        for i in range(n):
            mass = 0
            for j in range(l):
                mass += MASS_TABLE[s[(i + j) % n]]
            res.append(mass)
            if l % n == 0:
                break
    print (*sorted(res))


if __name__ == '__main__':
    main()

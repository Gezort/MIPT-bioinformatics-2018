def main():
    p = input()[1:-1]
    p = '{} {}'.format(p, len(p.split()) + 1)
    breakpoints = 0
    p = map(int, p.split())
    prev = 0
    for elem in p:
        if elem - prev != 1:
            breakpoints += 1
        prev = elem
    print(breakpoints)


if __name__ == '__main__':
    main()


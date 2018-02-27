from collections import defaultdict

def main():
    g = input()
    min_v = 0
    balance = 0
    indexes = {0}
    for i in range(len(g)):
        if g[i] == 'C':
            balance -= 1
        elif g[i] == 'G':
            balance += 1
        if balance == min_v:
            indexes.add(i + 1)
        elif balance < min_v:
            min_v = balance
            indexes = {i + 1}
    print (*sorted(indexes))

if __name__ == '__main__':
    main()

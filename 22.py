def main():
    n, m = map(int, input().split())
    horizontal_edges = []
    vertical_edges = []
    for i in range(n):
        row = map(int, input().split())
        vertical_edges.append(list(row))
    input()
    for i in range(n + 1):
        row = map(int, input().split())
        horizontal_edges.append(list(row))
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0] = 0
    for j in range(m):
        dp[0][j + 1] = dp[0][j] + horizontal_edges[0][j]
    for i in range(n):
        dp[i + 1][0] = dp[i][0] + vertical_edges[i][0]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(
                    dp[i - 1][j] + vertical_edges[i - 1][j],
                    dp[i][j - 1] + horizontal_edges[i][j - 1])
    print(dp[n][m])


if __name__ == '__main__':
    main()

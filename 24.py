import json
from tqdm import tqdm


class DPEntry:
    def __init__(self):
        self._previous_x = None
        self._previous_y = None
        self._value = -10000

    def update(self, from_x, from_y, value):
        if self._value < value:
            self._previous_x = from_x
            self._previous_y = from_y
            self._value = value

    def value(self):
        return self._value

    def x(self):
        return self._previous_x

    def y(self):
        return self._previous_y

    def __repr__(self):
        return str(self._value)


def main():
    with open('./PAM250.json', 'r') as f:
        PAM = json.load(f)
    s = input()
    t = input()
    n = len(s)
    m = len(t)

    dp = [[DPEntry() for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0].update(None, None, 0)
    for j in range(m):
        dp[0][j + 1].update(0, j, dp[0][j].value() + PAM['-'][t[j]])
        dp[0][j + 1].update(None, None, 0)
    for i in range(n):
        dp[i + 1][0].update(i, 0, dp[i][0].value() + PAM['-'][s[i]])
        dp[i + 1][0].update(None, None, 0)
    for i in tqdm(range(1, n + 1)):
        for j in range(1, m + 1):
            dp[i][j].update(
                    i, j - 1,
                    dp[i][j - 1].value() + PAM['-'][t[j - 1]]
                    )
            dp[i][j].update(
                    i - 1, j,
                    dp[i - 1][j].value() + PAM[s[i - 1]]['-']
                    )
            dp[i][j].update(
                    i - 1, j - 1,
                    dp[i - 1][j - 1].value() + PAM[s[i - 1]][t[j - 1]]
                    )
            dp[i][j].update(None, None, 0)
    res_s = []
    res_t = []
    i, j = n, m
    for candidate_i in range(n + 1):
        for candidate_j in range(m + 1):
            if dp[candidate_i][candidate_j].value() > dp[i][j].value():
                i, j = candidate_i, candidate_j
    print(dp[i][j].value())
    while i or j and dp[i][j].value() >= 0:
        if dp[i][j].x() == i:
            res_s.append('-')
            res_t.append(t[j - 1])
        elif dp[i][j].y() == j:
            res_s.append(s[i - 1])
            res_t.append('-')
        else:
            res_s.append(s[i - 1])
            res_t.append(t[j - 1])
        i, j = dp[i][j].x(), dp[i][j].y()
    print(''.join(res_s[:-1][::-1]), ''.join(res_t[:-1][::-1]), sep='\n')


if __name__ == '__main__':
    main()

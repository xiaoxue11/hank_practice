def common_child(a, b):
    m = len(a)
    n = len(b)
    cell = [[0]*(n+1) for j in range(m+1)]
    print(cell)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                cell[i][j] = cell[i-1][j-1] + 1
            else:
                cell[i][j] = max(cell[i-1][j], cell[i][j-1])
    print(cell)
    return cell[m][n]


def common_string(a, b):
    m, n = len(a), len(b)
    prev, cur = [0] * (n + 1), [0] * (n + 1)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                cur[j] = 1 + prev[j - 1]
            else:
                cur[j] = max(cur[j - 1], prev[j])
        cur, prev = prev, cur
    print(cur, prev)
    return prev[n]


if __name__ == '__main__':
    s1 = 'ABCDEF'
    s2 = 'FBDAMNB'
    common_child(s1, s2)
    print(common_string(s1, s2))

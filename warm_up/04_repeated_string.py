def repeated_string(s, n):
    return s.count('a')*(n//len(s)) + s[:n % len(s)].count('a')


if __name__ == '__main__':
    s = 'a'
    n = 1000000000000
    print(repeated_string(s, n))



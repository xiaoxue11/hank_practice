def alternating_characters(s1):
    steps = 0
    for i in range(len(s1)-1):
        if s1[i] == s1[i+1]:
            steps += 1
    return steps


if __name__ == '__main__':
    s = 'AAABBB'
    print(alternating_characters(s))
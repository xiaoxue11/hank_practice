def sub_str_count(s):
    nums = 0
    for i in range(1, len(s)+1):
        for j in range(len(s)-i+1):
            sub_string = s[j:j+i]
            if len(set(sub_string)) == 1:
                nums += 1
            elif (len(set(sub_string)) == 2) and (sub_string[::-1] == sub_string):
                nums += 1
    return nums


def sub_string_count(s):
    nums = 0
    n = len(s)
    sameChar = [0] * n
    i = 0
    while i < n:
        sameCharNum = 1
        j = i+1
        while j < n:
            if s[i] != s[j]:
                break
            sameCharNum += 1
            j += 1
        nums += int(sameCharNum*(sameCharNum+1)/2)
        sameChar[i] = sameCharNum
        i = j
    print(sameChar)
    for j in range(1, n):
        if s[j] == s[j-1]:
            sameChar[j] = sameChar[j-1]
        if (0 < j < n - 1) and s[j-1] == s[j+1] and s[j] != s[j-1]:
            nums += min(sameChar[j-1], sameChar[j+1])
    print(sameChar)
    print(s)
    return nums


if __name__ == '__main__':
    string = 'aabaaa'
    print(sub_string_count(string))
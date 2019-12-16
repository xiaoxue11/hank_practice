from collections import Counter


def make_anagram(a, b):
    nums = 0
    d1 = Counter(a)
    d2 = Counter(b)
    for k, v in d1.items():
        if k not in d2.keys():
            nums += v
        else:
            nums += abs(v - d2[k])
    for k, v in d2.items():
        if k not in d1.keys():
            nums += v
    print(d1)
    print(d2)
    print(nums)


if __name__ == '__main__':
    s1 = 'cde'
    s2 = 'dcf'
    make_anagram(s1, s2)
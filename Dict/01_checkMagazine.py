from collections import Counter


def check_magazine(a, b):
    d_a = Counter(a)
    d_b = Counter(b)
    for k, v in d_b.items():
        if k not in d_a.keys():
            print("No")
            return
        elif v > d_a[k]:
            print("No")
            return
        else:
            continue
    print('Yes')




if __name__ == '__main__':
    s1 = 'give me one grand today night'
    s2 = 'give one grand today'
    check_magazine(s1, s2)
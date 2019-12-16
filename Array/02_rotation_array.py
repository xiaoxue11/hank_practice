def rotation_left(a, d):
    for _ in range(d):
        ret = a.pop(0)
        # print(ret)
        a.append(ret)
        # print(a)
    return a


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    d = 4
    res = rotation_left(a, d)
    l1 = 3
    l2 = 8
    mid = (l1+l2) >> 1
    print(mid)
    print(a)
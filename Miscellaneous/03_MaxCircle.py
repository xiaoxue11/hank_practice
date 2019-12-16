"""
Created on :  10:08 AM
Author : Xue Zhang
"""


def max_circle1(queries):
    result = []
    d = {}
    for q1, q2 in queries:
        if q1 not in d and q2 not in d:
            d[q1] = [q1, q2]
            d[q2] = [q1, q2]
        elif q1 in d and q2 not in d:
            d[q1].append(q2)
            for key in d[q1]:
                d[key] = d[q1]
        elif q1 not in d and q2 in d:
            d[q2].append(q1)
            for key in d[q2]:
                d[key] = d[q1]
        elif q1 in d and q2 in d:
            keys = d[q1] + d[q2]
            for key in keys:
                d[key] = keys
        values = [len(v) for v in d.values()]
        result.append(max(values))
    return result


def max_circle2(queries):
    elems = {}  # reference for which set they are in
    groups = {}  # collection of the sets
    results = []
    maxl = 0
    for a, b in queries:
        if a not in elems:
            groups[a] = set([a])
            elems[a] = a
        if b not in elems:
            groups[b] = set([b])
            elems[b] = b
        if elems[a] != elems[b]:
            a, b = elems[a], elems[b]
            if len(groups[b]) > len(groups[a]):
                a, b = b, a
            groups[a] |= groups[b]
            for p in groups[b]:
                elems[p] = a
            del groups[b]
        print('The groups is: {}'.format(groups))
        print('The elems is : {}'.format(elems))
        maxl = max(maxl, len(groups[elems[a]]))
        results.append(maxl)
    return results


def get_root(x, links):
    while x != links[x]:
        x = links[links[x]]
    return x


def init(x, links, length):
    if x in links:
        return get_root(x, links)
    length[x] = 1
    links[x] = x
    return x


def max_circle(queries):
    links = {}
    length = {}
    result = []
    max_length = 2
    for a, b in queries:
        a = init(a, links, length)
        b = init(b, links, length)
        if a != b:
            if length[b] > length[a]:
                a, b = b, a
            links[b] = a
            length[a] += length[b]
            max_length = max(max_length, length[a])
        result.append(max_length)
    return result


if __name__ == '__main__':
    q_num = int(input())
    array = []
    for _ in range(q_num):
        array.append(list(map(int, input().rstrip().split())))
    ans = max_circle(array)
    print('\n'.join(map(str, ans)))

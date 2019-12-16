"""
Created on :  10:29 AM
Author : Xue Zhang
"""


def get_root(i, links):
    while i != links[i]:
        i = links[links[i]]
    return i


def roads_and_libraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return n * c_lib
    links = {i: i for i in range(1, n+1)}
    length = {i: 1 for i in range(1, n+1)}
    for a, b in cities:
        a = get_root(a, links)
        b = get_root(b, links)
        if a != b:
            if length[b] > length[a]:
                a, b = b, a
            links[b] = a
            length[a] += length[b]
    keys = [k for k in links if k == links[k]]
    ans = {}
    for k in keys:
        ans[k] = length[k] - 1
    total = len(ans) * c_lib + sum([c_road * v for v in ans.values()])
    return total


if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        nmC_libC_road = input().split()

        n_city = int(nmC_libC_road[0])

        m_road = int(nmC_libC_road[1])

        cost_lib = int(nmC_libC_road[2])

        cost_road = int(nmC_libC_road[3])

        cs = []

        for _ in range(m_road):
            cs.append(list(map(int, input().rstrip().split())))

        result = roads_and_libraries(n_city, cost_lib, cost_road, cs)

        print(result)

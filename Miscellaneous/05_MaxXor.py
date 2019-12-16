"""
Created on :  11:07 PM
Author : Xue Zhang
"""


def max_xor1(arr, queries):
    result = []
    for q in queries:
        max_val = q ^ arr[0]
        for v in arr:
            value = q ^ v
            if value > max_val:
                max_val = value
        result.append(max_val)
    return result


def max_xor(arr, queries):
    result = []
    trie = {}
    k = len(bin(max(arr + queries))) - 2
    for val in ['{:b}'.format(x).zfill(k) for x in arr]:
        node = trie
        for char in val:
            if char not in node:
                node[char] = {}
            node = node[char]
    for q in queries:
        node = trie
        s = ''
        for char in "{:b}".format(q).zfill(k):
            bit = str(int(char) ^ 1)
            bit = bit if bit in node else char
            s += bit
            node = node[bit]
        result.append(int(s, 2) ^ q)
    return result


def maxXor(arr, queries):
    ans = []
    trie = {}
    k = len(bin(max(arr+queries))) - 2
    # print(k)
    for number in ['{:b}'.format(x).zfill(k) for x in arr]:
        print(number)
        node = trie
        for char in number:
            if char not in node:
                node[char] = {}
            node = node[char]
        print(trie)
    for n in queries:
        node = trie
        print('the node is : {}'.format(node))
        s = ''
        for char in '{:b}'.format(n).zfill(k):
            tmp = str(int(char) ^ 1)
            tmp = tmp if tmp in node else char
            s += tmp
            node = node[tmp]
        print(s)
        ans.append(int(s, 2) ^ n)


if __name__ == '__main__':
    a = [1, 3, 5, 7]
    query = [17, 6]
    ret = max_xor(a, query)
    print('\n'.join(map(str, ret)))
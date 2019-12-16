"""
Created on :  2:44 PM
Author : Xue Zhang
"""
from collections import Counter
import string


def sherlock_and_anagrams(s):
    """暴力求解"""
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            for k in range(j+1, n):
                if Counter(s[j:j+i+1]) == Counter(s[k:k+1+i][::-1]):
                    count += 1
                    # print(s[j:j+1+i], s[k:k+i+1])
    return count



def sherlock_and_anagrams1(s):
    """find pattern and use dict to solve problems"""
    h = {}
    for i in range(len(s)):
        for j in range(i, len(s)):
            d = [0]*26
            sub_string = s[i:j+1]
            for char in sub_string:
                d[ord(char) - ord('a')] += 1
            d = tuple(d)
            # print(d)
            h[d] = h.get(d, 0) + 1
    # print(h)
    count = 0
    for values in h.values():
        count += values * (values - 1) //2
    return count


    # signatures = {}
          
    # # iterate over all substrings of s
    # for start in range(len(s)):
    #     for finish in range(start, len(s)):
    #         # initialize substring signature
    #         signature = [0]*26                                                                                                                                                                                                                                                                                                                                  `
    #         print(s[start:finish+1])
    #         for letter in s[start:finish+1]:
    #             signature[ord(letter)-ord('a')] += 1
    #         # tuples are hashable in contrast to lists
    #         signature = tuple(signature)
    #         print(signature)
    #         signatures[signature] = signatures.get(signature,0) + 1
    # print('*'*20)
    # print(signatures)
    # res = 0
    # for count in signatures.values():
    #     res += count*(count-1)//2
    # return res



if __name__ == '__main__':
    string = 'abba'
    print(sherlock_and_anagrams(string))
    print(sherlock_and_anagrams1(string))
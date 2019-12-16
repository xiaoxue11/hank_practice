"""
Created on :  10:41 PM
Author : Xue Zhang
"""


def luck_balance(k, contests):
    important_contests = [i[0] for i in contests if i[1] == 1]
    other_contests = [i[0] for i in contests if i[1] == 0]
    important_contests.sort()
    min_value = sum(other_contests)
    n = len(important_contests)
    lost_num = n - k
    j = 0
    for i in range(n):
        if j < lost_num:
            min_value -= important_contests[i]
            j += 1
        else:
            min_value += important_contests[i]
    return min_value


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luck_balance(k, contests)
    print(result)
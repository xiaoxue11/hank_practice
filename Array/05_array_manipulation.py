import time


def array_manipulation(n, queries):
    arr = [0]*n
    for i in queries:
        a = i[0]
        b = i[1]
        k = i[2]
        for j in range(a-1, b):
            arr[j] += k
    return max(arr)


def array_operator(n, queries):
    arr = [0] * (n+1)
    for i in queries:
        a = i[0] - 1
        b = i[1]
        k = i[2]
        arr[a] += k
        arr[b] -= k
    max_sum = 0
    current_sum = 0
    for i in arr:
        current_sum += i
        if max_sum < current_sum:
            max_sum = current_sum
    return max_sum


if __name__ == '__main__':
    num1 = 5
    num2 = 10
    q = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    p = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
    print(array_manipulation(num1, q))
    t1 = time.time()
    print(array_manipulation(num2, p))
    t2 = time.time()
    print(t2-t1)
    print(array_operator(num1, q))
    t3 = time.time()
    print(array_operator(num2, p))
    t4 = time.time()
    print(t4-t3)

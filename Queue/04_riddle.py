from collections import deque


def riddle(arr):
	""" find the maximum of the minimum(s) of every window size in the array """
	n = len(arr)
	li = []
	for i in range(1, n+1):
		stack = []
		for j in range(0, n-i+1):
			stack.append(min(arr[j:i+j]))
		li.append(max(stack))
	return li


def riddle1(arr):
	stack = deque()
	max_window = {}
	arr += [0,]
	for i, n in enumerate(arr):
		if not stack or n > stack[-1][1]:
			stack.append((i, n))
		else:
			while stack and stack[-1][1] >= n:
				if i-stack[-1][0] not in max_window or max_window[i-stack[-1][0]] < stack[-1][1]:
					max_window[i-stack[-1][0]] = stack[-1][1]
				p = stack.pop()
			stack.append((p[0], n))

	ans = [0]*(len(arr)-1)
	v_ant = min(max_window.values())
	for i in range(len(arr)-1, 0, -1):
		if i in max_window and max_window[i] > v_ant:
			ans[i-1] = max_window[i]
			v_ant = max_window[i]
		else:
			ans[i-1] = v_ant
	return ans

if __name__ == '__main__':
	a1 = [2, 6, 1, 12]
	a2 = [1, 2, 3, 5, 1, 13, 3]
	a3 = [3, 5, 4, 7, 6, 2]
	a4 = [2, 6, 1, 12]
	print(riddle1(a1))
	print(riddle1(a2))
	print(riddle1(a3))
	print(riddle1(a4))

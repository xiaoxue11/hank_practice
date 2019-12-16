def largest_rectangle(h):
	"""暴力求解"""
	n = len(h)
	max_area = 0
	for k in range(1, n+1):
		for i in range(0, n-k+1):
			min_h = min(h[i:i+k])
			area = min_h * k
			if area > max_area:
				max_area = area
	return max_area


def largest_rectangle1(h):
	"""find algorithm pattern to solve the problem"""
	h.append(0)
	stack = []
	max_area = 0
	for i, height in enumerate(h):
		j = i
		while stack and stack[-1][1] >= height:
			# print(stack)
			j, last = stack.pop()
			area = (i - j) * last
			if area > max_area:
				max_area = area
		stack.append((j, height))

	return max_area



if __name__ == '__main__':
	h = [3, 2, 3]
	# h = [1, 2, 3, 4, 5]
	print(largest_rectangle(h))
	print(largest_rectangle1(h))

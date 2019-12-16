def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	num = len(arr)//2
	left = merge_sort(arr[:num])
	right = merge_sort(arr[num:])
	result = []
	l, r = 0, 0
	while l < len(left) and r < len(right):
		if left[l] < right[r]:
			result.append(left[l])
			l += 1
		else:
			result.append(right[r])
			r += 1
	result += left[l:]
	result += right[r:]
	return result
	

if __name__ == '__main__':
	s = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	print(merge_sort(s))


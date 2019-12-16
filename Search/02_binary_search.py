def binary_search1(arr, value):
	"""递归查找"""
	n = len(arr)
	if n > 0:
		mid = n//2
		if arr[mid] == value:
			return True
		elif arr[mid] > value:
			return binary_search1(arr[:mid], value)
		else:
			return binary_search1(arr[mid+1:], value)
	return False


def binary_search(arr, value):
	"""非递归方式"""
	n = len(arr)
	low = 0
	high = n-1
	while low <= high:
		mid = (low + high) // 2
		print(mid)
		if arr[mid] == value:
			return True
		elif arr[mid] > value:
			high = mid - 1
		else:
			low = mid + 1
	return Flase


if __name__ == '__main__':
	li = [15, 24, 89, 90, 95, 100]
	print(binary_search1(li, 89))
	print(binary_search1(li, 91))
	print(binary_search(li, 89))
	print(binary_search1(li, 91))

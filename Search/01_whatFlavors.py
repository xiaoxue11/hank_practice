def what_flavors(cost, money):
	d = {}
	for i, c in enumerate(cost):
		if c in d:
			result= (d[c], i + 1)
			print(' '.join(map(str, result)))
			return 
		d[money - c] = i+1


if __name__ == '__main__':
    array = [1,4, 5, 3, 2]
    target = 4
    what_flavors(array, target)
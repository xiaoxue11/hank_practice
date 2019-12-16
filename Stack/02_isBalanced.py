def is_balanced(s):
	d = {'{': '}', '(': ')', '[': ']'}
	h = {'}': '{', ')': '(', ']': '[' }
	stack = [] 
	for i in s: 
		if i in d: 
			stack.append(i) 
		elif i in h: 
			print(stack)
			print(i)
			if (len(stack) > 0) and (h[i] == stack[-1]): 
				stack.pop() 
			else: 
				return "NO"
	if len(stack) == 0: 
		return "YES" 


def is_balaced(s):
	lefts = '{[('
	rights = '}])'
	closes = { a:b for a,b in zip(rights,lefts)}
	stack = []
	for c in s:
		if c in lefts:
			stack.append(c)
		elif c in rights:
			if not stack or stack.pop() != closes[c]:
				return False
	return "NO" if stack else "YES"


if __name__ == '__main__':
	string = '{{[[(())]]}}'
	print(is_balanced(string))
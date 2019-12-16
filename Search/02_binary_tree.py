class Node:
	"""tree node"""
	def __init__(self, data):
		self.data = data
		self.lchild = None
		self.rchild = None


class Tree:
	"""binary tree"""
	def __init__(self):
		self.root = None

	def add(self, value):
		node = Node(value)
		if self.root is None:
			self.root = node
			return
		q = [self.root]
		while q:
			cur_node = q.pop(0)
			if cur_node.lchild is None:
				cur_node.lchild = node
				return
			else:
				q.append(cur_node.lchild)
			if cur_node.rchild is None:
				cur_node.rchild = node
				return
			else:
				q.append(cur_node.rchild)

	def breadth_travel(self):
		if self.root is None:
			return
		q = [self.root]
		while q:
			cur_node = q.pop(0)
			print(cur_node.data, end=' ')
			if cur_node.lchild:
				q.append(cur_node.lchild)
			if cur_node.rchild:
				q.append(cur_node.rchild)

	def pre_order(self, node):
		if node is None:
			return
		print(node.data, end=' ')
		self.pre_order(node.lchild)
		self.pre_order(node.rchild)

	def in_order(self, node):
		if node is None:
			return
		self.in_order(node.lchild)
		print(node.data, end=' ')
		self.in_order(node.rchild)

	def post_order(self, node):
		if node is None:
			return
		self.post_order(node.lchild)
		self.post_order(node.rchild)
		print(node.data, end=' ')


if __name__ == '__main__':
	tree = Tree()
	for i in range(10):
		tree.add(i)
	tree.breadth_travel()
	print('\n')
	tree.pre_order(tree.root)
	print('\n')
	tree.in_order(tree.root)
	print('\n')
	tree.post_order(tree.root)


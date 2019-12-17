import math


class TreeNode:
	def __init__(self, value):
		self.value = value
		self.children = set()
		self.total_sum = None


def construct_tree(tree_values, tree_edges):
	nodes = [TreeNode(value) for value in tree_values]
	for tree_start, tree_end in tree_edges:
		nodes[tree_start - 1].children.add(nodes[tree_end - 1])
		nodes[tree_end - 1].children.add(nodes[tree_start - 1])
	return nodes[0]


def calculate_tree_sum(root):
	stack = (root, None)
	visited = set()
	while stack:
		node = stack[0]
		if node not in visited:
			visited.add(node)
			for child in node.children:
				child.children.remove(node)
				stack = (child, stack)
		else:
			stack = stack[-1]
			node.total_sum = sum(map(lambda x: x.total_sum, node.children)) + node.value


def is_even_number(value):
    return not value & 1 


def find_best_balanced_forest(root):
	stack = (root, None)
	visited, visited_sums, root_complement_sums = set(), set(), set()
	min_result_value = math.inf
	while stack:
		selected_node = stack[0]
		if selected_node not in visited:
			visited.add(selected_node)
			for child in selected_node.children:
				stack = (child, stack)
			selected_sum_comp = root.total_sum - selected_node.total_sum
			root_complement_sums.add(selected_sum_comp)
			if (selected_node.total_sum * 2 in visited_sums or root.total_sum - selected_node.total_sum * 2 in visited_sums) and selected_node.total_sum * 3 >= root.total_sum:
				candidate_value = selected_node.total_sum * 3 - root.total_sum
				if candidate_value < min_result_value:
					min_result_value = candidate_value
		else:
			if selected_node.total_sum * 2 == root.total_sum:
				candidate_value = selected_node.total_sum
				if candidate_value < min_result_value:
					min_result_value = candidate_value
			if (selected_node.total_sum in visited_sums or selected_node.total_sum in root_complement_sums) and selected_node.total_sum * 3 >= root.total_sum:
				candidate_value = selected_node.total_sum * 3 - root.total_sum
				if candidate_value < min_result_value:
					min_result_value = candidate_value

			selected_sum_comp = root.total_sum - selected_node.total_sum

			if is_even_number(selected_sum_comp):
				selected_sum_comp_half = selected_sum_comp // 2
				if selected_sum_comp_half > selected_node.total_sum and (selected_sum_comp_half in visited_sums or
					selected_sum_comp_half in root_complement_sums):
					candidate_value = selected_sum_comp_half - selected_node.total_sum 
					if candidate_value < min_result_value:
						min_result_value = candidate_value

			root_complement_sums.remove(selected_sum_comp)
			visited_sums.add(selected_node.total_sum)
			stack = stack[-1]

	if min_result_value == math.inf:
		min_result_value = -1
	return min_result_value

if __name__ == '__main__':
	values = [15, 12, 8, 14, 13]
	edges = [[1, 2], [1, 3], [1, 4], [4, 5]]
	root = construct_tree(values, edges)
	print(root)
	calculate_tree_sum(root)
	ans = find_best_balanced_forest(root)
	print(ans)
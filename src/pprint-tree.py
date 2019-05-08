from binarytree import tree, bst, heap, pprint

# Generate a random binary tree and return its root
my_tree = tree(height=5, balanced=False)

# Generate a random BST and return its root
my_bst = bst(height=5)

# Generate a random max heap and return its root
my_heap = heap(height=3, max=True)

# Pretty print the trees in stdout
pprint(my_tree)
pprint(my_bst)
pprint(my_heap)
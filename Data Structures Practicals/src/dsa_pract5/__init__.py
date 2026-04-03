"""
Question #1

Implement a Binary Search Tree (BST) with:
- Insert
- Search
- Delete
- Traversals (BFS + DFS)
"""

class BinarySearchTree:
    # Node class for each element in the BST
    class Node:
        def __init__(self, data):
            self.data = data      # Store value of the node
            self.left = None      # Pointer to left child
            self.right = None     # Pointer to right child

    def __init__(self):
        self.root = None  # Initialize an empty tree

    # Insert a new value into the BST
    def insert(self, data):
        if not self.root:
            # If tree is empty, new node becomes the root
            self.root = self.Node(data)
        else:
            # Otherwise recursively insert new data
            self._insert_rec(self.root, data)

    # Helper recursive insertion function
    def _insert_rec(self, node, data):
        if data < node.data:
            # Insert in left subtree
            if node.left is None:
                node.left = self.Node(data)
            else:
                self._insert_rec(node.left, data)
        else:
            # Insert in right subtree
            if node.right is None:
                node.right = self.Node(data)
            else:
                self._insert_rec(node.right, data)

    # Search for a value in the BST
    def search(self, key):
        return self._search_rec(self.root, key)

    # Helper recursive search function
    def _search_rec(self, node, key):
        # If node is None or key matches node's data
        if node is None or node.data == key:
            return node is not None

        # Choose left or right subtree based on key value
        if key < node.data:
            return self._search_rec(node.left, key)
        return self._search_rec(node.right, key)

    # Public delete function
    def delete(self, key):
        self.root = self._delete_rec(self.root, key)

    # Helper recursive delete function
    def _delete_rec(self, node, key):
        if node is None:
            return node

        # Traverse tree to find the node to delete
        if key < node.data:
            node.left = self._delete_rec(node.left, key)
        elif key > node.data:
            node.right = self._delete_rec(node.right, key)
        else:
            # Node found: handle 3 cases

            # Case 1: No left child
            if node.left is None:
                return node.right

            # Case 2: No right child
            elif node.right is None:
                return node.left

            # Case 3: Node with two children
            # Replace with inorder successor (minimum of right subtree)
            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete_rec(node.right, temp.data)

        return node

    # Helper to find minimum value node (used for deletion)
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Inorder traversal (Left → Root → Right)
    def inorder_traversal(self):
        elements = []
        self._inorder_rec(self.root, elements)
        return elements

    def _inorder_rec(self, node, elements):
        if node:
            self._inorder_rec(node.left, elements)
            elements.append(node.data)
            self._inorder_rec(node.right, elements)

    # Preorder traversal (Root → Left → Right)
    def preorder_traversal(self):
        elements = []
        self._preorder_rec(self.root, elements)
        return elements

    def _preorder_rec(self, node, elements):
        if node:
            elements.append(node.data)
            self._preorder_rec(node.left, elements)
            self._preorder_rec(node.right, elements)

    # Postorder traversal (Left → Right → Root)
    def postorder_traversal(self):
        elements = []
        self._postorder_rec(self.root, elements)
        return elements

    def _postorder_rec(self, node, elements):
        if node:
            self._postorder_rec(node.left, elements)
            self._postorder_rec(node.right, elements)
            elements.append(node.data)

    # Breadth-first traversal (level order)
    def breadth_first_traversal(self):
        elements = []
        if not self.root:
            return elements

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            elements.append(current.data)

            # Enqueue children
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return elements


"""
Question #2
Iterative versions of DFS traversals
"""

# Iterative Inorder (L → R)
def iterative_inorder_traversal(root):
    elements = []
    stack = []
    current = root

    # Simulates recursion using stack
    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        elements.append(current.data)
        current = current.right

    return elements

# Iterative Preorder (R → L because stack reverses order)
def iterative_preorder_traversal(root):
    elements = []
    if not root:
        return elements

    stack = [root]
    while stack:
        current = stack.pop()
        elements.append(current.data)

        # Order reversed because stack is LIFO
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return elements

# Iterative Postorder using two stacks
def iterative_postorder_traversal(root):
    elements = []
    if not root:
        return elements

    stack1 = [root]
    stack2 = []

    # First stack builds reversed postorder
    while stack1:
        current = stack1.pop()
        stack2.append(current)

        if current.left:
            stack1.append(current.left)
        if current.right:
            stack1.append(current.right)

    # Second stack holds correct order
    while stack2:
        current = stack2.pop()
        elements.append(current.data)

    return elements


"""
Question #3
Count total nodes using DFS traversal
"""
def count_nodes(root):
    if root is None:
        return 0
    # Count current node + left subtree + right subtree
    return 1 + count_nodes(root.left) + count_nodes(root.right)


"""
Question #4
Count leaf nodes (nodes with no children)
"""
def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1  # Leaf node
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)


"""
Question #5
Check if two BSTs are identical in structure & values
"""
def are_identical_trees(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        return (
            root1.data == root2.data and
            are_identical_trees(root1.left, root2.left) and
            are_identical_trees(root1.right, root2.right)
        )

    return False  # Structure mismatch


"""
Question #6
Build a height-balanced BST from a sorted list
"""
def minimize_bst_height(sorted_array):
    if not sorted_array:
        return None

    mid = len(sorted_array) // 2
    node = BinarySearchTree.Node(sorted_array[mid])

    # Recursively build left and right balanced subtrees
    node.left = minimize_bst_height(sorted_array[:mid])
    node.right = minimize_bst_height(sorted_array[mid + 1:])

    return node


def main():
    # Build a sample BST
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    # Test recursive traversals
    print("InOrder Traversal (Recursive):", bst.inorder_traversal())
    print("PreOrder Traversal (Recursive):", bst.preorder_traversal())
    print("PostOrder Traversal (Recursive):", bst.postorder_traversal())
    print("Breadth-First Traversal:", bst.breadth_first_traversal())

    # Test iterative traversals
    print("InOrder Traversal (Iterative):", iterative_inorder_traversal(bst.root))
    print("PreOrder Traversal (Iterative):", iterative_preorder_traversal(bst.root))
    print("PostOrder Traversal (Iterative):", iterative_postorder_traversal(bst.root))

    # Count nodes
    print("Total Nodes in BST:", count_nodes(bst.root))

    # Count leaf nodes
    print("Leaf Nodes in BST:", count_leaf_nodes(bst.root))

    # Compare identical trees
    bst2 = BinarySearchTree()
    bst2.insert(50)
    bst2.insert(30)
    bst2.insert(70)
    bst2.insert(20)
    bst2.insert(40)
    bst2.insert(60)
    bst2.insert(80)
    print("Are BSTs Identical:", are_identical_trees(bst.root, bst2.root))

    # Build a balanced BST
    sorted_array = [20, 30, 40, 50, 60, 70, 80]
    balanced_bst_root = minimize_bst_height(sorted_array)
    print("Balanced BST InOrder Traversal:", iterative_inorder_traversal(balanced_bst_root))


if __name__ == "__main__":
    main()

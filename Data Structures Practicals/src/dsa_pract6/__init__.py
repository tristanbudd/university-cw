"""
Question #1

Implement a 2-3 Tree (B Tree of order 3). Hint: Refer to the definition and constraints regarding the number of nodes and
elements in a 2-3 Tree. Recall that a typical 2-3 Tree requires the following CRUD operations:
 Insert Insert a new element to the 2-3 Tree
 Search Search for an element in the 2-3 Tree (similar to N-ary search)
 Traverse Access each element in the 2-3 Tree (breadth first and depth first)
 Delete (Advanced) Delete an element from the 2-3 Tree
"""
class TwoThreeTree:
    class Node:
        def __init__(self, keys=None, children=None):
            self.keys = keys or []
            self.children = children or []

        @property
        def is_leaf(self):
            return len(self.children) == 0

    def __init__(self):
        self.root = None

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, node, key):
        if node is None:
            return False

        if key in node.keys:
            return True

        if node.is_leaf:
            return False

        if len(node.keys) == 1:
            if key < node.keys[0]:
                return self._search_rec(node.children[0], key)
            else:
                return self._search_rec(node.children[1], key)
        else:
            if key < node.keys[0]:
                return self._search_rec(node.children[0], key)
            elif key < node.keys[1]:
                return self._search_rec(node.children[1], key)
            else:
                return self._search_rec(node.children[2], key)

    def insert(self, key):
        if self.root is None:
            self.root = self.Node([key], [])
        else:
            promoted = self._insert(self.root, key)
            if promoted:
                # Split root
                new_root = self.Node([promoted[0]], [promoted[1], promoted[2]])
                self.root = new_root

    def _insert(self, node, key):
        # Insert into leaf
        if node.is_leaf:
            node.keys.append(key)
            node.keys.sort()

            if len(node.keys) <= 2:
                return None  # no split needed

            # Split 3 keys
            return self._split(node)

        # Determine child
        if len(node.keys) == 1:
            child_idx = 0 if key < node.keys[0] else 1
        else:
            if key < node.keys[0]:
                child_idx = 0
            elif key < node.keys[1]:
                child_idx = 1
            else:
                child_idx = 2

        promoted = self._insert(node.children[child_idx], key)

        if not promoted:
            return None

        # Insert promoted key
        middle, left_child, right_child = promoted

        node.keys.insert(child_idx, middle)
        node.children[child_idx] = left_child
        node.children.insert(child_idx + 1, right_child)

        if len(node.keys) <= 2:
            return None

        return self._split(node)

    def _split(self, node):
        """
        Split a node with 3 keys into:
        - middle key promoted
        - left and right nodes returned
        """
        left = self.Node([node.keys[0]])
        right = self.Node([node.keys[2]])

        if not node.is_leaf:
            left.children = node.children[:2]
            right.children = node.children[2:]

        return (node.keys[1], left, right)

    def delete(self, key):
        if not self.root:
            return

        self._delete(self.root, key)

        # Shrink root if needed
        if len(self.root.keys) == 0 and not self.root.is_leaf:
            self.root = self.root.children[0]

    def _delete(self, node, key):
        if node.is_leaf:
            if key in node.keys:
                node.keys.remove(key)
            return

        # Find child index
        if len(node.keys) == 1:
            if key < node.keys[0]:
                idx = 0
            elif key == node.keys[0]:
                # Replace with inorder successor
                successor = self._get_min(node.children[1])
                node.keys[0] = successor
                self._delete(node.children[1], successor)
                return
            else:
                idx = 1
        else:
            if key < node.keys[0]:
                idx = 0
            elif key == node.keys[0]:
                successor = self._get_min(node.children[1])
                node.keys[0] = successor
                self._delete(node.children[1], successor)
                return
            elif key < node.keys[1]:
                idx = 1
            elif key == node.keys[1]:
                successor = self._get_min(node.children[2])
                node.keys[1] = successor
                self._delete(node.children[2], successor)
                return
            else:
                idx = 2

        # Recurse
        self._delete(node.children[idx], key)

        # Fix child if underflow
        self._fix(node, idx)

    def _fix(self, parent, idx):
        """
        Ensures child at index idx has at least 1 key.
        Attempts rotate then merge.
        """
        child = parent.children[idx]

        if len(child.keys) > 0:
            return  # OK

        # Try borrow from left sibling
        if idx > 0:
            left = parent.children[idx - 1]
            if len(left.keys) > 1:
                # rotate right
                child.keys.insert(0, parent.keys[idx - 1])
                parent.keys[idx - 1] = left.keys.pop()
                if not left.is_leaf:
                    child.children.insert(0, left.children.pop())
                return

        # Try borrow from right sibling
        if idx < len(parent.children) - 1:
            right = parent.children[idx + 1]
            if len(right.keys) > 1:
                # rotate left
                child.keys.append(parent.keys[idx])
                parent.keys[idx] = right.keys.pop(0)
                if not right.is_leaf:
                    child.children.append(right.children.pop(0))
                return

        # Merge with sibling
        if idx > 0:
            left = parent.children[idx - 1]
            left.keys.append(parent.keys.pop(idx - 1))
            left.keys.extend(child.keys)
            if not child.is_leaf:
                left.children.extend(child.children)
            parent.children.pop(idx)
        else:
            right = parent.children[idx + 1]
            child.keys.append(parent.keys.pop(idx))
            child.keys.extend(right.keys)
            if not right.is_leaf:
                child.children.extend(right.children)
            parent.children.pop(idx + 1)

    def _get_min(self, node):
        while not node.is_leaf:
            node = node.children[0]
        return node.keys[0]

    def traverse(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return

        if len(node.keys) == 1:
            if not node.is_leaf:
                self._inorder(node.children[0], result)
            result.append(node.keys[0])
            if not node.is_leaf:
                self._inorder(node.children[1], result)

        else:
            if not node.is_leaf:
                self._inorder(node.children[0], result)
            result.append(node.keys[0])
            if not node.is_leaf:
                self._inorder(node.children[1], result)
            result.append(node.keys[1])
            if not node.is_leaf:
                self._inorder(node.children[2], result)


"""
Question #2
Implement a B Tree of order N (N>=2). Hint: Refer to the definition and constraints regarding the number of nodes and
elements. Recall that a typical B Tree requires the following CRUD operations:
 Insert Insert a new element to the B Tree
 Search Search for an element in the B Tree (similar to N-ary search)
 Traverse Access each element in the B Tree (breadth first and depth first)
 Delete (Advanced) Delete an element from the B Tree
"""
class BTree:
    def __init__(self, t):
        if t < 2:
            raise ValueError("B-Tree minimum degree t must be >= 2")
        self.root = self.Node(t)
        self.t = t  # minimum degree

    class Node:
        def __init__(self, t):
            self.t = t
            self.keys = []
            self.children = []
            self.leaf = True

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = self.Node(self.t)
            new_root.leaf = False
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_non_full(new_root, key)
        else:
            self._insert_non_full(root, key)

    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, index):
        t = self.t
        full_child = parent.children[index]
        new_child = self.Node(t)
        new_child.leaf = full_child.leaf
        parent.children.insert(index + 1, new_child)
        parent.keys.insert(index, full_child.keys[t - 1])

        new_child.keys = full_child.keys[t:(2 * t - 1)]
        full_child.keys = full_child.keys[0:(t - 1)]

        if not full_child.leaf:
            new_child.children = full_child.children[t:(2 * t)]
            full_child.children = full_child.children[0:t]

    def traverse(self):
        result = []
        self._traverse_rec(self.root, result)
        return result

    def _traverse_rec(self, node, result):
        for i in range(len(node.keys)):
            if not node.leaf:
                self._traverse_rec(node.children[i], result)
            result.append(node.keys[i])
        if not node.leaf:
            self._traverse_rec(node.children[len(node.keys)], result)

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return True
        if node.leaf:
            return False
        return self._search_rec(node.children[i], key)

    def delete(self, key):
        if not self.root:
            return
        self._delete_rec(self.root, key)
        # If root has no keys and is internal, make its first child the new root
        if len(self.root.keys) == 0 and not self.root.leaf:
            self.root = self.root.children[0]

    def _delete_rec(self, node, key):
        t = self.t
        idx = 0
        # Find first key >= key
        while idx < len(node.keys) and key > node.keys[idx]:
            idx += 1

        # Key is present in this node
        if idx < len(node.keys) and node.keys[idx] == key:
            if node.leaf:
                # Node is leaf -> remove key
                node.keys.pop(idx)
                return
            else:
                # Node is internal
                # If left child has >= t keys, replace with predecessor
                if len(node.children[idx].keys) >= t:
                    pred = self._get_predecessor(node, idx)
                    node.keys[idx] = pred
                    self._delete_rec(node.children[idx], pred)
                # Else if right child has >= t keys, replace with successor
                elif len(node.children[idx + 1].keys) >= t:
                    succ = self._get_successor(node, idx)
                    node.keys[idx] = succ
                    self._delete_rec(node.children[idx + 1], succ)
                else:
                    # Both children have t-1 keys -> merge them with key and recurse
                    self._merge_children(node, idx)
                    self._delete_rec(node.children[idx], key)
                return

        # Key not present in this node
        else:
            if node.leaf:
                return
            # Ensure child idx has at least t keys before recursing
            if len(node.children[idx].keys) == t - 1:
                # Try borrow from left sibling
                if idx - 1 >= 0 and len(node.children[idx - 1].keys) >= t:
                    self._borrow_from_prev(node, idx)
                # Try borrow from right sibling
                elif idx + 1 < len(node.children) and len(node.children[idx + 1].keys) >= t:
                    self._borrow_from_next(node, idx)
                else:
                    # Merge with a sibling
                    if idx + 1 < len(node.children):
                        self._merge_children(node, idx)
                    else:
                        # Merge with left sibling
                        self._merge_children(node, idx - 1)
                        idx = idx - 1
            # After ensuring child has >= t keys, recurse
            self._delete_rec(node.children[idx], key)

    def _get_predecessor(self, node, idx):
        cur = node.children[idx]
        while not cur.leaf:
            cur = cur.children[len(cur.keys)]
        return cur.keys[-1]

    def _get_successor(self, node, idx):
        cur = node.children[idx + 1]
        while not cur.leaf:
            cur = cur.children[0]
        return cur.keys[0]

    def _borrow_from_prev(self, parent, idx):
        child = parent.children[idx]
        left_sib = parent.children[idx - 1]

        # Move parent's key down to child's front
        child.keys.insert(0, parent.keys[idx - 1])
        if not left_sib.leaf:
            child.children.insert(0, left_sib.children.pop())
        # Bring left sibling's last key up to parent
        parent.keys[idx - 1] = left_sib.keys.pop()

    def _borrow_from_next(self, parent, idx):
        child = parent.children[idx]
        right_sib = parent.children[idx + 1]

        # Move parent's key down to child's end
        child.keys.append(parent.keys[idx])
        if not right_sib.leaf:
            child.children.append(right_sib.children.pop(0))
        # Bring right sibling's first key up to parent
        parent.keys[idx] = right_sib.keys.pop(0)

    def _merge_children(self, parent, idx):
        """
        Merge parent.keys[idx] and parent.children[idx+1] into parent.children[idx]
        After merge, parent.children[idx] will have keys: left.keys + [parent.keys[idx]] + right.keys
        and children = left.children + right.children (if any)
        """
        left = parent.children[idx]
        right = parent.children[idx + 1]
        t = self.t

        # Pull down the key from parent into left
        left.keys.append(parent.keys[idx])
        # Append right's keys
        left.keys.extend(right.keys)
        # Append right's children if any
        if not left.leaf:
            left.children.extend(right.children)

        # Remove key and right child from parent
        parent.keys.pop(idx)
        parent.children.pop(idx + 1)


"""
Question #3

(Advanced) Determine whether a B Tree of order 2 qualifies as anAVLTree. Justify your answer either by coding with an arbitrary sequence of data for insertion and deletion, or through a written analysis.
Hint: In an AVL Tree, the difference in heights of the subtrees for any given node is no more than 1. 
"""
def is_btree_avl(btree):
    def check_avl(node):
        if node is None:
            return 0, True

        heights = []
        is_avl = True

        for child in node.children:
            height, child_is_avl = check_avl(child)
            heights.append(height)
            is_avl = is_avl and child_is_avl

        if heights:
            min_height = min(heights)
            max_height = max(heights)
            if max_height - min_height > 1:
                is_avl = False
            return max_height + 1, is_avl
        else:
            return 1, is_avl

    _, avl_status = check_avl(btree.root)
    return avl_status


"""
Question #3

Implement a B+ Tree of order N (N>=2):
Hint: n a B+ Tree, data is stored exclusively in the leaf nodes. Define two node types:
leaves and non-leaves. Recall that a typical B+ Tree requires the following CRUD operations:
 Insert Insert a new element to the B+ Tree
 Search Search for an element in the B+ Tree (similar to N-ary search)
 Traverse Access each element in the B+ Tree (noting that all data items arestored in the leaf nodes in a B+ Tree)
 Delete (Advanced) Delete an element from the B+ Tree
"""
class BPlusTree:
    class Node:
        def __init__(self, t, leaf=False):
            self.t = t
            self.keys = []
            self.children = []
            self.leaf = leaf
            self.next = None   # leaf link

    def __init__(self, t):
        self.t = t
        self.root = self.Node(t, leaf=True)

    def search(self, key):
        node = self.root
        while not node.leaf:
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            node = node.children[i]
        return key in node.keys

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t - 1):
            new_root = self.Node(self.t)
            new_root.children.append(root)
            self._split_internal(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        if node.leaf:
            i = len(node.keys) - 1
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            child = node.children[i]
            if len(child.keys) == (2 * self.t - 1):
                self._split_internal(node, i)
                if key >= node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_internal(self, parent, idx):
        t = self.t
        child = parent.children[idx]
        new_node = self.Node(t, leaf=child.leaf)

        mid = t - 1
        parent.keys.insert(idx, child.keys[mid])
        parent.children.insert(idx + 1, new_node)

        new_node.keys = child.keys[mid + 1:]
        child.keys = child.keys[:mid]

        if not child.leaf:
            new_node.children = child.children[t:]
            child.children = child.children[:t]
        else:
            new_node.next = child.next
            child.next = new_node

    def traverse(self):
        node = self.root
        while not node.leaf:
            node = node.children[0]
        result = []
        while node:
            result.extend(node.keys)
            node = node.next
        return result

    def delete(self, key):
        self._delete_rec(self.root, key)
        if not self.root.leaf and len(self.root.keys) == 0:
            self.root = self.root.children[0]

    def _delete_rec(self, node, key):
        if node.leaf:
            if key in node.keys:
                node.keys.remove(key)
            return

        idx = 0
        while idx < len(node.keys) and key >= node.keys[idx]:
            idx += 1

        child = node.children[idx]
        self._delete_rec(child, key)

        if len(child.keys) < self.t - 1:
            self._fix(node, idx)

    def _fix(self, parent, idx):
        t = self.t
        child = parent.children[idx]

        if idx > 0 and len(parent.children[idx - 1].keys) > t - 1:
            left = parent.children[idx - 1]
            if child.leaf:
                child.keys.insert(0, left.keys.pop())
                parent.keys[idx - 1] = child.keys[0]
            else:
                child.keys.insert(0, parent.keys[idx - 1])
                parent.keys[idx - 1] = left.keys.pop()
                child.children.insert(0, left.children.pop())
            return

        if idx < len(parent.children) - 1 and len(parent.children[idx + 1].keys) > t - 1:
            right = parent.children[idx + 1]
            if child.leaf:
                child.keys.append(right.keys.pop(0))
                parent.keys[idx] = right.keys[0]
            else:
                child.keys.append(parent.keys[idx])
                parent.keys[idx] = right.keys.pop(0)
                child.children.append(right.children.pop(0))
            return

        if idx > 0:
            left = parent.children[idx - 1]
            left.keys.extend(child.keys)
            if not child.leaf:
                left.children.extend(child.children)
            if left.leaf:
                left.next = child.next
            parent.keys.pop(idx - 1)
            parent.children.pop(idx)
        else:
            right = parent.children[idx + 1]
            child.keys.extend(right.keys)
            if not child.leaf:
                child.children.extend(right.children)
            if child.leaf:
                child.next = right.next
            parent.keys.pop(idx)
            parent.children.pop(idx + 1)


def main():
    # Question #1
    print("--- Question #1 ---")
    tree = TwoThreeTree()

    for x in [5, 1, 9, 3, 7, 2, 6, 4, 8]:
        tree.insert(x)

    print(tree.traverse())

    tree.delete(5)
    tree.delete(1)

    print(tree.traverse())

    # Question #2
    print("--- Question #2 ---")
    bt = BTree(2)
    for k in [10, 20, 5, 6, 12, 30, 7, 17]:
        bt.insert(k)
    print("Traverse before deletes:", bt.traverse())
    bt.delete(6)
    bt.delete(13)
    bt.delete(7)
    print("Traverse after deletes:", bt.traverse())
    print("Search 17 (should be True):", bt.search(17))
    print("Search 6 (should be False):", bt.search(6))

    # Question #3
    print("--- Question #3 ---")
    btree = BTree(2)
    for key in [30, 20, 40, 10, 25, 35, 50]:
        btree.insert(key)

    print("Is B-Tree of order 2 an AVL Tree?", is_btree_avl(btree))

    btree2 = BTree(2)

    for key in [50, 40, 60, 55, 70, 65, 80]:
        btree2.insert(key)

    btree2.delete(40)
    btree2.delete(50)

    print("Is B-Tree of order 2 an AVL Tree?", is_btree_avl(btree2))

    # Conclusion: Algorithm seems to work and always fix the balance.

    # Question #4
    print("--- Question #4 ---")
    bpt = BPlusTree(2)

    for k in [10, 20, 5, 6, 12, 30, 7, 17, 25, 3, 15]:
        bpt.insert(k)

    print("Traverse:", bpt.traverse())
    print("Search 12:", bpt.search(12))
    print("Search 19:", bpt.search(19))

    bpt2 = BPlusTree(3)
    for k in [50, 10, 40, 60, 30, 20, 70, 55, 65, 75]:
        bpt2.insert(k)

    print("Traverse (order 3):", bpt2.traverse())
    print("Search 65:", bpt2.search(65))
    print("Search 99:", bpt2.search(99))


if __name__ == "__main__":
    main()

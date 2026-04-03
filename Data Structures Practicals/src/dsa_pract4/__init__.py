"""
Question #1

Implement a Singly Linked List (SLL):
A typical SLL supports the following operations:

• Insert  → Add a new node to the end of the list  
• Search  → Look for a value in the list  
• Delete  → Remove a node with a specific value  
• Traverse → Access each node in order  
"""

class SinglyLinkedList:
    # Node class for each element in the list
    class Node:
        def __init__(self, data):
            self.data = data      # Value held by the node
            self.next = None      # Pointer to the next node

    def __init__(self):
        self.head = None  # Start with an empty list

    # Insert a new value at the end of the list
    def insert(self, data):
        new_node = self.Node(data)

        # If the list is empty, new node becomes the head
        if not self.head:
            self.head = new_node
            return

        # Otherwise traverse to the end of the list
        last = self.head
        while last.next:
            last = last.next

        # Link new node at the end
        last.next = new_node

    # Search for a value in the list; return True if found
    def search(self, key):
        current = self.head

        # Traverse nodes sequentially
        while current:
            if current.data == key:
                return True
            current = current.next

        return False  # Not found

    # Delete the first node containing the specified key
    def delete(self, key):
        current = self.head
        prev = None

        # Traverse until node to delete is found
        while current and current.data != key:
            prev = current
            current = current.next

        # If value not present, nothing to delete
        if not current:
            return

        # If node is not head, bypass it
        if prev:
            prev.next = current.next
        else:
            # If deleting head, update head pointer
            self.head = current.next

    # Traverse list and collect values in Python list
    def traverse(self):
        elements = []
        current = self.head

        # Append each node's data to result list
        while current:
            elements.append(current.data)
            current = current.next

        return elements


"""
Question #2

Design an algorithm to sort a Singly Linked List (SLL).

Approach used here: Merge Sort  
- Well-suited for linked lists  
- Splits list in half using slow/fast pointers  
- Recursively sorts each half  
- Merges sorted halves back together  
"""
def sort_sll(sll):

    # Split linked list into two halves
    def split(head):
        slow, fast = head, head.next

        # Move fast pointer twice as fast as slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list at the slow pointer
        middle = slow.next
        slow.next = None
        return head, middle

    # Merge two sorted linked lists into one
    def merge_sorted_lists(left, right):
        dummy = SinglyLinkedList.Node(0)
        tail = dummy

        # Compare elements from both lists; append smallest
        while left and right:
            if left.data <= right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        # Append any remaining elements
        tail.next = left or right
        return dummy.next

    # Recursive merge sort
    def merge_sort(head):
        # Base case: list of 0 or 1 item already sorted
        if not head or not head.next:
            return head

        left, right = split(head)

        # Sort each half recursively
        left = merge_sort(left)
        right = merge_sort(right)

        # Merge the two sorted halves
        return merge_sorted_lists(left, right)

    # Update SLL's head with sorted version
    sll.head = merge_sort(sll.head)
    return sll


"""
Question #3

Design an algorithm to reverse a SLL.

Approach:
- Reverses the pointers one at a time  
- Uses three pointers: prev, current, next  
- After traversal, prev becomes new head  
"""
def reverse_sll(sll):
    prev = None
    current = sll.head

    # Reverse the direction of next pointers
    while current:
        next_node = current.next   # Save next node
        current.next = prev        # Reverse pointer
        prev = current             # Move prev forward
        current = next_node        # Move current forward

    # New head of reversed list
    sll.head = prev
    return sll


"""
Question #4

Design an algorithm to remove the N-th node from the end of a SLL.

Technique: Two-Pointer (Fast/Slow)
- Move fast pointer n+1 steps ahead  
- Move both pointers until fast reaches end  
- Slow pointer will be just before the target node  
"""
def remove_nth_from_end(sll, n):
    dummy = SinglyLinkedList.Node(0)
    dummy.next = sll.head

    first = dummy
    second = dummy

    # Move first pointer ahead by n+1 positions
    for _ in range(n + 1):
        if first:
            first = first.next

    # Move both pointers until first reaches the end
    while first:
        first = first.next
        second = second.next

    # Delete the target node
    if second.next:
        second.next = second.next.next

    # Update head (important when removing original head)
    sll.head = dummy.next
    return sll


"""
Question #5

Design an algorithm to merge two sorted SLLs into one sorted SLL.

Approach:
- Use pointers to traverse both lists  
- Append smallest node each step  
- Continue until both lists fully consumed  
"""
def merge_two_sorted_slls(sll1, sll2):
    dummy = SinglyLinkedList.Node(0)
    tail = dummy

    p1 = sll1.head
    p2 = sll2.head

    # Traverse both lists, selecting smallest elements first
    while p1 and p2:
        if p1.data <= p2.data:
            tail.next = p1
            p1 = p1.next
        else:
            tail.next = p2
            p2 = p2.next
        tail = tail.next

    # Append remaining nodes in either list
    tail.next = p1 or p2

    merged_sll = SinglyLinkedList()
    merged_sll.head = dummy.next
    return merged_sll


"""
Question #6

Design an algorithm to merge N sorted SLLs (N >= 2).

Approach:
- Reuse merge algorithm from Question 5  
- Merge two lists at a time  
- Append result back to list of lists  
- Continue until only one list remains  
"""
def merge_n_sorted_slls(slls):

    # Helper function: merges two sorted SLLs by inserting values
    def merge(ll1, ll2):
        ll3 = SinglyLinkedList()
        n1 = ll1.head
        n2 = ll2.head

        # Insert smallest nodes from both lists
        while n1 is not None and n2 is not None:
            if n1.data > n2.data:
                ll3.insert(n2.data)
                n2 = n2.next
            else:
                ll3.insert(n1.data)
                n1 = n1.next

        # Append remaining nodes
        while n1 is not None:
            ll3.insert(n1.data)
            n1 = n1.next

        while n2 is not None:
            ll3.insert(n2.data)
            n2 = n2.next

        return ll3

    # Must be at least 2 sorted SLLs
    if not slls or len(slls) < 2:
        raise ValueError("At least two sorted SLLs are required.")

    # Merge repeatedly until only one list remains
    while len(slls) > 1:
        ll1 = slls.pop(0)
        ll2 = slls.pop(0)
        merged = merge(ll1, ll2)
        slls.append(merged)

    return slls[0]


def main():
    # Basic SLL operations
    sll = SinglyLinkedList()
    sll.insert(10)
    sll.insert(20)
    sll.insert(30)
    print("Traverse:", sll.traverse())
    print("Search 20:", sll.search(20))
    print("Search 40:", sll.search(40))
    sll.delete(20)
    print("Traverse after deleting 20:", sll.traverse())

    # Sorting the SLL
    sll.insert(5)
    sll.insert(15)
    sll.insert(25)
    print("Traverse before sorting:", sll.traverse())
    sorted_sll = sort_sll(sll)
    print("Traverse after sorting:", sorted_sll.traverse())

    # Reverse SLL
    reversed_sll = reverse_sll(sorted_sll)
    print("Traverse after reversing:", reversed_sll.traverse())

    # Remove nth node from end
    updated_sll = remove_nth_from_end(reversed_sll, 2)
    print("Traverse after removing 2nd node from end:", updated_sll.traverse())
    updated_sll = remove_nth_from_end(updated_sll, 4)
    print("Traverse after removing 4th node from end:", updated_sll.traverse())

    # Merge two sorted SLLs
    sll1 = SinglyLinkedList()
    sll1.insert(1)
    sll1.insert(3)
    sll1.insert(5)
    sll2 = SinglyLinkedList()
    sll2.insert(2)
    sll2.insert(4)
    sll2.insert(6)
    merged_sll = merge_two_sorted_slls(sll1, sll2)
    print("Traverse merged sorted SLLs:", merged_sll.traverse())

    # Merge N sorted SLLs
    list1 = SinglyLinkedList()
    list1.insert(1)
    list1.insert(4)
    list1.insert(10)
    list1.insert(0)
    sorted_list1 = sort_sll(list1)

    list2 = SinglyLinkedList()
    list2.insert(2)
    list2.insert(5)
    list2.insert(-3)
    list2.insert(-6)
    sorted_list2 = sort_sll(list2)

    list3 = SinglyLinkedList()
    list3.insert(3)
    list3.insert(7)
    list3.insert(8)
    sorted_list3 = sort_sll(list3)

    print(sorted_list1.traverse())
    print(sorted_list2.traverse())
    print(sorted_list3.traverse())

    merged_list = merge_n_sorted_slls([sorted_list1, sorted_list2, sorted_list3])
    print("Merged list:", merged_list.traverse())


if __name__ == "__main__":
    main()

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Maps original node -> copied node
        hashmap = {}

        # Pass 1: Create a copy of every node
        curr = head
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next

        # Pass 2: Assign next and random pointers
        curr = head
        while curr:
            copy = hashmap[curr]

            copy.next = hashmap.get(curr.next)
            copy.random = hashmap.get(curr.random)

            curr = curr.next

        return hashmap[head]


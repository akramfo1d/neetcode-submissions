class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Interleave copied nodes
        temp = head
        while temp:
            copy = Node(temp.val)
            copy.next = temp.next
            temp.next = copy
            temp = copy.next

        # Step 2: Set random pointers
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        # Step 3: Separate the lists
        temp = head
        copy_head = head.next

        while temp:
            copy = temp.next
            temp.next = copy.next

            if copy.next:
                copy.next = copy.next.next

            temp = temp.next

        return copy_head
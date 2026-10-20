
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldtonew = {}

        def clone(node):
            if node in oldtonew:
                return oldtonew[node]

            copy = Node(node.val)
            oldtonew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))

            return copy

        return clone(node)

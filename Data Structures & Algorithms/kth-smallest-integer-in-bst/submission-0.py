class Solution:
    def kthSmallest(self, root, k):
        def inorder(node):
            nonlocal k

            if not node:
                return None

            result = inorder(node.left)

            if result is not None:
                return result

            k -= 1

            if k == 0:
                return node.val

            return inorder(node.right)

        return inorder(root)
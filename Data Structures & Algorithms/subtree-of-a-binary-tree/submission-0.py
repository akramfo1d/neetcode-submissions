class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return False
            
            if node.val == subRoot.val and equalroot(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
        
        def equalroot(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            
            return equalroot(p.left, q.left) and equalroot(p.right, q.right)
        
        return dfs(root)
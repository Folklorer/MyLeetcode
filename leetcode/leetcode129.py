# 240730

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root) -> int:
        def dfs(root,prev):
            if not root:
                return 0
            tmp = prev*10+root.val
            if not root.left and not root.right:
                return tmp
            else:
                return dfs(root.left,tmp)+dfs(root.right,tmp)
        return dfs(root,0)
# 240729
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        if not root:
            return None
        self.left = self.invertTree(self.left)
        self.right = self.invertTree(self.right)
        self.left, self.right = self.right, self.left
        return root
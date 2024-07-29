# 240729

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        lst = []
        def bl(root):
            if root:
                lst.append(root)
                bl(root.left)
                bl(root.right)
        bl(root)
        for i in range(len(lst)-1):
            now, next=lst[i],lst[i+1]
            now.left = None
            now.right = next

            
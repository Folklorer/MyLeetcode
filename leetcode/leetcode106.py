# 240729
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        root.left, root.right = self.buildTree(inorder[:idx],postorder[:idx]),self.buildTree(inorder[idx+1:],postorder[idx:-1])
        return root

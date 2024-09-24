#Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        curTotal = 0
        curNode = root

        if root.left is None and root.right is None and root == targetSum:
            return True
        
        while curNode is not None:
            curTotal += curNode.val
            
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        queue = deque((root,))  # 3
        while queue:
            node = queue.popleft() # 5
            node.left, node.right = node.right, node.left  # null, null
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root


# [4, 2, 7, null, 3, 5, 9]

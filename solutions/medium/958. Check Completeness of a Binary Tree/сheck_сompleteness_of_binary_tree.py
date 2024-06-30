from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()                 # [None, None, None, None]
        q.append(root)
        while q:
            node = q.popleft()      # None
            if node is None:
                return not any(q)
            q.append(node.left)
            q.append(node.right)
        return True

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def __init__(self):
        self.stack = deque()
    
    def fill_stack(self, node):
        self.stack.append(node)
        while node.left:
            node = node.left
            self.stack.append(node)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        self.fill_stack(root) #
        precedent_node = self.stack.pop()  # 3
        while self.stack or precedent_node.right:
            if precedent_node.right:
                self.fill_stack(precedent_node.right)
            following_node = self.stack.pop()  # 3
            if following_node.val <= precedent_node.val:
                return False
            precedent_node = following_node
        return True


# 3, 1, 2, 4        

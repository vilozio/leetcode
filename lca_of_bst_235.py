# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def fill_ancestors(self, root: 'TreeNode', target: 'TreeNode', ancestors):
        current = root
        while current:
            ancestors[current.val] = current
            if target.val < current.val:
                current = current.left
            elif target.val > current.val:
                current = current.right
            else:
                current = None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_ancestors = {}
        q_ancestors = {}
        self.fill_ancestors(root, p, p_ancestors)
        self.fill_ancestors(root, q, q_ancestors)
        for p_anc_key, p_ancestor in reversed(p_ancestors.items()):
            if p_anc_key in q_ancestors:
                return p_ancestor

            
# current - 7
# q_ancestors - {6, 8, 7}
# p_ancestors - {6, 2, 0}

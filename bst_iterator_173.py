from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack: List[TreeNode] = []
        self.fill_stack(root)

    def fill_stack(self, x: TreeNode):
        self.stack.append(x)
        while x.left:
            x = x.left
            self.stack.append(x)

    def next(self) -> int:
        y = self.stack.pop()
        if y.right:
            self.fill_stack(y.right)
        return y.val

    def hasNext(self) -> bool:
        return bool(self.stack)


def test():
    nodes = {
        7: TreeNode(7),
        3: TreeNode(3),
        15: TreeNode(15),
        9: TreeNode(9),
        20: TreeNode(20),
    }
    root = nodes[7]
    root.left = nodes[3]
    root.right = nodes[15]
    root.right.left = nodes[9]
    root.right.right = nodes[20]
    bsti = BSTIterator(root)
    assert bsti.next() == 3
    assert bsti.next() == 7
    assert bsti.hasNext() is True
    assert bsti.next() == 9
    assert bsti.hasNext() is True
    assert bsti.next() == 15
    assert bsti.hasNext() is True
    assert bsti.next() == 20
    assert bsti.hasNext() is False

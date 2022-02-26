from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        q = deque()                            # []
        visited = [False] * 100                # [t, t, t, t, t]
        cloned_start = Node(node.val)
        cloned_all = {node.val: cloned_start}  # {1[2, 3, 5], 2[1, 3, 4], 3[1, 2], 5[1, 4], 4[2, 5]}
        q.append(node)
        while q:
            node = q.popleft()                               # 4
            cloned = cloned_all[node.val]
            visited[node.val - 1] = True
            for neighbor in node.neighbors:                  # 5 [2]
                if not visited[neighbor.val - 1]:            # f
                    if neighbor.val in cloned_all:           # f
                        cloned_nei = cloned_all[neighbor.val]
                    else:
                        cloned_nei = Node(neighbor.val)
                        cloned_all[neighbor.val] = cloned_nei
                        q.append(neighbor)
                    cloned_nei.neighbors.append(cloned)
                    cloned.neighbors.append(cloned_nei)
        return cloned_start

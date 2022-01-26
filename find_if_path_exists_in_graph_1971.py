from typing import List
from collections import defaultdict
from queue import Queue


class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        queue = Queue()
        graph = Graph()
        marked = [0] * n
        for edge in edges:
            graph.add_edge(edge[0], edge[1])
        marked[source] = 1
        queue.put(source)
        while not queue.empty():
            node = queue.get()
            if node == destination:
                return True
            for adjacent_node in graph.graph[node]:
                if not marked[adjacent_node]:
                    marked[adjacent_node] = 1
                    queue.put(adjacent_node)
        return False


def call(n, edges, source, destination):
    s = Solution()
    return s.validPath(n, edges, source, destination)


def test():
    assert call(3, [[0, 1], [1, 2], [2, 0]], 0, 2) is True
    assert call(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5) is False

from typing import List
from collections import defaultdict
from queue import Queue


class Graph:
    def __init__(self):
        self.nodes = defaultdict(set)

    def add_edge(self, v, u):
        self.nodes[v].add(u)
        self.nodes[u].add(v)


class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        graph = Graph()
        for node1, node2 in corridors:
            graph.add_edge(node1, node2)
        triplets = set()
        queue = Queue()
        visited = [False] * n
        for corridor in corridors:
            if not visited[corridor[0] - 1]:
                queue.put(corridor[0])
                while not queue.empty():
                    node = queue.get()
                    adjacents = graph.nodes[node]
                    for adjacent in adjacents:
                        if not visited[adjacent - 1]:
                            second_adjacents = graph.nodes[adjacent]
                            for third_adjacent in adjacents:
                                if third_adjacent in second_adjacents:
                                    triplets.add(frozenset((node, adjacent, third_adjacent)))
                            queue.put(adjacent)
                    visited[node - 1] = True
        return len(triplets)


def call(n, corridors):
    s = Solution()
    return s.numberOfPaths(n, corridors)


def test():
    assert call(5, [[1, 2], [5, 2], [4, 1], [2, 4], [3, 1], [3, 4]]) == 2
    assert call(4, [[1, 2], [3, 4]]) == 0
    assert call(5, [[4, 1], [4, 2], [3, 4], [5, 3], [5, 2], [1, 3], [3, 2], [2, 1], [5, 4], [5, 1]]) == 10

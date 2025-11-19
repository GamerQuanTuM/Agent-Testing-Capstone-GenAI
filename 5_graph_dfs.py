"""
Graph DFS traversal
Provide DFS (recursive and iterative) for adjacency-list graphs.
"""
from typing import Dict, List, Set


def dfs_recursive(graph: Dict[int, List[int]], start: int, visited: Set[int] = None) -> List[int]:
    if visited is None:
        visited = set()
    res = []

    def _dfs(node: int):
        visited.add(node)
        res.append(node)
        for nbr in graph.get(node, []):
            if nbr not in visited:
                _dfs(nbr)

    _dfs(start)
    return res


def dfs_iterative(graph: Dict[int, List[int]], start: int) -> List[int]:
    visited = set()
    stack = [start]
    res = []
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        res.append(node)
        # push neighbors in reverse order to mimic recursive order
        for nbr in reversed(graph.get(node, [])):
            if nbr not in visited:
                stack.append(nbr)
    return res


if __name__ == '__main__':
    g = {
        1: [2, 3],
        2: [4],
        3: [5],
        4: [],
        5: []
    }
    print('dfs_recursive from 1 ->', dfs_recursive(g, 1))
    print('dfs_iterative from 1 ->', dfs_iterative(g, 1))

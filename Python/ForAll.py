from typing import List
from functools import cache


class Solution:
    FOUND = 0

    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        roots = set()
        self.edges = edges
        self.guesses = guesses
        self.guesses_length = len(guesses)

        for left, right in edges:
            roots.add(left)
            roots.add(right)

        ans = 0

        for root in roots:
            found_count = 0
            self.dfs_find(root, None)

            if self.FOUND >= k:
                ans += 1

            self.FOUND = 0

        return ans

    #@cache
    def dfs_find(self, root, parent):
        if self.FOUND == self.guesses_length:
            return

        next_level = []

        for edge in self.edges:
            if root in edge:
                second_val = edge[1 - edge.index(root)]
                if parent is None or second_val != parent:
                    next_level.append(second_val)

        for node in next_level:
            for guess in self.guesses:
                if guess[0] == root and guess[1] == node:
                    self.FOUND += 1

        for node in next_level:
            self.dfs_find(node, root)


def dfs_edges(edges: list, root, parent):
    print(root)
    next_level = []

    for edge in edges:
        if root in edge:
            second_val = edge[1 - edge.index(root)]
            if parent is None or second_val != parent:
                next_level.append(edge[1 - edge.index(root)])

    for node in next_level:
        dfs_edges(edges, node, root)


if __name__ == "__main__":
    # edges = [[0, 1], [1, 2], [1, 3], [4, 2]]
    # guesses = [[1, 3], [0, 1], [1, 0], [2, 4]]
    # k = 3

    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    guesses = [[1, 0], [3, 4], [2, 1], [3, 2]]
    k = 1

    #dfs_edges(edges, 4, None)

    print(Solution().rootCount(edges, guesses, k))

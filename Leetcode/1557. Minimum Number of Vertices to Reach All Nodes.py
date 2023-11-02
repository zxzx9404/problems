class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        adj_list = [[] for _ in range(n)]
        ans = []
        for i, j in edges:
            adj_list[j].append(i)

        for idx, k in enumerate(adj_list):
            if not k:
               ans.append(idx)
        return ans
